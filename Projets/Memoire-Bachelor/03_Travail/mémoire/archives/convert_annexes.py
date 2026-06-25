import os
import markdown

template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {{ --gold: #DDA83E; --bg: #0A0C1A; --border: rgba(212, 175, 55, 0.3); --text: #E0E0E0; --card: rgba(255,255,255,0.03); }}
        body {{ margin: 0; padding: 20px; background: var(--bg); color: var(--text); font-family: 'Montserrat', sans-serif; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
        .page {{ max-width: 210mm; margin: 0 auto; background: #0F1115; padding: 20mm; box-shadow: 0 0 30px rgba(0,0,0,0.8); }}
        @media print {{
            body {{ padding: 0; background: #0F1115;}}
            .page {{ margin: 0; padding: 15mm; width: 100%; max-width: 100%; box-shadow: none; }}
            h1, h2, h3 {{ color: var(--gold) !important; }}
            th {{ background: rgba(212, 175, 55, 0.1) !important; color: var(--gold) !important; }}
            td {{ background: var(--card) !important; }}
            /* Ensure links look good in print */
            a {{ color: var(--gold); text-decoration: none; border: 1px solid var(--gold); padding: 10px; display: inline-block; }}
        }}
        h1 {{ font-family: 'Cinzel', serif; color: var(--gold); text-align: center; border-bottom: 2px solid var(--gold); padding-bottom: 15px; font-size: 20pt; margin-bottom: 30px; }}
        h2 {{ font-family: 'Cinzel', serif; color: var(--gold); font-size: 14pt; margin-top: 30px; border-left: 3px solid var(--gold); padding-left: 10px; }}
        h3 {{ font-family: 'Cinzel', serif; color: #BCBFD0; font-size: 11pt; }}
        p, li {{ line-height: 1.6; font-size: 10pt; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 9pt; }}
        th, td {{ border: 1px solid var(--border); padding: 12px; text-align: left; vertical-align: top; }}
        th {{ font-family: 'Cinzel', serif; color: var(--gold); background: rgba(212, 175, 55, 0.1); }}
        td {{ background: var(--card); }}
    </style>
</head>
<body>
    <div class="page">
        {content}
    </div>
</body>
</html>"""

annex_dir = r"C:\Users\julien\OneDrive\Bureau\geminicli\super-agent-consulting\mémoire\RDM 3.0\annexe"

for filename in os.listdir(annex_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(annex_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                md_text = f.read()
            
            html_content = markdown.markdown(md_text, extensions=['tables'])
            
            html_filepath = os.path.join(annex_dir, filename.replace('.md', '.html'))
            with open(html_filepath, 'w', encoding='utf-8') as f:
                f.write(template.format(title=filename.replace('.md', '').replace('_', ' ').title(), content=html_content))
            print(f"Created {html_filepath}")
