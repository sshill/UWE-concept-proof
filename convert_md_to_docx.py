#!/usr/bin/env python3
import re
import sys
import os
import subprocess
import html

def clean_latex(text):
    # LaTeX symbol replacements
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
        (r'\\infty', '∞'),
        (r'\\Delta', 'Δ'),
        (r'\\Phi', 'Φ'),
        (r'\\rho', 'ρ'),
        (r'\\nu', 'ν'),
        (r'\\lambda', 'λ'),
        (r'\\theta', 'θ'),
        (r'\\mu', 'μ'),
        (r'\\pi', 'π'),
        (r'\\omega', 'ω'),
        (r'\\Omega', 'Ω'),
        (r'\\dots', '…'),
        (r'\\varnothing', '⌀'),
        (r'\\sim', '~'),
        (r'\\hat{\\mathbf{v}}', 'v̂'),
        (r'\\mathbf{([^}]+)}', r'<b>\1</b>'),
        (r'\\text{([^}]+)}', r'\1'),
        (r'\\sqrt{([^}]+)}', r'√(\1)'),
        (r'\\frac{([^}]+)}{([^}]+)}', r'(\1)/(\2)'),
        (r'\^2', '²'),
        (r'\^3', '³'),
        (r'\^T', 'ᵀ'),
        (r'\^{-15}', '⁻¹⁵'),
        (r'\^{-4}', '⁻⁴'),
        (r'\^{-3}', '⁻³'),
        (r'\\,', ' '),
        (r'\\;', ' '),
        (r'\\!', ''),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    
    # Strip $ signs from $math$
    text = re.sub(r'\$([^\$]+)\$', r'<em>\1</em>', text)
    return text

def inline_formatting(text):
    # Escape HTML special chars first except where we already have tags
    # We do a safe replacement of code blocks first
    code_tokens = []
    def save_code(m):
        code_tokens.append(m.group(1))
        return f"___CODE_TOKEN_{len(code_tokens)-1}___"
    
    text = re.sub(r'`([^`]+)`', save_code, text)
    
    # Clean latex before markdown bold/italic
    text = clean_latex(text)
    
    # Tokenize images and links first so URLs with underscores are not mangled
    img_tokens = []
    def save_img(m):
        alt = m.group(1)
        url = m.group(2)
        idx = len(img_tokens)
        img_tokens.append(f'<div style="text-align:center; margin:16px 0;"><img src="{url}" alt="{alt}" style="max-width:100%; height:auto;" /><br><small style="color:#666;">{alt}</small></div>')
        return f"QQQIMGTOKEN{idx}QQQ"
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', save_img, text)

    link_tokens = []
    def save_link(m):
        label = m.group(1)
        url = m.group(2)
        idx = len(link_tokens)
        link_tokens.append((label, url))
        return f"QQQLINKTOKEN{idx}QQQ"
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', save_link, text)

    # Bold & Italic
    text = re.sub(r'\*\*\*([^*]+)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', text)
    text = re.sub(r'___([^_]+)___', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'__([^_]+)__', r'<strong>\1</strong>', text)
    text = re.sub(r'_([^_]+)_', r'<em>\1</em>', text)
    
    # Restore links
    for i, (label, url) in enumerate(link_tokens):
        text = text.replace(f"QQQLINKTOKEN{i}QQQ", f'<a href="{url}">{label}</a>')

    # Restore images
    for i, img_html in enumerate(img_tokens):
        text = text.replace(f"QQQIMGTOKEN{i}QQQ", img_html)
        
    # Restore code
    for i, token in enumerate(code_tokens):
        escaped = html.escape(token)
        text = text.replace(f"___CODE_TOKEN_{i}___", f"<code>{escaped}</code>")
        
    return text

def md_to_html(md_text, title="Document"):
    lines = md_text.splitlines()
    html_lines = []
    
    html_lines.append(f'''<!DOCTYPE html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>
body{{font-family: Calibri, Arial, sans-serif; line-height: 1.5; font-size: 11pt; color: #111; max-width: 900px; margin: 0 auto; padding: 20px;}}
h1{{font-size: 20pt; color: #003366; margin-top: 24px; margin-bottom: 8px;}}
h2{{font-size: 16pt; color: #003366; border-bottom: 1px solid #ccc; padding-bottom: 4px; margin-top: 20px; margin-bottom: 8px;}}
h3{{font-size: 13pt; color: #222; margin-top: 16px; margin-bottom: 6px;}}
h4{{font-size: 11pt; color: #333; margin-top: 12px; margin-bottom: 4px; font-weight: bold;}}
h5{{font-size: 11pt; color: #444; margin-top: 10px; margin-bottom: 4px; font-weight: bold;}}
blockquote{{border-left: 4px solid #0066cc; margin: 10px 0; padding: 10px 15px; background: #f4f8fa; color: #333;}}
pre{{background: #f0f0f0; padding: 10px; border-radius: 4px; font-family: Consolas, monospace; font-size: 9.5pt; overflow-x: auto; white-space: pre-wrap; line-height: 1.2;}}
a{{color: #0066cc; text-decoration: underline;}}
hr{{border: 0; border-top: 1px solid #ddd; margin: 20px 0;}}
table{{border-collapse: collapse; width: 100%; margin: 15px 0;}}
th, td{{border: 1px solid #ccc; padding: 6px 10px; text-align: left; font-size: 10pt; vertical-align: top;}}
th{{background-color: #f2f5f8; color: #003366; font-weight: bold;}}
code{{font-family: Consolas, monospace; background: #f0f0f0; padding: 2px 4px; border-radius: 3px; font-size: 10pt;}}
ul{{margin: 8px 0 8px 20px; padding: 0;}}
ol{{margin: 8px 0 8px 20px; padding: 0;}}
li{{margin-bottom: 4px;}}
p{{margin: 8px 0;}}
</style></head><body>''')

    in_code = False
    code_content = []
    in_table = False
    table_rows = []
    in_ul = False
    in_ol = False
    ul_level = 0
    in_quote = False
    quote_lines = []

    def close_lists():
        nonlocal in_ul, in_ol, ul_level
        out = []
        if in_ul:
            while ul_level > 0:
                out.append("</ul>")
                ul_level -= 1
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False
        return out

    def close_quote():
        nonlocal in_quote, quote_lines
        if in_quote:
            res = "<blockquote>" + "<br>".join(quote_lines) + "</blockquote>"
            in_quote = False
            quote_lines = []
            return [res]
        return []

    def close_table():
        nonlocal in_table, table_rows
        out = []
        if in_table:
            out.append("<table>")
            for i, row in enumerate(table_rows):
                if i == 0:
                    out.append("<thead><tr>")
                    for cell in row:
                        out.append(f"<th>{inline_formatting(cell.strip())}</th>")
                    out.append("</tr></thead><tbody>")
                else:
                    out.append("<tr>")
                    for cell in row:
                        out.append(f"<td>{inline_formatting(cell.strip())}</td>")
                    out.append("</tr>")
            if len(table_rows) > 0:
                out.append("</tbody>")
            out.append("</table>")
            in_table = False
            table_rows = []
        return out

    for line in lines:
        raw_line = line
        stripped = line.strip()

        # Handle fenced code block
        if stripped.startswith("```") or stripped.startswith("~~~~"):
            if in_code:
                html_lines.extend(close_lists())
                escaped_code = html.escape("\n".join(code_content))
                html_lines.append(f"<pre><code>{escaped_code}</code></pre>")
                in_code = False
                code_content = []
            else:
                html_lines.extend(close_lists())
                html_lines.extend(close_quote())
                html_lines.extend(close_table())
                in_code = True
                code_content = []
            continue

        if in_code:
            code_content.append(raw_line)
            continue

        # Handle Blockquotes
        if stripped.startswith(">"):
            html_lines.extend(close_lists())
            html_lines.extend(close_table())
            in_quote = True
            q_text = stripped.lstrip("> ").strip()
            quote_lines.append(inline_formatting(q_text))
            continue
        elif in_quote:
            html_lines.extend(close_quote())

        # Handle Table rows
        if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2:
            html_lines.extend(close_lists())
            html_lines.extend(close_quote())
            # Check if separator row
            if re.match(r'^\|[\s\:\-\|]+\|$', stripped):
                # separator line
                continue
            cells = [c for c in stripped[1:-1].split("|")]
            if not in_table:
                in_table = True
                table_rows = [cells]
            else:
                table_rows.append(cells)
            continue
        elif in_table:
            html_lines.extend(close_table())

        # Blank line
        if not stripped:
            html_lines.extend(close_lists())
            html_lines.extend(close_quote())
            html_lines.extend(close_table())
            continue

        # Horizontal Rule
        if re.match(r'^(?:---|\*\*\*|___)\s*$', stripped):
            html_lines.extend(close_lists())
            html_lines.extend(close_quote())
            html_lines.extend(close_table())
            html_lines.append("<hr>")
            continue

        # Headers
        h_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if h_match:
            html_lines.extend(close_lists())
            html_lines.extend(close_quote())
            html_lines.extend(close_table())
            h_level = len(h_match.group(1))
            h_text = inline_formatting(h_match.group(2))
            html_lines.append(f"<h{h_level}>{h_text}</h{h_level}>")
            continue

        # Unordered list
        ul_match = re.match(r'^(\s*)[*\-]\s+(.*)$', line)
        if ul_match:
            indent = len(ul_match.group(1))
            current_level = (indent // 2) + 1
            item_text = inline_formatting(ul_match.group(2))
            
            if not in_ul:
                html_lines.extend(close_lists())
                html_lines.append("<ul>")
                in_ul = True
                ul_level = 1
            
            while ul_level < current_level:
                html_lines.append("<ul>")
                ul_level += 1
            while ul_level > current_level:
                html_lines.append("</ul>")
                ul_level -= 1
                
            html_lines.append(f"<li>{item_text}</li>")
            continue

        # Ordered list
        ol_match = re.match(r'^\s*(\d+)\.\s+(.*)$', line)
        if ol_match:
            item_text = inline_formatting(ol_match.group(2))
            if not in_ol:
                html_lines.extend(close_lists())
                html_lines.append("<ol>")
                in_ol = True
            html_lines.append(f"<li>{item_text}</li>")
            continue

        # Paragraph
        html_lines.extend(close_lists())
        p_text = inline_formatting(stripped)
        html_lines.append(f"<p>{p_text}</p>")

    # Close any open blocks
    html_lines.extend(close_lists())
    html_lines.extend(close_quote())
    html_lines.extend(close_table())

    html_lines.append("</body></html>")
    return "\n".join(html_lines)

def convert_file(md_path, html_path, odt_path, docx_path, title):
    print(f"Reading {md_path}...")
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_content = md_to_html(md_text, title)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved {html_path}")

    # Convert HTML to ODT using LibreOffice
    cmd_odt = [
        "libreoffice",
        "-env:UserInstallation=file:///home/hills/Documents/UWS/.lo_user",
        "--headless",
        "--convert-to", "odt",
        html_path,
        "--outdir", os.path.dirname(odt_path)
    ]
    print(f"Running: {' '.join(cmd_odt)}")
    res1 = subprocess.run(cmd_odt, capture_output=True, text=True)
    if res1.returncode != 0:
        print("Error generating ODT:", res1.stderr)
        return False
    print(f"Generated {odt_path}")

    # Convert ODT to DOCX using LibreOffice
    cmd_docx = [
        "libreoffice",
        "-env:UserInstallation=file:///home/hills/Documents/UWS/.lo_user",
        "--headless",
        "--convert-to", "docx",
        odt_path,
        "--outdir", os.path.dirname(docx_path)
    ]
    print(f"Running: {' '.join(cmd_docx)}")
    res2 = subprocess.run(cmd_docx, capture_output=True, text=True)
    if res2.returncode != 0:
        print("Error generating DOCX:", res2.stderr)
        return False
    print(f"Generated {docx_path}")
    return True

if __name__ == "__main__":
    work_dir = "/home/hills/Documents/UWS"
    
    # 1. Main Ukrainian document
    uov_md = os.path.join(work_dir, "Classification_of_UOV.md")
    uov_html = os.path.join(work_dir, "Classification_of_UOV.html")
    uov_odt = os.path.join(work_dir, "Classification_of_UOV.odt")
    uov_docx = os.path.join(work_dir, "Classification_of_UOV.docx")
    
    if os.path.exists(uov_md):
        convert_file(uov_md, uov_html, uov_odt, uov_docx, "Classification of Unmanned Orbital Vehicles (UOV)")
        
    # 2. LinkedIn English document
    li_md = os.path.join(work_dir, "Classification_of_UOV_LinkedIn.md")
    li_html = os.path.join(work_dir, "Classification_of_UOV_LinkedIn.html")
    li_odt = os.path.join(work_dir, "Classification_of_UOV_LinkedIn.odt")
    li_docx = os.path.join(work_dir, "Classification_of_UOV_LinkedIn.docx")
    
    if os.path.exists(li_md):
        convert_file(li_md, li_html, li_odt, li_docx, "Classification of UOV - LinkedIn Edition")

