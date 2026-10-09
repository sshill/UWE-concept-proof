#!/usr/bin/env python3
"""
convert_mwi.py

Compiles UWE_MWI_West_Point_Essay.md into:
1. UWE_MWI_West_Point_Essay.html
2. UWE_MWI_West_Point_Essay.odt
3. UWE_MWI_West_Point_Essay.docx
4. UWE_MWI_West_Point_Essay.pdf

Extracts strictly PART 2 (The Analytical Manuscript) for editorial submission to
Modern War Institute at West Point (United States Military Academy).
"""

import os
import re
import html
import subprocess
import shutil
import zipfile

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

    # Step 3: Handle \mathbf{...}
    s = re.sub(r"\\mathbf\{\s*([^}]+)\s*\}", r"<strong>\1</strong>", s)

    # Step 4: Handle fractions \frac{a}{b} -> (a / b)
    s = re.sub(r"\\frac\{\s*([^}]+)\s*\}\{\s*([^}]+)\s*\}", r"(\1 / \2)", s)

    # Step 5: Handle superscripts and subscripts
    s = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"\^([a-zA-Z0-9\+\-]+)", r"<sup>\1</sup>", s)
    s = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", s)
    s = re.sub(r"_([a-zA-Z0-9\+\-]+)", r"<sub>\1</sub>", s)

    # Step 6: Symbols
    s = s.replace(r"\cdot", "·")
    s = s.replace(r"\times", "×")
    s = s.replace(r"\approx", "≈")
    s = s.replace(r"\propto", "∝")
    s = s.replace(r"\le", "≤")
    s = s.replace(r"\ge", "≥")
    s = s.replace(r"\pm", "±")
    s = s.replace(r"\circ", "°")
    s = s.replace(r"\Delta", "Δ")
    s = s.replace(r"\leftrightarrow", "↔")
    s = s.replace(r"\rightarrow", "→")

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
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

    # Restore markdown links
    for idx, (label, url) in enumerate(link_tokens):
        text = text.replace(f"{{{{LINKTOKEN:{idx}}}}}", f'<a href="{url}" style="color: #1e3a8a; text-decoration: underline;">{label}</a>')

    # Restore code spans
    for idx, code in enumerate(code_tokens):
        escaped_code = html.escape(code)
        text = text.replace(f"{{{{CODETOKEN:{idx}}}}}", f'<code style="font-family: Consolas, monospace; background: #eef3f8; padding: 1.5pt 4pt; border-radius: 3pt; font-size: 9.5pt; color: #0b2545;">{escaped_code}</code>')

    return text

def md_to_html(md_content, title="Modern War Institute Analysis"):
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
                for c_idx, cell in enumerate(row):
                    tag = "th" if r_idx == 0 else "td"
                    bg = ' background-color: #f1f5f9; font-weight: bold; color: #0f172a;' if r_idx == 0 else (' background-color: #f8fafc;' if r_idx % 2 == 1 else ' background-color: #ffffff;')
                    cell_html = inline_formatting(cell.strip())
                    html_lines.append(f'    <{tag} style="border: 1px solid #cbd5e1; padding: 6pt 8pt; text-align: left;{bg}">{cell_html}</{tag}>')
                html_lines.append('  </tr>')
            html_lines.append('</table>')
            in_table = False
            table_rows = []

    in_blockquote = False
    def close_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            html_lines.append("</blockquote>")
            in_blockquote = False

    in_pre = False
    pre_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Fenced code block (ASCII diagram or code)
        if line.strip().startswith("```"):
            if not in_pre:
                close_list()
                close_table()
                close_blockquote()
                in_pre = True
                pre_lines = []
            else:
                in_pre = False
                escaped_pre = "\n".join(html.escape(l) for l in pre_lines)
                html_lines.append(f'<pre style="background: #0f172a; color: #e2e8f0; padding: 10pt 14pt; border-radius: 6pt; font-family: Consolas, monospace; font-size: 8.5pt; line-height: 1.35; overflow-x: auto; margin: 12pt 0; border: 1px solid #1e293b;">{escaped_pre}</pre>')
            i += 1
            continue

        if in_pre:
            pre_lines.append(line)
            i += 1
            continue

        stripped = line.strip()

        # Display math $$ ... $$
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 2:
            close_list()
            close_table()
            close_blockquote()
            math_html = parse_math_to_html(stripped)
            html_lines.append(f'<div style="text-align: center; margin: 14pt 0; font-family: Georgia, serif; font-size: 11pt; color: #0f172a; background: #f8fafc; padding: 8pt; border-radius: 4pt; border: 1px solid #e2e8f0;">{math_html}</div>')
            i += 1
            continue

        # Horizontal Rule
        if re.match(r'^(\*\*\*|---|___)$', stripped):
            close_list()
            close_table()
            close_blockquote()
            html_lines.append('<hr style="border: none; border-top: 1.5px solid #cbd5e1; margin: 20pt 0;" />')
            i += 1
            continue

        # Table rows
        if stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            close_blockquote()
            # Check if divider line
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                i += 1
                continue
            cells = [c for c in stripped.split("|")[1:-1]]
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
            i += 1
            continue
        else:
            close_table()

        # Blockquote
        if stripped.startswith(">"):
            close_list()
            quote_text = stripped[1:].strip()
            if not in_blockquote:
                html_lines.append('<blockquote style="border-left: 3.5px solid #0284c7; padding-left: 14pt; margin: 12pt 0; color: #334155; font-style: italic; background: #f0f9ff; padding: 8pt 14pt; border-radius: 0 4pt 4pt 0;">')
                in_blockquote = True
            html_lines.append(f'<p style="margin: 4pt 0;">{inline_formatting(quote_text)}</p>')
            i += 1
            continue
        else:
            close_blockquote()

        # Headings
        h_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if h_match:
            close_list()
            level = len(h_match.group(1))
            h_text = inline_formatting(h_match.group(2))
            if level == 1:
                html_lines.append(f'<h1 style="font-size: 22pt; font-weight: 800; color: #0f172a; margin-top: 24pt; margin-bottom: 12pt; line-height: 1.25; border-bottom: 2px solid #0284c7; padding-bottom: 6pt;">{h_text}</h1>')
            elif level == 2:
                html_lines.append(f'<h2 style="font-size: 16pt; font-weight: 700; color: #1e3a8a; margin-top: 20pt; margin-bottom: 10pt; line-height: 1.3;">{h_text}</h2>')
            elif level == 3:
                html_lines.append(f'<h3 style="font-size: 13pt; font-weight: 700; color: #0369a1; margin-top: 16pt; margin-bottom: 8pt; line-height: 1.35;">{h_text}</h3>')
            elif level == 4:
                html_lines.append(f'<h4 style="font-size: 11pt; font-weight: 700; color: #334155; margin-top: 12pt; margin-bottom: 6pt;">{h_text}</h4>')
            else:
                html_lines.append(f'<h5 style="font-size: 10pt; font-weight: 700; color: #475569; margin-top: 10pt; margin-bottom: 4pt;">{h_text}</h5>')
            i += 1
            continue

        # Unordered List Items
        ul_match = re.match(r'^[\*\-]\s+(.*)$', stripped)
        if ul_match:
            item_text = inline_formatting(ul_match.group(1))
            if not in_list or list_type != "ul":
                close_list()
                html_lines.append('<ul style="margin: 8pt 0 8pt 20pt; padding-left: 0; line-height: 1.55;">')
                in_list = True
                list_type = "ul"
            html_lines.append(f'<li style="margin-bottom: 4pt; color: #1e293b;">{item_text}</li>')
            i += 1
            continue

        # Ordered List Items
        ol_match = re.match(r'^\d+\.\s+(.*)$', stripped)
        if ol_match:
            item_text = inline_formatting(ol_match.group(1))
            if not in_list or list_type != "ol":
                close_list()
                html_lines.append('<ol style="margin: 8pt 0 8pt 20pt; padding-left: 0; line-height: 1.55;">')
                in_list = True
                list_type = "ol"
            html_lines.append(f'<li style="margin-bottom: 4pt; color: #1e293b;">{item_text}</li>')
            i += 1
            continue

        # Empty lines
        if not stripped:
            close_list()
            i += 1
            continue

        # Images: ![alt](url)
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', stripped)
        if img_match:
            close_list()
            alt_text = img_match.group(1)
            img_src = img_match.group(2)
            html_lines.append(f'<div style="text-align: center; margin: 18pt 0;">')
            html_lines.append(f'  <img src="{img_src}" alt="{alt_text}" style="max-width: 100%; height: auto; border-radius: 6pt; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 1px solid #cbd5e1;" />')
            html_lines.append(f'</div>')
            i += 1
            continue

        # Image Caption: *Figure X: ...*
        if stripped.startswith("*Figure") and stripped.endswith("*"):
            caption_text = inline_formatting(stripped[1:-1])
            html_lines.append(f'<p style="text-align: center; font-size: 9.5pt; color: #64748b; font-style: italic; margin-top: -10pt; margin-bottom: 16pt;">{caption_text}</p>')
            i += 1
            continue

        # Regular Paragraph
        close_list()
        p_text = inline_formatting(stripped)
        html_lines.append(f'<p style="margin: 8pt 0; line-height: 1.6; text-align: justify; color: #1e293b; font-size: 10.5pt;">{p_text}</p>')
        i += 1

    close_list()
    close_table()
    close_blockquote()

    body_html = "\n".join(html_lines)

    complete_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
  @page {{
    size: letter portrait;
    margin: 1in;
    @bottom-center {{
      content: counter(page);
      font-size: 9pt;
      font-family: 'Times New Roman', Times, serif;
      color: #64748b;
    }}
  }}
  body {{
    font-family: 'Times New Roman', Times, Georgia, serif;
    color: #0f172a;
    background-color: #ffffff;
    line-height: 1.6;
    margin: 0;
    padding: 0;
  }}
  h1, h2, h3, h4, h5 {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  }}
  table, tr, td, th {{
    page-break-inside: avoid;
  }}
  img {{
    page-break-inside: avoid;
  }}
  pre, code {{
    font-family: Consolas, 'Courier New', monospace;
  }}
</style>
</head>
<body>
{body_html}
</body>
</html>"""
    return complete_doc

def embed_images_in_docx(docx_path):
    backup_path = docx_path + '.bak'
    shutil.copy2(docx_path, backup_path)
    zin = zipfile.ZipFile(backup_path, 'r')
    zout = zipfile.ZipFile(docx_path, 'w', compression=zipfile.ZIP_DEFLATED)
    
    base_dir = os.path.dirname(docx_path)
    target_img = os.path.join(base_dir, "mwi_ugv_ground_kill_zone_fitted.png")

    for item in zin.infolist():
        if item.filename.startswith('word/media/'):
            # Replace LibreOffice placeholder with high-res PNG
            if os.path.exists(target_img):
                with open(target_img, 'rb') as f_img:
                    data = f_img.read()
                zout.writestr(item, data)
                print(f"Replaced {item.filename} with high-res {os.path.basename(target_img)}")
            else:
                zout.writestr(item, zin.read(item.filename))
        else:
            zout.writestr(item, zin.read(item.filename))
            
    zin.close()
    zout.close()
    if os.path.exists(backup_path):
        os.remove(backup_path)

def convert():
    base_dir = "/home/hills/Documents/UWS"
    md_file = os.path.join(base_dir, "UWE_MWI_West_Point_Essay.md")
    html_file = os.path.join(base_dir, "UWE_MWI_West_Point_Essay.html")
    odt_file = os.path.join(base_dir, "UWE_MWI_West_Point_Essay.odt")
    docx_file = os.path.join(base_dir, "UWE_MWI_West_Point_Essay.docx")
    pdf_file = os.path.join(base_dir, "UWE_MWI_West_Point_Essay.pdf")

    print(f"Reading markdown: {md_file}")
    with open(md_file, "r", encoding="utf-8") as f:
        full_content = f.read()

    # Extract strictly PART 2 for the formal manuscript
    if "## PART 2: THE ANALYTICAL MANUSCRIPT" in full_content:
        part2 = full_content.split("## PART 2: THE ANALYTICAL MANUSCRIPT")[1].strip()
    else:
        part2 = full_content

    print("Generating formatted HTML...")
    html_content = md_to_html(part2, title="Modern War Institute at West Point: The Autonomous Trench")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved HTML: {html_file}")

    # Use clean isolated profile for LibreOffice conversions
    staging_dir = os.path.join(base_dir, ".lo_staging_mwi")
    os.makedirs(staging_dir, exist_ok=True)
    lo_profile = f"-env:UserInstallation=file://{os.path.join(base_dir, '.lo_user_mwi')}"

    # Step 1: HTML -> ODT
    print("Converting HTML to ODT via LibreOffice...")
    cmd1 = [
        "libreoffice",
        lo_profile,
        "--headless",
        "--convert-to", "odt:writer8",
        "--outdir", staging_dir,
        html_file
    ]
    subprocess.run(cmd1, check=True)
    staged_odt = os.path.join(staging_dir, "UWE_MWI_West_Point_Essay.odt")
    shutil.copy2(staged_odt, odt_file)

    # Step 2: ODT -> DOCX
    print("Converting ODT to DOCX via LibreOffice...")
    cmd2 = [
        "libreoffice",
        lo_profile,
        "--headless",
        "--convert-to", "docx:MS Word 2007 XML",
        "--outdir", staging_dir,
        staged_odt
    ]
    subprocess.run(cmd2, check=True)
    staged_docx = os.path.join(staging_dir, "UWE_MWI_West_Point_Essay.docx")
    shutil.copy2(staged_docx, docx_file)
    embed_images_in_docx(docx_file)

    # Step 3: ODT -> PDF
    print("Converting ODT to PDF via LibreOffice...")
    cmd3 = [
        "libreoffice",
        lo_profile,
        "--headless",
        "--convert-to", "pdf:writer_pdf_Export",
        "--outdir", staging_dir,
        staged_odt
    ]
    subprocess.run(cmd3, check=True)
    staged_pdf = os.path.join(staging_dir, "UWE_MWI_West_Point_Essay.pdf")
    shutil.copy2(staged_pdf, pdf_file)

    print("\n========================================================")
    print("SUCCESS: Modern War Institute Submission Package Compiled!")
    print(f"HTML: {html_file}")
    print(f"ODT:  {odt_file}")
    print(f"DOCX: {docx_file}")
    print(f"PDF:  {pdf_file}")
    print("========================================================")

if __name__ == "__main__":
    convert()
