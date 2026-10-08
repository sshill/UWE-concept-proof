#!/usr/bin/env python3
"""
Dedicated Compiler for Defense One Op-Ed Submission.
Extracts strictly Part 2 (The Manuscript), formats typography, renders formulas,
and generates .docx, .pdf, .odt, and .html via headless LibreOffice.
"""

import re
import os
import sys
import html
import subprocess
import shutil

def format_math_symbols(content):
    replacements = [
        (r'\\approx', '≈'),
        (r'\\le', '≤'),
        (r'\\ge', '≥'),
        (r'\\ne', '≠'),
        (r'\\pm', '±'),
        (r'\\times', '×'),
        (r'\\cdot', '·'),
        (r'\\to', '→'),
        (r'\\rightarrow', '→'),
        (r'\\leftarrow', '←'),
        (r'\\Delta', 'Δ'),
        (r'\\lambda', 'λ'),
        (r'\\nabla', '∇'),
        (r'\\mu', 'μ'),
        (r'\\dots', '…'),
        (r'\\cdots', '⋯'),
        (r'\\in', '∈'),
        (r'\\infty', '∞'),
        (r'\\mathbf{([^}]+)}', r'<b>\1</b>'),
        (r'\\text{([^}]+)}', r'\1'),
        (r'\\textsubscript{([^}]+)}', r'<sub>\1</sub>'),
        (r'\\textsuperscript{([^}]+)}', r'<sup>\1</sup>'),
        (r'\^{([0-9A-Za-z\-+]+)}', r'<sup>\1</sup>'),
        (r'\^([0-9]+)', r'<sup>\1</sup>'),
        (r'_\{([0-9A-Za-z\-+]+)\}', r'<sub>\1</sub>'),
        (r'_([0-9A-Za-z])', r'<sub>\1</sub>'),
        (r'\\,', ' '),
        (r'\\;', ' '),
    ]
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
    return content

def inline_formatting(text):
    # 1. Protect code spans
    code_tokens = []
    def save_code(m):
        code_tokens.append(m.group(1))
        return f"{{{{CODETOKEN:{len(code_tokens)-1}}}}}"
    text = re.sub(r'`([^`]+)`', save_code, text)

    # 2. Protect escaped dollars
    dollar_tokens = []
    def save_dollar(m):
        dollar_tokens.append("$" + m.group(1))
        return f"{{{{DOLLARESC:{len(dollar_tokens)-1}}}}}"
    text = re.sub(r'\\\$([0-9A-Za-z]+)', save_dollar, text)
    text = text.replace(r'\$', '&#36;')

    # 3. Protect links
    link_tokens = []
    def save_link(m):
        label = m.group(1)
        url = m.group(2)
        idx = len(link_tokens)
        link_tokens.append((label, url))
        return f"{{{{LINKTOKEN:{idx}}}}}"
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', save_link, text)

    # 4. Handle block math formulas
    def replace_block_math(m):
        content = m.group(1).strip()
        if "Aerial" in content or "Regime" in content:
            rendered = (
                '<div style="text-align: center; margin: 12pt 0; padding: 10pt; background-color: #f8fafc; border: 1.5px solid #0f2b48; border-radius: 4px;">'
                '<div style="font-size: 11pt; font-weight: bold; color: #0f2b48; letter-spacing: 0.5px;">'
                'Aerial Platform = [ Regime &middot; Launch Mode ] &minus; [ Powerplant &middot; Mission Vector ] &minus; [ Autonomy &middot; Control ]'
                '</div>'
                '<div style="font-size: 8.5pt; color: #475569; margin-top: 3pt; font-style: italic;">'
                'The Six-Character Unmanned Aerial &amp; Copter Taxonomy Matrix'
                '</div>'
                '</div>'
            )
            return rendered
        if "[\\mathbf{O}\\mathbf{P}]" in content or "[OP]" in content or "[O P]" in content:
            rendered = (
                '<div style="text-align: center; margin: 8pt 0 12pt 0; font-size: 13pt; font-weight: bold; color: #0f2b48; letter-spacing: 2px;">'
                '[ O P ] &minus; [ E M ] &minus; [ T C ]'
                '</div>'
            )
            return rendered

        formatted = format_math_symbols(content)
        formatted = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1 / \2', formatted)
        formatted = re.sub(r'\\([a-zA-Z]+)', r'\1', formatted)
        return f'<div style="text-align: center; margin: 12pt 0; font-family: \'Cambria Math\', \'Times New Roman\', serif; font-size: 13pt; color: #0f2b48; font-style: italic;">{formatted}</div>'

    text = re.sub(r'\$\$(.*?)\$\$', replace_block_math, text, flags=re.DOTALL)

    # 5. Handle inline math
    def replace_inline_math(m):
        m_content = m.group(1).strip()
        formatted = format_math_symbols(m_content)
        return f'<span style="font-style: italic; font-weight: 500;">{formatted}</span>'

    text = re.sub(r'\$([^\$]+)\$', replace_inline_math, text)

    # 6. Markdown bold & italic
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

    # 7. Restore links
    for i, (label, url) in enumerate(link_tokens):
        text = text.replace(f"{{{{LINKTOKEN:{i}}}}}", f'<a href="{url}" style="color: #0284c7; text-decoration: underline;">{label}</a>')

    # 8. Restore code spans
    for i, token in enumerate(code_tokens):
        escaped = html.escape(token)
        text = text.replace(f"{{{{CODETOKEN:{i}}}}}", f'<code style="font-family: Consolas, monospace; background-color: #f1f5f9; padding: 1px 4px; border-radius: 3px; font-size: 8.5pt; color: #0f172a; border: 1px solid #cbd5e1;">{escaped}</code>')

    # 9. Restore escaped dollar signs
    for i, tok in enumerate(dollar_tokens):
        text = text.replace(f"{{{{DOLLARESC:{i}}}}}", tok)

    return text

def md_to_html(md_text, title="Why the Pentagon Must Retire FPV - Defense One Op-Ed"):
    lines = md_text.splitlines()
    html_lines = []

    css = """
    @page {
        size: A4;
        margin: 16mm 18mm 16mm 18mm;
    }
    body {
        font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
        line-height: 1.34;
        font-size: 10pt;
        color: #1e293b;
        max-width: 820px;
        margin: 0 auto;
    }
    h1 {
        font-size: 18pt;
        font-weight: 800;
        color: #0f2b48;
        line-height: 1.2;
        margin-top: 14pt;
        margin-bottom: 6pt;
        border-bottom: 2px solid #0f2b48;
        padding-bottom: 6pt;
    }
    h2 {
        font-size: 13pt;
        font-weight: 700;
        color: #0f2b48;
        margin-top: 14pt;
        margin-bottom: 4pt;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 3pt;
    }
    h3 {
        font-size: 11pt;
        font-weight: 700;
        color: #1e3a8a;
        margin-top: 11pt;
        margin-bottom: 3pt;
    }
    h4 {
        font-size: 10pt;
        font-weight: 700;
        color: #334155;
        margin-top: 8pt;
        margin-bottom: 2pt;
    }
    p {
        margin-top: 4pt;
        margin-bottom: 5pt;
        text-align: justify;
    }
    ul, ol {
        margin-top: 3pt;
        margin-bottom: 5pt;
        padding-left: 20pt;
    }
    li {
        margin-bottom: 2.5pt;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin-top: 8pt;
        margin-bottom: 10pt;
        font-size: 8.5pt;
    }
    th, td {
        border: 1px solid #cbd5e1;
        padding: 5pt 7pt;
        text-align: left;
    }
    th {
        background-color: #f1f5f9;
        font-weight: 700;
        color: #0f2b48;
    }
    tr:nth-child(even) td {
        background-color: #f8fafc;
    }
    blockquote {
        margin: 8pt 0;
        padding: 5pt 12pt;
        border-left: 3.5px solid #0284c7;
        background-color: #f0f9ff;
        color: #0369a1;
        font-style: italic;
    }
    hr {
        border: 0;
        border-top: 1px solid #cbd5e1;
        margin: 10pt 0;
    }
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 10pt auto;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
    }
    .caption {
        text-align: center;
        font-size: 8pt;
        color: #64748b;
        font-style: italic;
        margin-top: -6pt;
        margin-bottom: 10pt;
    }
    """

    html_lines.append("<!DOCTYPE html>")
    html_lines.append("<html lang='en'>")
    html_lines.append("<head>")
    html_lines.append("<meta charset='utf-8'>")
    html_lines.append(f"<title>{html.escape(title)}</title>")
    html_lines.append(f"<style>{css}</style>")
    html_lines.append("</head>")
    html_lines.append("<body>")

    i = 0
    in_list = None
    in_table = False

    while i < len(lines):
        line = lines[i]
        raw_strip = line.strip()

        if not raw_strip:
            if in_list:
                html_lines.append(f"</{in_list}>")
                in_list = None
            if in_table:
                html_lines.append("</tbody></table>")
                in_table = False
            i += 1
            continue

        if raw_strip.startswith("```"):
            if in_list:
                html_lines.append(f"</{in_list}>")
                in_list = None
            code_block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_block.append(lines[i])
                i += 1
            i += 1
            escaped_code = html.escape("\n".join(code_block))
            html_lines.append(f'<pre style="background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 8pt; border-radius: 4px; font-family: Consolas, monospace; font-size: 8.5pt; overflow-x: auto;"><code>{escaped_code}</code></pre>')
            continue

        if raw_strip.startswith("$$"):
            math_block = [raw_strip]
            if not (raw_strip.endswith("$$") and len(raw_strip) > 2):
                i += 1
                while i < len(lines) and not lines[i].strip().endswith("$$"):
                    math_block.append(lines[i])
                    i += 1
                if i < len(lines):
                    math_block.append(lines[i])
            full_math = "\n".join(math_block)
            rendered_math = inline_formatting(full_math)
            html_lines.append(rendered_math)
            i += 1
            continue

        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', raw_strip)
        if img_match:
            alt_text = img_match.group(1)
            img_src = img_match.group(2)
            if not os.path.isabs(img_src):
                img_src = os.path.abspath(os.path.join("/home/hills/Documents/UWS", img_src))
            html_lines.append(f'<div style="text-align: center; margin: 12pt 0; page-break-inside: avoid;">')
            html_lines.append(f'  <img src="{img_src}" alt="{html.escape(alt_text)}" style="max-width: 100%; height: auto; border: 1.5px solid #0f2b48; border-radius: 4px;" />')
            if alt_text:
                html_lines.append(f'  <div style="font-size: 8pt; color: #475569; margin-top: 4pt; font-style: italic; font-weight: 600;">{html.escape(alt_text)}</div>')
            html_lines.append('</div>')
            i += 1
            continue

        if raw_strip.startswith("#"):
            if in_list:
                html_lines.append(f"</{in_list}>")
                in_list = None
            if in_table:
                html_lines.append("</tbody></table>")
                in_table = False

            level = len(raw_strip) - len(raw_strip.lstrip("#"))
            title_text = raw_strip.lstrip("#").strip()
            title_formatted = inline_formatting(title_text)
            level = min(level, 4)
            html_lines.append(f"<h{level}>{title_formatted}</h{level}>")
            i += 1
            continue

        if re.match(r'^(---+|\*\*\*+|___+)$', raw_strip):
            if in_list:
                html_lines.append(f"</{in_list}>")
                in_list = None
            if in_table:
                html_lines.append("</tbody></table>")
                in_table = False
            html_lines.append("<hr />")
            i += 1
            continue

        list_match = re.match(r'^(\*|-|\+)\s+(.+)$', raw_strip)
        if list_match:
            item_text = inline_formatting(list_match.group(2))
            if in_list != "ul":
                if in_list:
                    html_lines.append(f"</{in_list}>")
                html_lines.append("<ul>")
                in_list = "ul"
            html_lines.append(f"<li>{item_text}</li>")
            i += 1
            continue

        num_list_match = re.match(r'^\d+\.\s+(.+)$', raw_strip)
        if num_list_match:
            item_text = inline_formatting(num_list_match.group(1))
            if in_list != "ol":
                if in_list:
                    html_lines.append(f"</{in_list}>")
                html_lines.append("<ol>")
                in_list = "ol"
            html_lines.append(f"<li>{item_text}</li>")
            i += 1
            continue

        if raw_strip.startswith(">"):
            if in_list:
                html_lines.append(f"</{in_list}>")
                in_list = None
            bq_text = inline_formatting(raw_strip.lstrip(">").strip())
            html_lines.append(f"<blockquote>{bq_text}</blockquote>")
            i += 1
            continue

        p_formatted = inline_formatting(raw_strip)
        html_lines.append(f"<p>{p_formatted}</p>")
        i += 1

    if in_list:
        html_lines.append(f"</{in_list}>")
    if in_table:
        html_lines.append("</tbody></table>")

    html_lines.append("</body>")
    html_lines.append("</html>")
    return "\n".join(html_lines)

def convert():
    base_dir = "/home/hills/Documents/UWS"
    md_file = os.path.join(base_dir, "UWE_Defense_One_OpEd.md")
    html_file = os.path.join(base_dir, "UWE_Defense_One_OpEd.html")
    odt_file = os.path.join(base_dir, "UWE_Defense_One_OpEd.odt")
    docx_file = os.path.join(base_dir, "UWE_Defense_One_OpEd.docx")
    pdf_file = os.path.join(base_dir, "UWE_Defense_One_OpEd.pdf")

    print(f"Reading {md_file}...")
    with open(md_file, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Extract strictly Part 2
    part2_marker = "## PART 2: THE COMPLETE OP-ED MANUSCRIPT"
    if part2_marker in full_content:
        manuscript_md = full_content.split(part2_marker)[1].strip()
        print("Extracted Part 2 (The Op-Ed Manuscript) exclusively for Defense One.")
    else:
        manuscript_md = full_content

    html_content = md_to_html(manuscript_md, title="Why the Pentagon Must Retire FPV - Defense One Op-Ed")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Wrote HTML: {html_file}")

    lo_user = "file:///home/hills/Documents/UWS/.lo_user"
    staging_dir = "/tmp/lo_staging"
    os.makedirs(staging_dir, exist_ok=True)

    # Step 1: HTML -> ODT
    cmd_odt = [
        "libreoffice",
        f"-env:UserInstallation={lo_user}",
        "--headless",
        "--convert-to", "odt",
        html_file,
        "--outdir", staging_dir
    ]
    print("Converting HTML to ODT...")
    subprocess.run(cmd_odt, check=True)
    staged_odt = os.path.join(staging_dir, "UWE_Defense_One_OpEd.odt")
    shutil.copy2(staged_odt, odt_file)

    # Step 2: ODT -> DOCX
    cmd_docx = [
        "libreoffice",
        f"-env:UserInstallation={lo_user}",
        "--headless",
        "--convert-to", "docx",
        staged_odt,
        "--outdir", staging_dir
    ]
    print("Converting ODT to DOCX...")
    subprocess.run(cmd_docx, check=True)
    staged_docx = os.path.join(staging_dir, "UWE_Defense_One_OpEd.docx")
    shutil.copy2(staged_docx, docx_file)

    # Step 3: ODT -> PDF
    cmd_pdf = [
        "libreoffice",
        f"-env:UserInstallation={lo_user}",
        "--headless",
        "--convert-to", "pdf",
        staged_odt,
        "--outdir", staging_dir
    ]
    print("Converting ODT to PDF...")
    subprocess.run(cmd_pdf, check=True)
    staged_pdf = os.path.join(staging_dir, "UWE_Defense_One_OpEd.pdf")
    shutil.copy2(staged_pdf, pdf_file)

    print("Conversion completed successfully!")
    print(f"DOCX: {docx_file}")
    print(f"PDF:  {pdf_file}")

if __name__ == "__main__":
    convert()
