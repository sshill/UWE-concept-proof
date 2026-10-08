#!/usr/bin/env python3
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
        (r'\\mathcal{E}', 'ℰ'),
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
        if "mathbf{UOV}" in content or "Physical" in content:
            rendered = (
                '<div style="text-align: center; margin: 12pt 0; padding: 10pt; background-color: #f8fafc; border: 1.5px solid #0f2b48; border-radius: 4px;">'
                '<div style="font-size: 11pt; font-weight: bold; color: #0f2b48; letter-spacing: 0.5px;">'
                'UOV = [ Physical Regime &middot; Propulsion ] &minus; [ Lifecycle &middot; Mission ] &minus; [ Autonomy &middot; Control ]'
                '</div>'
                '<div style="font-size: 8.5pt; color: #475569; margin-top: 3pt; font-style: italic;">'
                'The Six-Character Unmanned Orbital Vehicle (UOV) Taxonomy'
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
        if "mathcal{E}" in content or "frac{\\mu}{2a}" in content or "v^2" in content:
            rendered = (
                '<div style="text-align: center; margin: 14pt 0 12pt 0;">'
                '  <table align="center" style="border-collapse: collapse; font-family: \'Cambria Math\', \'Times New Roman\', serif; font-size: 13pt; color: #0f2b48;">'
                '    <tr>'
                '      <td style="font-style: italic; font-size: 14pt; padding: 0 4pt; vertical-align: middle;">ℰ</td>'
                '      <td style="font-size: 14pt; padding: 0 4pt; vertical-align: middle;">=</td>'
                '      <td style="font-size: 14pt; padding: 0 2pt; vertical-align: middle;">&minus;</td>'
                '      <td style="vertical-align: middle; text-align: center; padding: 0 4pt;">'
                '        <div style="border-bottom: 1.2px solid #0f2b48; padding: 0 3pt 1px 3pt; font-style: italic;">μ</div>'
                '        <div style="padding-top: 1px; font-style: italic;">2a</div>'
                '      </td>'
                '      <td style="font-size: 14pt; padding: 0 4pt; vertical-align: middle;">=</td>'
                '      <td style="vertical-align: middle; text-align: center; padding: 0 4pt;">'
                '        <div style="border-bottom: 1.2px solid #0f2b48; padding: 0 3pt 1px 3pt; font-style: italic;">v<sup>2</sup></div>'
                '        <div style="padding-top: 1px; font-style: normal;">2</div>'
                '      </td>'
                '      <td style="font-size: 14pt; padding: 0 2pt; vertical-align: middle;">&minus;</td>'
                '      <td style="vertical-align: middle; text-align: center; padding: 0 4pt;">'
                '        <div style="border-bottom: 1.2px solid #0f2b48; padding: 0 3pt 1px 3pt; font-style: italic;">μ</div>'
                '        <div style="padding-top: 1px; font-style: italic;">r</div>'
                '      </td>'
                '    </tr>'
                '  </table>'
                '  <div style="font-size: 8.5pt; color: #64748b; font-style: italic; margin-top: 5pt;">'
                '    Specific Mechanical Orbital Energy (Vis-Viva Integral)'
                '  </div>'
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
        text = text.replace(f"{{{{CODETOKEN:{i}}}}}", f'<code style="font-family: Consolas, monospace; background-color: #f1f5f9; padding: 1px 3px; border-radius: 2px; font-size: 8.5pt; color: #0f172a; border: 1px solid #cbd5e1;">{escaped}</code>')

    # 9. Restore escaped dollar signs
    for i, tok in enumerate(dollar_tokens):
        text = text.replace(f"{{{{DOLLARESC:{i}}}}}", tok)

    return text

def md_to_html(md_text, title="The Kondratyuk Paradigm"):
    lines = md_text.splitlines()
    html_lines = []

    css = """
    @page {
        size: A4;
        margin: 15mm 16mm 15mm 16mm;
    }
    body {
        font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
        line-height: 1.32;
        font-size: 10pt;
        color: #1e293b;
        max-width: 850px;
        margin: 0 auto;
        padding: 10px;
        background-color: #ffffff;
    }
    h1 {
        font-size: 17pt;
        font-weight: 700;
        color: #0f2b48;
        border-bottom: 2px solid #0f2b48;
        padding-bottom: 5pt;
        margin-top: 14pt;
        margin-bottom: 6pt;
        line-height: 1.25;
    }
    h2 {
        font-size: 12.5pt;
        font-weight: 700;
        color: #0f2b48;
        border-bottom: 1.5pt solid #cbd5e1;
        padding-bottom: 3pt;
        margin-top: 13pt;
        margin-bottom: 5pt;
    }
    h3 {
        font-size: 11pt;
        font-weight: 600;
        color: #1e3a8a;
        margin-top: 10pt;
        margin-bottom: 4pt;
    }
    h4 {
        font-size: 10pt;
        font-weight: 600;
        color: #334155;
        margin-top: 8pt;
        margin-bottom: 3pt;
    }
    h5 {
        font-size: 9.5pt;
        font-weight: 600;
        color: #475569;
        margin-top: 6pt;
        margin-bottom: 2pt;
    }
    p {
        margin: 3.5pt 0;
        text-align: justify;
    }
    hr {
        border: 0;
        border-top: 1px solid #cbd5e1;
        margin: 9pt 0;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 10pt 0;
        font-size: 8pt;
        line-height: 1.2;
        border: 1px solid #94a3b8;
    }
    thead {
        display: table-header-group;
    }
    tr {
        page-break-inside: avoid;
        break-inside: avoid;
    }
    th {
        background-color: #f1f5f9;
        color: #0f2b48;
        font-weight: 700;
        border: 1px solid #94a3b8;
        padding: 4pt 5pt;
        text-align: left !important;
    }
    td {
        border: 1px solid #cbd5e1;
        padding: 3pt 5pt;
        vertical-align: top;
        text-align: left !important;
    }
    td p {
        text-align: left !important;
        margin: 0;
    }
    tr:nth-child(even) td {
        background-color: #f8fafc;
    }
    pre {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 4px;
        padding: 6pt 8pt;
        font-family: Consolas, monospace;
        font-size: 8pt;
        line-height: 1.25;
        white-space: pre-wrap;
        margin: 6pt 0;
    }
    blockquote {
        border-left: 3.5pt solid #0284c7;
        margin: 6pt 0;
        padding: 4pt 10pt;
        background-color: #f0f9ff;
        color: #0369a1;
        font-style: italic;
    }
    ul, ol {
        margin: 4pt 0 4pt 16pt;
        padding: 0;
    }
    li {
        margin-bottom: 2.5pt;
    }
    """

    html_lines.append(f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{css}</style></head><body>')

    in_code = False
    code_content = []
    in_table = False
    table_rows = []
    list_stack = []
    in_quote = False
    quote_lines = []

    def close_all_lists():
        nonlocal list_stack
        out = []
        while list_stack:
            tag, _ = list_stack.pop()
            out.append(f"</{tag}>")
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
            out.append('<table border="1" cellspacing="0" cellpadding="5">')
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

        if stripped.startswith("```") or stripped.startswith("~~~~"):
            if in_code:
                html_lines.extend(close_all_lists())
                escaped_code = html.escape("\n".join(code_content))
                html_lines.append(f"<pre><code>{escaped_code}</code></pre>")
                in_code = False
                code_content = []
            else:
                html_lines.extend(close_all_lists())
                html_lines.extend(close_quote())
                html_lines.extend(close_table())
                in_code = True
                code_content = []
            continue

        if in_code:
            code_content.append(raw_line)
            continue

        if stripped.startswith(">"):
            html_lines.extend(close_all_lists())
            html_lines.extend(close_table())
            in_quote = True
            q_text = stripped.lstrip("> ").strip()
            quote_lines.append(inline_formatting(q_text))
            continue
        elif in_quote:
            html_lines.extend(close_quote())

        if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2:
            html_lines.extend(close_all_lists())
            html_lines.extend(close_quote())
            if re.match(r'^\|[\s\:\-\|]+\|$', stripped):
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

        if not stripped:
            continue

        if re.match(r'^(?:---|\*\*\*|___)\s*$', stripped):
            html_lines.extend(close_all_lists())
            html_lines.extend(close_quote())
            html_lines.extend(close_table())
            html_lines.append('<hr>')
            continue

        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', stripped)
        if img_match:
            html_lines.extend(close_all_lists())
            html_lines.extend(close_quote())
            html_lines.extend(close_table())
            caption = img_match.group(1)
            src = img_match.group(2)
            work_dir = "/home/hills/Documents/UWS"
            abs_src = os.path.join(work_dir, src) if not os.path.isabs(src) else src
            html_lines.append(f'<div style="text-align: center; margin: 12pt 0; page-break-inside: avoid;"><img src="{abs_src}" style="max-width: 100%; height: auto; border: 1.5px solid #0f2b48; border-radius: 4px;" /><div style="font-size: 8pt; color: #475569; margin-top: 4pt; font-style: italic; font-weight: 600;">{html.escape(caption)}</div></div>')
            continue

        h_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        if h_match:
            html_lines.extend(close_all_lists())
            html_lines.extend(close_quote())
            html_lines.extend(close_table())
            h_level = len(h_match.group(1))
            h_text = inline_formatting(h_match.group(2))
            html_lines.append(f"<h{h_level}>{h_text}</h{h_level}>")
            continue

        ol_match = re.match(r'^(\s*)(\d+)\.\s+(.*)$', line)
        if ol_match:
            indent = len(ol_match.group(1))
            item_text = inline_formatting(ol_match.group(3))
            while list_stack and list_stack[-1][0] == 'ul' and list_stack[-1][1] > indent:
                tag, _ = list_stack.pop()
                html_lines.append(f"</{tag}>")
            if not list_stack or list_stack[-1][0] != 'ol':
                html_lines.append("<ol>")
                list_stack.append(('ol', indent))
            html_lines.append(f"<li>{item_text}</li>")
            continue

        ul_match = re.match(r'^(\s*)[*\-]\s+(.*)$', line)
        if ul_match:
            indent = len(ul_match.group(1))
            item_text = inline_formatting(ul_match.group(2))
            while list_stack and list_stack[-1][1] > indent:
                tag, _ = list_stack.pop()
                html_lines.append(f"</{tag}>")
            if not list_stack or list_stack[-1][1] < indent or list_stack[-1][0] != 'ul':
                html_lines.append("<ul>")
                list_stack.append(('ul', indent))
            html_lines.append(f"<li>{item_text}</li>")
            continue

        html_lines.extend(close_all_lists())
        p_text = inline_formatting(stripped)
        html_lines.append(f"<p>{p_text}</p>")

    html_lines.extend(close_all_lists())
    html_lines.extend(close_quote())
    html_lines.extend(close_table())
    html_lines.append("</body></html>")
    return "\n".join(html_lines)

def convert_one(base_name, title):
    work_dir = "/home/hills/Documents/UWS"
    md_file = os.path.join(work_dir, f"{base_name}.md")
    html_file = os.path.join(work_dir, f"{base_name}.html")
    odt_file = os.path.join(work_dir, f"{base_name}.odt")
    docx_file = os.path.join(work_dir, f"{base_name}.docx")
    pdf_file = os.path.join(work_dir, f"{base_name}.pdf")

    print(f"\n==========================================")
    print(f"Processing {base_name}...")
    print(f"Reading {md_file}...")
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Part 1 vs Part 2 filtering:
    # If the markdown has PART 2, extract exclusively Part 2 (The Manuscript):
    part2_match = re.search(r"##\s*PART 2:[^\n]*\n(.*)", md_text, re.DOTALL)
    if part2_match:
        md_text = part2_match.group(1).strip()
        print(f"Extracted Part 2 (The Manuscript) exclusively for {base_name}.")
    elif "## Executive Pitch & Context" in md_text:
        md_text = re.sub(r'##\s*Executive Pitch & Context.*?(?=\n##|\Z)', '', md_text, flags=re.DOTALL)
        md_text = re.sub(r'(?:---\s*){2,}', '---\n\n', md_text)
        print(f"Stripped Executive Pitch & Context for {base_name}.")

    html_content = md_to_html(md_text, title)
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
    staged_odt = os.path.join(staging_dir, f"{base_name}.odt")
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
    staged_docx = os.path.join(staging_dir, f"{base_name}.docx")
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
    staged_pdf = os.path.join(staging_dir, f"{base_name}.pdf")
    shutil.copy2(staged_pdf, pdf_file)

    print(f"Conversion of {base_name} completed successfully!")
    print(f"DOCX: {docx_file}")
    print(f"PDF:  {pdf_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1].replace(".md", "")
        convert_one(target, "The Kondratyuk Paradigm in Orbital Warfare")
    else:
        convert_one("UWE_Space_Review_Submission", "The Kondratyuk Paradigm - The Space Review Submission")
        convert_one("UWE_SpaceNews_OpEd", "Beyond Satellite Mass - SpaceNews Op-Ed")
