import re
import os

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for the new button
new_css = """
        .back-btn {
            background: rgba(221, 168, 62, 0.1);
            border: 1px solid var(--gold);
            color: var(--gold) !important;
            padding: 4px 12px;
            font-family: 'Cinzel';
            font-size: 7pt;
            letter-spacing: 1px;
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none !important;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .back-btn:hover {
            background: var(--gold);
            color: #000 !important;
        }
        @media print {
            .back-btn { display: none !important; }
        }
"""

content = content.replace('</style>', f"{new_css}\n    </style>")

# 2. Inject the button in all footers (except page 1 and 2)
# We look for <div class="footer"><div>SECTION NAME</div><div class="page-num">XX</div></div>
# We want to change it to <div class="footer"><a href="#toc" class="back-btn">◈ DASHBOARD</a><div>SECTION NAME</div><div class="page-num">XX</div></div>

def add_back_button(match):
    full_footer = match.group(0)
    # Check if it's page 01 or 02
    if 'class="page-num">01<' in full_footer or 'class="page-num">02<' in full_footer:
        return full_footer
    
    # Inject the button at the start of the footer
    new_footer = full_footer.replace('<div class="footer">', '<div class="footer"><a href="#toc" class="back-btn">◈ BACK TO CENTER</a>')
    return new_footer

content = re.sub(r'(?s)<div class="footer">.*?</div>', add_back_button, content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Back buttons added to all footers.")
