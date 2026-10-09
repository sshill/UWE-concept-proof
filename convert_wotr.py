#!/usr/bin/env python3
"""
Dedicated Compiler for War on the Rocks In-Depth Analytical Essay.
Extracts strictly Part 2 (The Complete Analytical Essay), formats typography,
renders formulas and figures, and generates .docx, .pdf, .odt, and .html via headless LibreOffice.
"""

import re
import os
import sys
import html
import subprocess
import shutil

def parse_math_to_html(formula_str):
    s = formula_str.strip()
    if s.startswith("$$") and s.endswith("$$"):
        s = s[2:-2].strip()
    elif s.startswith("$") and s.endswith("$"):
        s = s[1:-1].strip()

    # Step 1: Strip \left and \right delimiters
    s = re.sub(r"\\left\s*([(\[{|])", r"\1", s)
    s = re.sub(r"\\right\s*([)\]}|])", r"\1", s)
    s = re.sub(r"\\left\b", "", s)
    s = re.sub(r"\\right\b", "", s)

    # Step 2: Strip \text{...} and tab+ext{...}
    s = re.sub(r"\\text\{\s*([^}]+)\s*\}", r"\1", s)
    s = re.sub(r"[\t\\]+ext\{\s*([^}]+)\s*\}", r"\1", s)

    # Step 3: Math symbols and greek letters
    s = s.replace(r"\approx", "≈")
    s = s.replace(r"\cdot", "·")
    s = s.replace(r"\times", "×")
    s = s.replace(r"\pm", "±")
    s = re.sub(r"\\gg\b", "≫", s)
    s = re.sub(r"\\ll\b", "≪", s)
    s = re.sub(r"\\le\b", "≤", s)
    s = re.sub(r"\\ge\b", "≥", s)
    s = re.sub(r"\\ne\b", "≠", s)
    s = s.replace(r"\sigma", "σ")
    s = s.replace(r"\tau", "τ")
    s = s.replace(r"\Delta", "Δ")
    s = s.replace(r"\lambda", "λ")
    s = s.replace(r"\nabla", "∇")
    s = s.replace(r"\mu", "μ")
    s = s.replace(r"\,", " ")
    s = s.replace(r"\;", " ")
    s = s.replace(r"\ ", " ")

    # Step 4: \mathbf
    s = re.sub(r"\\mathbf\{\s*([^}]+)\s*\}", r"<b>\1</b>", s)

    # Step 5: \sqrt with nested braces
    s = re.sub(r"\\sqrt\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", r"√(\1)", s)
    s = re.sub(r"\\sqrt\s*([0-9a-zA-Z])", r"√\1", s)

    # Step 6: Subscripts and superscripts
    s = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", s)
    s = re.sub(r"_([0-9A-Za-z])", r"<sub>\1</sub>", s)
    s = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"\^([0-9A-Za-z])", r"<sup>\1</sup>", s)

    # Step 7: Clean leftover backslashes
    s = s.replace("\\", "")
    return s

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
        link_tokens.append((label, url))
        return f"{{{{LINKTOKEN:{len(link_tokens)-1}}}}}"
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', save_link, text)

    # 4. Parse inline math ($...$)
    def repl_inline_math(m):
        math_content = m.group(1)
        # Avoid matching empty or invalid
        if not math_content.strip():
            return "$$"
        return parse_math_to_html(math_content)
    text = re.sub(r'\$([^\$]+)\$', repl_inline_math, text)

    # 5. Bold and Italic
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    text = re.sub(r'___([^_]+)___', r'<b><i>\1</i></b>', text)
    text = re.sub(r'__([^_]+)__', r'<b>\1</b>', text)
    text = re.sub(r'_([^_]+)_', r'<i>\1</i>', text)

    # 6. Restore links
    for idx, (label, url) in enumerate(link_tokens):
        formatted_label = inline_formatting(label)
        link_html = f'<a href="{html.escape(url)}" style="color: #0284c7; text-decoration: underline;">{formatted_label}</a>'
        text = text.replace(f"{{{{LINKTOKEN:{idx}}}}}", link_html)

    # 7. Restore dollars
    for idx, val in enumerate(dollar_tokens):
        text = text.replace(f"{{{{DOLLARESC:{idx}}}}}", val)

    # 8. Restore code spans
    for idx, code_val in enumerate(code_tokens):
        escaped_code = html.escape(code_val)
        code_html = f'<code style="font-family: Consolas, monospace; background-color: #f1f5f9; padding: 1pt 3pt; border-radius: 3px; font-size: 8.5pt; color: #0f172a; border: 1px solid #e2e8f0;">{escaped_code}</code>'
        text = text.replace(f"{{{{CODETOKEN:{idx}}}}}", code_html)

    return text

def md_to_html(md_content, title="War on the Rocks Essay"):
    html_lines = []
    html_lines.append("<!DOCTYPE html>")
    html_lines.append("<html lang=\"en\">")
    html_lines.append("<head>")
    html_lines.append("<meta charset=\"UTF-8\">")
    html_lines.append(f"<title>{html.escape(title)}</title>")
    html_lines.append("""
<style>
    @page {
        size: A4;
        margin: 20mm 18mm 20mm 18mm;
    }
    body {
        font-family: 'Georgia', 'Times New Roman', serif;
        font-size: 10.5pt;
        line-height: 1.55;
        color: #1e293b;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }
    h1 {
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 18pt;
        font-weight: 800;
        color: #0b1f3a;
        margin-top: 14pt;
        margin-bottom: 6pt;
        line-height: 1.25;
        border-bottom: 2px solid #0b1f3a;
        padding-bottom: 4pt;
    }
    h2 {
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 13.5pt;
        font-weight: 700;
        color: #1e3a8a;
        margin-top: 14pt;
        margin-bottom: 5pt;
        line-height: 1.3;
    }
    h3 {
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 11.5pt;
        font-weight: 700;
        color: #1d4ed8;
        margin-top: 12pt;
        margin-bottom: 4pt;
        line-height: 1.3;
    }
    h4 {
        font-family: 'Segoe UI', Arial, sans-serif;
        font-size: 10.5pt;
        font-weight: 700;
        color: #334155;
        margin-top: 10pt;
        margin-bottom: 3pt;
    }
    p {
        margin-top: 0;
        margin-bottom: 7pt;
        text-align: justify;
    }
    blockquote {
        margin: 8pt 0;
        padding: 7pt 12pt;
        background-color: #f8fafc;
        border-left: 3.5px solid #0284c7;
        font-size: 9.5pt;
        color: #334155;
        font-style: italic;
    }
    ul, ol {
        margin-top: 0;
        margin-bottom: 7pt;
        padding-left: 18pt;
    }
    li {
        margin-bottom: 3pt;
        text-align: justify;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 10pt 0;
        font-size: 9pt;
        page-break-inside: avoid;
    }
    th, td {
        border: 1px solid #cbd5e1;
        padding: 5pt 7pt;
        text-align: left;
    }
    th {
        background-color: #0f2b48;
        color: #ffffff;
        font-family: 'Segoe UI', Arial, sans-serif;
        font-weight: 600;
    }
    tr:nth-child(even) td {
        background-color: #f8fafc;
    }
    hr {
        border: none;
        border-top: 1px solid #cbd5e1;
        margin: 12pt 0;
    }
</style>
""")
    html_lines.append("</head>")
    html_lines.append("<body>")

    lines = md_content.split("\n")
    in_table = False
    in_list = None
    i = 0

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

        if raw_strip.startswith("|") and raw_strip.endswith("|"):
            cells = [c.strip() for c in raw_strip[1:-1].split("|")]
            if not in_table:
                if in_list:
                    html_lines.append(f"</{in_list}>")
                    in_list = None
                in_table = True
                html_lines.append("<table><thead><tr>")
                for c in cells:
                    html_lines.append(f"<th>{inline_formatting(c)}</th>")
                html_lines.append("</tr></thead><tbody>")
                if i + 1 < len(lines) and re.match(r'^\|[\s:-|]+\|$', lines[i+1].strip()):
                    i += 1
            else:
                html_lines.append("<tr>")
                for c in cells:
                    html_lines.append(f"<td>{inline_formatting(c)}</td>")
                html_lines.append("</tr>")
            i += 1
            continue
        elif in_table:
            html_lines.append("</tbody></table>")
            in_table = False

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
            html_lines.append(f'<pre style="background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 7pt; border-radius: 4px; font-family: Consolas, monospace; font-size: 8pt; overflow-x: auto; page-break-inside: avoid;"><code>{escaped_code}</code></pre>')
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
            rendered_math = parse_math_to_html(full_math)
            html_lines.append(f'<div style="text-align: center; margin: 10pt 0; font-family: \'Georgia\', \'Times New Roman\', serif; font-size: 11pt; font-weight: bold; color: #0b1f3a; page-break-inside: avoid;">{rendered_math}</div>')
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
                html_lines.append(f'  <div style="font-size: 8.5pt; color: #475569; margin-top: 4pt; font-style: italic; font-weight: 600;">{html.escape(alt_text)}</div>')
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
    md_file = os.path.join(base_dir, "UWE_War_on_the_Rocks_Essay.md")
    html_file = os.path.join(base_dir, "UWE_War_on_the_Rocks_Essay.html")
    odt_file = os.path.join(base_dir, "UWE_War_on_the_Rocks_Essay.odt")
    docx_file = os.path.join(base_dir, "UWE_War_on_the_Rocks_Essay.docx")
    pdf_file = os.path.join(base_dir, "UWE_War_on_the_Rocks_Essay.pdf")

    print(f"Reading {md_file}...")
    with open(md_file, "r", encoding="utf-8") as f:
        full_content = f.read()

    part2_marker = "## PART 2: THE COMPLETE ANALYTICAL ESSAY"
    if part2_marker in full_content:
        manuscript_md = full_content.split(part2_marker)[1].strip()
        print("Extracted Part 2 (The Analytical Essay) exclusively for War on the Rocks.")
    else:
        manuscript_md = full_content

    html_content = md_to_html(manuscript_md, title="The Death of MALE Sanctuaries - War on the Rocks Essay")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Wrote HTML: {html_file}")

    lo_user = "file:///home/hills/Documents/UWS/.lo_user"
    staging_dir = "/tmp/lo_staging_wotr"
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
    staged_odt = os.path.join(staging_dir, "UWE_War_on_the_Rocks_Essay.odt")
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
    staged_docx = os.path.join(staging_dir, "UWE_War_on_the_Rocks_Essay.docx")
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
    staged_pdf = os.path.join(staging_dir, "UWE_War_on_the_Rocks_Essay.pdf")
    shutil.copy2(staged_pdf, pdf_file)

    print("Conversion completed successfully!")
    print(f"DOCX: {docx_file}")
    print(f"PDF:  {pdf_file}")

if __name__ == "__main__":
    convert()
