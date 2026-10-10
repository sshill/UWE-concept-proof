#!/usr/bin/env python3
"""
convert_rusi.py

Compiles UWE_RUSI_Defence_Systems_Monograph.md into publication-grade submission formats:
1. UWE_RUSI_Defence_Systems_Monograph.html
2. UWE_RUSI_Defence_Systems_Monograph.odt
3. UWE_RUSI_Defence_Systems_Monograph.docx
4. UWE_RUSI_Defence_Systems_Monograph.pdf

Prepared for submission to Royal United Services Institute (RUSI Defence Systems / Commentary), Whitehall, London.
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

    s = re.sub(r"\\left\s*([(\[{|])", r"\1", s)
    s = re.sub(r"\\right\s*([)\]}|])", r"\1", s)
    s = re.sub(r"\\left\b", "", s)
    s = re.sub(r"\\right\b", "", s)
    s = re.sub(r"\\text\{\s*([^}]+)\s*\}", r"\1", s)
    s = re.sub(r"\\mathbf\{\s*([^}]+)\s*\}", r"<strong>\1</strong>", s)
    s = re.sub(r"\\frac\{\s*([^}]+)\s*\}\{\s*([^}]+)\s*\}", r"(\1 / \2)", s)
    s = re.sub(r"\^\{([^}]+)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", s)
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
    s = s.replace("\\", "")
    return s

def inline_formatting(text):
    code_tokens = []
    def save_code(m):
        code_tokens.append(m.group(1))
        return f"{{{{CODETOKEN:{len(code_tokens)-1}}}}}"
    text = re.sub(r'`([^`]+)`', save_code, text)

    link_tokens = []
    def save_link(m):
        label, url = m.group(1), m.group(2)
        link_tokens.append((label, url))
        return f"{{{{LINKTOKEN:{len(link_tokens)-1}}}}}"
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', save_link, text)

    def repl_inline_math(m):
        math_content = m.group(1)
        if not math_content.strip():
            return "$$"
        return parse_math_to_html(math_content)
    text = re.sub(r'\$([^\$]+)\$', repl_inline_math, text)

    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)

    for idx, (label, url) in enumerate(link_tokens):
        text = text.replace(f"{{{{LINKTOKEN:{idx}}}}}", f'<a href="{url}" style="color: #0284c7; text-decoration: underline;">{label}</a>')

    for idx, code in enumerate(code_tokens):
        escaped_code = html.escape(code)
        text = text.replace(f"{{{{CODETOKEN:{idx}}}}}", f'<code style="font-family: Consolas, monospace; background: #f1f5f9; padding: 1.5pt 4pt; border-radius: 3pt; font-size: 9.5pt; color: #0f172a;">{escaped_code}</code>')

    return text

def md_to_html(md_content, title="RUSI Defence Systems Monograph"):
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
            html_lines.append('<table style="width: 100%; border-collapse: collapse; margin: 12pt 0; font-size: 10pt; border: 1px solid #cbd5e1;">')
            for r_idx, row in enumerate(table_rows):
                html_lines.append("<tr>")
                for c_idx, cell in enumerate(row):
                    tag = "th" if r_idx == 0 else "td"
                    bg = 'background-color: #f8fafc;' if r_idx == 0 else ('background-color: #f1f5f9;' if r_idx % 2 == 1 else '')
                    weight = 'font-weight: 700;' if r_idx == 0 else 'font-weight: 400;'
                    cell_html = inline_formatting(cell.strip())
                    html_lines.append(f'<{tag} style="border: 1px solid #cbd5e1; padding: 6pt 10pt; text-align: left; {bg} {weight}">{cell_html}</{tag}>')
                html_lines.append("</tr>")
            html_lines.append("</table>")
            in_table = False
            table_rows = []

    in_blockquote = False
    def close_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            html_lines.append("</blockquote>")
            in_blockquote = False

    i = 0
    n = len(lines)
    while i < n:
        raw_line = lines[i]
        stripped = raw_line.strip()

        # Fenced code block or ASCII diagram
        if stripped.startswith("```"):
            close_list()
            close_table()
            close_blockquote()
            code_block = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_block.append(lines[i])
                i += 1
            i += 1
            code_str = html.escape("\n".join(code_block))
            html_lines.append(f'<pre style="background: #0f172a; color: #f8fafc; padding: 12pt 16pt; border-radius: 6pt; font-family: Consolas, monospace; font-size: 8.5pt; line-height: 1.35; overflow-x: auto; border: 1px solid #334155;">{code_str}</pre>')
            continue

        # Blank line
        if not stripped:
            close_list()
            close_table()
            close_blockquote()
            i += 1
            continue

        # Horizontal Rule
        if re.match(r'^(\*{3,}|-{3,}|_{3,})$', stripped):
            close_list()
            close_table()
            close_blockquote()
            html_lines.append('<hr style="border: 0; height: 1.5pt; background: #cbd5e1; margin: 18pt 0;" />')
            i += 1
            continue

        # Blockquote
        if stripped.startswith(">"):
            close_list()
            close_table()
            if not in_blockquote:
                html_lines.append('<blockquote style="margin: 12pt 0; padding: 8pt 16pt; border-left: 4pt solid #0284c7; background: #f0f9ff; color: #0c4a6e; font-style: italic;">')
                in_blockquote = True
            bq_text = inline_formatting(stripped.lstrip("> ").strip())
            html_lines.append(f'<p style="margin: 4pt 0;">{bq_text}</p>')
            i += 1
            continue
        else:
            close_blockquote()

        # Headings
        if stripped.startswith("#"):
            close_list()
            close_table()
            h_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
            if h_match:
                level = len(h_match.group(1))
                h_text = inline_formatting(h_match.group(2))
                sizes = {1: "24pt", 2: "18pt", 3: "14pt", 4: "12pt", 5: "11pt", 6: "10pt"}
                margins = {1: "24pt 0 10pt", 2: "20pt 0 8pt", 3: "16pt 0 6pt", 4: "12pt 0 4pt"}
                color = "#0f172a" if level <= 2 else "#1e293b"
                html_lines.append(f'<h{level} style="font-size: {sizes.get(level, "11pt")}; margin: {margins.get(level, "10pt 0")}; font-weight: 800; color: {color}; line-height: 1.25;">{h_text}</h{level}>')
                i += 1
                continue

        # Image ![alt](url)
        img_match = re.match(r'^!\[([^\]]*)\]\(([^)]+)\)$', stripped)
        if img_match:
            close_list()
            close_table()
            alt, src = img_match.group(1), img_match.group(2)
            html_lines.append(f'<div style="text-align: center; margin: 18pt 0;">')
            html_lines.append(f'<img src="{src}" alt="{alt}" style="max-width: 100%; height: auto; border: 1px solid #cbd5e1; border-radius: 6pt; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />')
            if alt:
                html_lines.append(f'<p style="font-size: 9.5pt; color: #64748b; font-style: italic; margin-top: 6pt;">{alt}</p>')
            html_lines.append('</div>')
            i += 1
            continue

        # Table rows
        if stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            cells = [c for c in stripped.strip("|").split("|")]
            if re.match(r'^[\s\-:|]+$', stripped):
                i += 1
                continue
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
            i += 1
            continue
        else:
            close_table()

        # Unordered list
        ul_match = re.match(r'^[-*+]\s+(.*)$', stripped)
        if ul_match:
            if not in_list or list_type != "ul":
                close_list()
                in_list = True
                list_type = "ul"
                html_lines.append('<ul style="margin: 8pt 0 8pt 20pt; padding: 0; line-height: 1.6;">')
            li_text = inline_formatting(ul_match.group(1))
            html_lines.append(f'<li style="margin: 3pt 0; color: #1e293b;">{li_text}</li>')
            i += 1
            continue

        # Ordered list
        ol_match = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if ol_match:
            if not in_list or list_type != "ol":
                close_list()
                in_list = True
                list_type = "ol"
                html_lines.append('<ol style="margin: 8pt 0 8pt 20pt; padding: 0; line-height: 1.6;">')
            li_text = inline_formatting(ol_match.group(2))
            html_lines.append(f'<li style="margin: 3pt 0; color: #1e293b;">{li_text}</li>')
            i += 1
            continue

        # Regular Paragraph
        close_list()
        close_table()
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
    size: a4 portrait;
    margin: 20mm;
    @bottom-center {{
      content: counter(page);
      font-size: 9pt;
      font-family: 'Georgia', serif;
      color: #64748b;
    }}
  }}
  body {{
    font-family: 'Georgia', 'Times New Roman', serif;
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
    target_img = os.path.join(base_dir, "rusi_uk_maritime_cui_architecture_fitted.png")

    for item in zin.infolist():
        if item.filename.startswith('word/media/'):
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
    md_file = os.path.join(base_dir, "UWE_RUSI_Defence_Systems_Monograph.md")
    html_file = os.path.join(base_dir, "UWE_RUSI_Defence_Systems_Monograph.html")
    odt_file = os.path.join(base_dir, "UWE_RUSI_Defence_Systems_Monograph.odt")
    docx_file = os.path.join(base_dir, "UWE_RUSI_Defence_Systems_Monograph.docx")
    pdf_file = os.path.join(base_dir, "UWE_RUSI_Defence_Systems_Monograph.pdf")

    print(f"Reading markdown: {md_file}")
    with open(md_file, "r", encoding="utf-8") as f:
        full_content = f.read()

    print("Generating formatted HTML...")
    html_content = md_to_html(full_content, title="RUSI Defence Systems: The Software-Defined Escort")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved HTML: {html_file}")

    staging_dir = os.path.join(base_dir, ".lo_staging_rusi")
    os.makedirs(staging_dir, exist_ok=True)
    lo_profile = f"-env:UserInstallation=file://{os.path.join(base_dir, '.lo_user_rusi')}"

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
    staged_odt = os.path.join(staging_dir, "UWE_RUSI_Defence_Systems_Monograph.odt")
    shutil.copy2(staged_odt, odt_file)
    print(f"Saved ODT: {odt_file}")

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
    staged_docx = os.path.join(staging_dir, "UWE_RUSI_Defence_Systems_Monograph.docx")
    shutil.copy2(staged_docx, docx_file)
    embed_images_in_docx(docx_file)
    print(f"Saved DOCX: {docx_file}")

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
    staged_pdf = os.path.join(staging_dir, "UWE_RUSI_Defence_Systems_Monograph.pdf")
    shutil.copy2(staged_pdf, pdf_file)
    print(f"Saved PDF: {pdf_file}")

    print("\n========================================================")
    print("SUCCESS: RUSI Defence Systems Submission Package Compiled!")
    print(f"HTML: {html_file}")
    print(f"ODT:  {odt_file}")
    print(f"DOCX: {docx_file}")
    print(f"PDF:  {pdf_file}")
    print("========================================================")

if __name__ == "__main__":
    convert()
