import os
import re

def analyze_pages(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to find pages
    pages = re.findall(r'(<div class="page"[^>]*>.*?</div>\s*</div>)', content, re.DOTALL)
    
    results = []
    for i, page in enumerate(pages):
        # Check if it has h1
        has_h1 = '<h1>' in page
        # Check if it has content
        has_content = 'class="content"' in page or 'class=\'content\'' in page
        # Check if it's TOC
        is_toc = 'id="toc"' in page or 'class="sommaire"' in page
        
        if has_h1 and not has_content and not is_toc:
            results.append(i + 1)
            
    return results

html_files = [f for f in os.listdir('mémoire') if f.endswith('.html')]
for f in html_files:
    path = os.path.join('mémoire', f)
    pages = analyze_pages(path)
    if pages:
        print(f"{f}: Pages {pages}")
