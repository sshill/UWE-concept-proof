#!/usr/bin/env python3
"""
convert_air_space.py

Compiles UWE_Air_Space_Forces_Feature.md into:
1. UWE_Air_Space_Forces_Feature.html
2. UWE_Air_Space_Forces_Feature.odt
3. UWE_Air_Space_Forces_Feature.docx
4. UWE_Air_Space_Forces_Feature.pdf

Extracts strictly PART 2 (The Feature Manuscript) for editorial submission to
Air & Space Forces Magazine (Air & Space Forces Association).
"""

import os
import re
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

    # Step 2: Strip \text{...}
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
    # Protect code spans
    code_tokens = []
    def save_code(m):
        code_tokens.append(m.group(1))
        return f"{{{{CODETOKEN:{len(code_tokens)-1}}}}}"
    text = re.sub(r'`([^`]+)`', save_code, text)

    # Protect markdown links
    link_tokens = []
    def save_link(m):
        label, url = m.group(1), m.group(2)
        link_tokens.append((label, url))
        return f"{{{{LINKTOKEN:{len(link_tokens)-1}}}}}"
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', save_link, text)

    # Parse inline math ($...$)
    def repl_inline_math(m):
        math_content = m.group(1)
        if not math_content.strip():
            return "$$"
        return parse_math_to_html(math_content)
    text = re.sub(r'\$([^\$]+)\$', repl_inline_math, text)

    # Bold and Italic
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', text)
    text = re.sub(r'___([^_]+)___', r'<b><i>\1</i></b>', text)
    text = re.sub(r'__([^_]+)__', r'<b>\1</b>', text)
    text = re.sub(r'_([^_]+)_', r'<i>\1</i>', text)

    # Restore links
    for idx, (label, url) in enumerate(link_tokens):
        formatted_label = inline_formatting(label)
        text = text.replace(f"{{{{LINKTOKEN:{idx}}}}}", f'<a href="{url}" style="color: #0b4f8a; text-decoration: underline;">{formatted_label}</a>')

    # Restore code spans
    for idx, code in enumerate(code_tokens):
        escaped_code = html.escape(code)
        text = text.replace(f"{{{{CODETOKEN:{idx}}}}}", f'<code style="font-family: Consolas, monospace; background: #eef3f8; padding: 1.5pt 4pt; border-radius: 3pt; font-size: 9.5pt; color: #0b2545;">{escaped_code}</code>')

    return text

def md_to_html(md_content, title="Air & Space Forces Magazine Feature"):
    lines = md_content.splitlines()
    html_lines = []
    
    in_list = False
    list_type = None
    in_table = False
    table_rows = []

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            if list_type == "ul":
                html_lines.append("</ul>")
            elif list_type == "ol":
                html_lines.append("</ol>")
            in_list = False
            list_type = None

    def close_table():
        nonlocal in_table, table_rows
        if in_table:
            html_lines.append('<table style="width: 100%; border-collapse: collapse; margin: 12pt 0; font-size: 10pt;">')
            for r_idx, row in enumerate(table_rows):
                html_lines.append('  <tr>')
                cells = [c.strip() for c in row.split('|')[1:-1]]
                for c in cells:
                    tag = "th" if r_idx == 0 else "td"
                    style = "border: 1px solid #cbd5e1; padding: 6pt 8pt; text-align: left;"
                    if r_idx == 0:
                        style += " background-color: #0b2545; color: #ffffff; font-weight: bold;"
                    else:
                        style += " background-color: #f8fafc;" if r_idx % 2 == 1 else " background-color: #ffffff;"
                    formatted_cell = inline_formatting(c)
                    html_lines.append(f'    <{tag} style="{style}">{formatted_cell}</{tag}>')
                html_lines.append('  </tr>')
            html_lines.append('</table>')
            in_table = False
            table_rows = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Empty line
        if not stripped:
            close_list()
            close_table()
            i += 1
            continue

        # Horizontal Rule
        if re.match(r'^(?:---|\*\*\*|___)$', stripped):
            close_list()
            close_table()
            html_lines.append('<hr style="border: none; border-top: 1.5px solid #cbd5e1; margin: 16pt 0;" />')
            i += 1
            continue

        # Images
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)', stripped)
        if img_match:
            close_list()
            close_table()
            alt = img_match.group(1)
            src = img_match.group(2)
            caption = alt if alt else ""
            html_lines.append(f'''
<div style="text-align: center; margin: 16pt 0; page-break-inside: avoid;">
  <img src="{src}" alt="{caption}" style="max-width: 100%; height: auto; border: 1px solid #cbd5e1; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.08);" />
  <div style="font-size: 9pt; color: #475569; font-style: italic; margin-top: 6pt; font-family: 'Georgia', serif;">{caption}</div>
</div>''')
            i += 1
            continue

        # Display Math ($$...$$)
        if stripped.startswith("$$"):
            close_list()
            close_table()
            math_block = [stripped]
            if not stripped.endswith("$$") or stripped == "$$":
                i += 1
                while i < len(lines) and not lines[i].strip().endswith("$$"):
                    math_block.append(lines[i])
                    i += 1
                if i < len(lines):
                    math_block.append(lines[i])
            full_math = "\n".join(math_block)
            rendered_math = parse_math_to_html(full_math)
            html_lines.append(f'<div style="text-align: center; margin: 12pt 0; font-family: \'Georgia\', serif; font-size: 11pt; font-weight: bold; color: #0b2545; page-break-inside: avoid;">{rendered_math}</div>')
            i += 1
            continue

        # Headings
        h1_match = re.match(r'^#\s+(.+)$', stripped)
        if h1_match:
            close_list()
            close_table()
            text = inline_formatting(h1_match.group(1))
            html_lines.append(f'<h1 style="font-family: \'Georgia\', serif; font-size: 21pt; color: #0b2545; border-bottom: 2px solid #0b2545; padding-bottom: 6pt; margin-top: 20pt; margin-bottom: 12pt; line-height: 1.25;">{text}</h1>')
            i += 1
            continue

        h2_match = re.match(r'^##\s+(.+)$', stripped)
        if h2_match:
            close_list()
            close_table()
            text = inline_formatting(h2_match.group(1))
            html_lines.append(f'<h2 style="font-family: \'Georgia\', serif; font-size: 16pt; color: #154273; margin-top: 18pt; margin-bottom: 10pt; border-bottom: 1px solid #cbd5e1; padding-bottom: 4pt; line-height: 1.3;">{text}</h2>')
            i += 1
            continue

        h3_match = re.match(r'^###\s+(.+)$', stripped)
        if h3_match:
            close_list()
            close_table()
            text = inline_formatting(h3_match.group(1))
            html_lines.append(f'<h3 style="font-family: \'Georgia\', serif; font-size: 13.5pt; color: #0b2545; margin-top: 14pt; margin-bottom: 8pt; line-height: 1.3;">{text}</h3>')
            i += 1
            continue

        h4_match = re.match(r'^####\s+(.+)$', stripped)
        if h4_match:
            close_list()
            close_table()
            text = inline_formatting(h4_match.group(1))
            html_lines.append(f'<h4 style="font-family: \'Georgia\', serif; font-size: 11.5pt; color: #1e3a8a; margin-top: 12pt; margin-bottom: 6pt; font-weight: bold;">{text}</h4>')
            i += 1
            continue

        # Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                close_list()
                in_table = True
                table_rows = []
            if not re.match(r'^\|(?:\s*:?-+:?\s*\|)+$', stripped):
                table_rows.append(stripped)
            i += 1
            continue
        else:
            close_table()

        # Lists (ul / ol)
        ul_match = re.match(r'^[*\-]\s+(.+)$', stripped)
        ol_match = re.match(r'^\d+\.\s+(.+)$', stripped)
        if ul_match or ol_match:
            close_table()
            target_type = "ul" if ul_match else "ol"
            item_text = ul_match.group(1) if ul_match else ol_match.group(1)
            if not in_list or list_type != target_type:
                close_list()
                in_list = True
                list_type = target_type
                html_lines.append(f'<{list_type} style="margin: 6pt 0 10pt 20pt; padding: 0;">')
            formatted_item = inline_formatting(item_text)
            html_lines.append(f'  <li style="margin-bottom: 4.5pt; line-height: 1.5; font-size: 10.5pt; color: #1e293b;">{formatted_item}</li>')
            i += 1
            continue
        else:
            close_list()

        # Regular Paragraph
        formatted_p = inline_formatting(stripped)
        html_lines.append(f'<p style="margin: 0 0 9pt 0; text-align: justify; line-height: 1.55; font-size: 10.5pt; color: #0f172a;">{formatted_p}</p>')
        i += 1

    close_list()
    close_table()

    body_html = "\n".join(html_lines)

    complete_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{html.escape(title)}</title>
  <style>
    @page {{
      size: A4;
      margin: 20mm 18mm 20mm 18mm;
      @bottom-right {{
        content: counter(page);
        font-family: 'Georgia', serif;
        font-size: 9pt;
        color: #64748b;
      }}
    }}
    body {{
      font-family: 'Georgia', 'Times New Roman', serif;
      font-size: 10.5pt;
      color: #0f172a;
      line-height: 1.55;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }}
    a {{ color: #0b4f8a; text-decoration: underline; }}
    h1, h2, h3, h4 {{ font-family: 'Georgia', serif; }}
    table {{ page-break-inside: avoid; }}
  </style>
</head>
<body>
<div style="max-width: 800px; margin: 0 auto; padding: 10px;">
  <div style="border-bottom: 2px solid #0b2545; padding-bottom: 8pt; margin-bottom: 14pt;">
    <div style="font-family: 'Arial', sans-serif; font-size: 8.5pt; font-weight: bold; text-transform: uppercase; letter-spacing: 1.5px; color: #154273;">
      AIR &amp; SPACE FORCES MAGAZINE • STRATEGIC FEATURE SUBMISSION
    </div>
    <div style="font-family: 'Arial', sans-serif; font-size: 8pt; color: #64748b; margin-top: 2pt;">
      AIR &amp; SPACE FORCES ASSOCIATION (AFA) • OFFICIAL DEFENSE JOURNAL
    </div>
  </div>
{body_html}
</div>
</body>
</html>"""
    return complete_doc


def embed_images_in_docx(docx_path):
    import zipfile, re, os, shutil
    backup_path = docx_path + '.bak'
    shutil.copy2(docx_path, backup_path)
    zin = zipfile.ZipFile(backup_path, 'r')
    zout = zipfile.ZipFile(docx_path, 'w', compression=zipfile.ZIP_DEFLATED)
    rels_content = zin.read('word/_rels/document.xml.rels').decode('utf-8')
    img_map = {}
    count = 1
    for m in re.finditer(r'<Relationship Id="([^"]+)" Type="[^"]*relationships/image" Target="file://([^"]+)" TargetMode="External"/>', rels_content):
        r_id = m.group(1)
        file_path = m.group(2)
        media_name = f'media/image{count}.png'
        img_map[r_id] = (file_path, media_name)
        count += 1
    new_rels = rels_content
    for r_id, (file_path, media_name) in img_map.items():
        old_tag = f'<Relationship Id="{r_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="file://{file_path}" TargetMode="External"/>'
        new_tag = f'<Relationship Id="{r_id}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{media_name}"/>'
        new_rels = new_rels.replace(old_tag, new_tag)
    for item in zin.infolist():
        if item.filename == 'word/_rels/document.xml.rels':
            zout.writestr(item, new_rels.encode('utf-8'))
        else:
            zout.writestr(item, zin.read(item.filename))
    for r_id, (file_path, media_name) in img_map.items():
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                zout.writestr(f'word/{media_name}', f.read())
            print(f'Embedded {file_path} as word/{media_name}')
    zin.close()
    zout.close()
    os.remove(backup_path)

def convert():
    base_dir = "/home/hills/Documents/UWS"
    md_file = os.path.join(base_dir, "UWE_Air_Space_Forces_Feature.md")
    html_file = os.path.join(base_dir, "UWE_Air_Space_Forces_Feature.html")
    odt_file = os.path.join(base_dir, "UWE_Air_Space_Forces_Feature.odt")
    docx_file = os.path.join(base_dir, "UWE_Air_Space_Forces_Feature.docx")
    pdf_file = os.path.join(base_dir, "UWE_Air_Space_Forces_Feature.pdf")

    print(f"Reading {md_file}...")
    with open(md_file, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Extract strictly Part 2
    part2_marker = "## PART 2: THE FEATURE MANUSCRIPT"
    if part2_marker in full_content:
        manuscript_md = full_content.split(part2_marker)[1].strip()
        print("Extracted Part 2 (The Feature Manuscript) exclusively.")
    else:
        manuscript_md = full_content
        print("Marker not found, using full content.")

    html_doc = md_to_html(manuscript_md, title="De-Centering the Pilot - Air & Space Forces Magazine Feature")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_doc)
    print(f"Wrote HTML: {html_file}")

    # Isolated staging directory for LibreOffice
    staging_dir = "/tmp/lo_staging_asf"
    if os.path.exists(staging_dir):
        shutil.rmtree(staging_dir)
    os.makedirs(staging_dir, exist_ok=True)

    lo_user_dir = f"file://{base_dir}/.lo_user"

    # Step 1: HTML to ODT
    print("Converting HTML to ODT...")
    cmd1 = [
        "libreoffice",
        f"-env:UserInstallation={lo_user_dir}",
        "--headless",
        "--convert-to", "odt:writerweb8_writer",
        html_file,
        "--outdir", staging_dir
    ]
    subprocess.run(cmd1, check=True)
    staged_odt = os.path.join(staging_dir, "UWE_Air_Space_Forces_Feature.odt")
    shutil.copy2(staged_odt, odt_file)

    # Step 2: ODT to DOCX
    print("Converting ODT to DOCX...")
    cmd2 = [
        "libreoffice",
        f"-env:UserInstallation={lo_user_dir}",
        "--headless",
        "--convert-to", "docx:MS Word 2007 XML",
        staged_odt,
        "--outdir", staging_dir
    ]
    subprocess.run(cmd2, check=True)
    staged_docx = os.path.join(staging_dir, "UWE_Air_Space_Forces_Feature.docx")
    shutil.copy2(staged_docx, docx_file)
    embed_images_in_docx(docx_file)

    # Step 3: ODT to PDF
    print("Converting ODT to PDF...")
    cmd3 = [
        "libreoffice",
        f"-env:UserInstallation={lo_user_dir}",
        "--headless",
        "--convert-to", "pdf:writer_pdf_Export",
        staged_odt,
        "--outdir", staging_dir
    ]
    subprocess.run(cmd3, check=True)
    staged_pdf = os.path.join(staging_dir, "UWE_Air_Space_Forces_Feature.pdf")
    shutil.copy2(staged_pdf, pdf_file)

    print("Conversion completed successfully!")
    print(f"DOCX: {docx_file}")
    print(f"PDF:  {pdf_file}")

if __name__ == "__main__":
    convert()
