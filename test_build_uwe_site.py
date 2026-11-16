import contextlib
import copy
import io
import re
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest import mock
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True

import build_uwe_site as site


class PageLinks(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.links = []
        self.ids = set()
        self.segments = []
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if "spec-seg" in attrs.get("class", "").split():
            self.segments.append(attrs)


class TestSiteBuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        temporary = tempfile.TemporaryDirectory(prefix="uwe-site-test-")
        cls.addClassCleanup(temporary.cleanup)
        cls.docs = Path(temporary.name) / "docs"
        with mock.patch.object(site, "DOCS", cls.docs), contextlib.redirect_stdout(io.StringIO()):
            site.main()
        cls.pages = {
            path: PageLinks(path.read_text(encoding="utf-8"))
            for path in cls.docs.rglob("*.html")
        }

    def test_build_exposes_new_cases_and_both_c2_articles(self):
        for case in site.CASES_DATA:
            with self.subTest(case=case["id"]):
                self.assertTrue((self.docs / "cases" / f"{case['slug']}.html").is_file())
        c2_index = self.pages[self.docs / "c2" / "index.html"]
        self.assertIn("officer.html", c2_index.links)
        self.assertIn(Path(site.C2_ARTICLE_PATH).name, c2_index.links)
        article = self.pages[self.docs / site.C2_ARTICLE_PATH]
        self.assertIn("../cases/32-izzy-fried-c2.html", article.links)
        self.assertIn("https://lnkd.in/p/d9qXKrmm", article.links)
        sitemap = (self.docs / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn(f"{site.BASE_URL}/{site.C2_ARTICLE_PATH}", sitemap)

    def test_c2_is_not_rendered_as_a_physical_taxonomy(self):
        index = self.pages[self.docs / "domains" / "index.html"]
        self.assertNotIn("c2.html", index.links)
        self.assertIn("../c2/index.html", index.links)
        self.assertFalse((self.docs / "domains" / "c2.html").exists())
        for domain in site.DOMAINS_DATA:
            for slug in domain["cases"]:
                self.assertIn(f"../cases/{slug}.html", index.links)
        case = self.pages[self.docs / "cases" / "32-izzy-fried-c2.html"]
        self.assertIn("../c2/index.html", case.links)
        self.assertIn(f"../{site.C2_ARTICLE_PATH}", case.links)

    def test_category_filters_and_spectrum_keep_c2_without_losing_percentages(self):
        pills, _ = site.render_filter_pills()
        self.assertIn('data-domain-filter="C2"', pills)
        spectrum = PageLinks(site.render_spectrum_bar())
        categories = {segment["data-domain-filter"] for segment in spectrum.segments}
        self.assertEqual(categories, {case["domain"] for case in site.CASES_DATA})
        widths = [
            int(re.search(r"width:(\d+)%", segment["style"]).group(1))
            for segment in spectrum.segments
        ]
        self.assertEqual(sum(widths), 100)

    def test_all_generated_local_files_and_anchors_resolve(self):
        for path, page in self.pages.items():
            for link in page.links:
                parts = urlsplit(link)
                if parts.scheme or parts.netloc:
                    continue
                with self.subTest(page=str(path.relative_to(self.docs)), link=link):
                    target = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                    if target.is_dir():
                        target /= "index.html"
                    self.assertTrue(target.is_file(), f"Missing target: {target}")
                    if parts.fragment and target in self.pages:
                        self.assertIn(unquote(parts.fragment), self.pages[target].ids)

    def test_validator_still_rejects_an_undeclared_collision(self):
        cases = copy.deepcopy(site.CASES_DATA)
        cases[0]["token"] = cases[2]["token"]
        with self.assertRaisesRegex(ValueError, "Unauthorized token collision"):
            site.validate_uwe_integrity(cases, site.VENDORS_DATA, site.DOMAINS_DATA, self.docs)

    def test_validator_rejects_wrong_physical_domain_assignment(self):
        domains = copy.deepcopy(site.DOMAINS_DATA)
        domains[0]["cases"][0], domains[2]["cases"][0] = (
            domains[2]["cases"][0], domains[0]["cases"][0]
        )
        with self.assertRaisesRegex(ValueError, "Incorrect case assignment"):
            site.validate_uwe_integrity(site.CASES_DATA, site.VENDORS_DATA, domains, self.docs)


if __name__ == "__main__":
    unittest.main()
