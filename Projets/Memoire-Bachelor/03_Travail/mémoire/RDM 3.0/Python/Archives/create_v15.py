import codecs
import re

with open('mémoire/RDM 3.0/build_rdm_v14_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add CSS for the button
btn_css = """
        .btn-sommaire {
            display: inline-block;
            font-family: 'Arial', sans-serif;
            font-size: 8pt;
            color: #777;
            text-decoration: none;
            border: 1px solid #444;
            padding: 2px 8px;
            border-radius: 3px;
            margin-left: 15px;
            vertical-align: middle;
            transition: all 0.2s ease-in-out;
        }
        .btn-sommaire:hover {
            background: var(--gold);
            color: var(--black);
            border-color: var(--gold);
        }
"""
if ".btn-sommaire" not in c:
    c = c.replace("</style>", btn_css + "\n    </style>")

# 2. Add anchor to the Table of Contents
old_sommaire_h1 = '<h1 style="color: #DDA83E; text-align: center;">Sommaire Analytique Général</h1>'
new_sommaire_h1 = '<a id="sommaire-anchor"></a><h1 style="color: #DDA83E; text-align: center;">Sommaire Analytique Général</h1>'
if '<a id="sommaire-anchor">' not in c:
    c = c.replace(old_sommaire_h1, new_sommaire_h1)

# 3. Add the button to all chapter H1 tags using a robust replacement function
button_html = ' <a href="#sommaire-anchor" class="btn-sommaire">Retour au Sommaire</a>'

def add_button_to_h1(match):
    h1_tag = match.group(1)
    # Do not add the button to the Table of Contents itself, or the Executive Summary
    if "Sommaire Analytique" in h1_tag or "Executive Summary" in h1_tag:
        return f"<h1>{h1_tag}</h1>"
    # Prevent adding duplicate buttons
    if "Retour au Sommaire" in h1_tag:
        return f"<h1>{h1_tag}</h1>"
    return f"<h1>{h1_tag}{button_html}</h1>"

# This regex finds the content inside <h1> tags and passes it to the function
c = re.sub(r'<h1>(.*?)</h1>', add_button_to_h1, c, flags=re.DOTALL)


# --- UPDATE VERSIONING ---
c = c.replace("V14 SOUTENANCE", "V15 SOUTENANCE")
c = c.replace("RAPPORT_DE_MISSION_V14_SOUTENANCE.html", "RAPPORT_DE_MISSION_V15_SOUTENANCE.html")
c = c.replace("ÉDITION V14 SOUTENANCE", "ÉDITION V15 SOUTENANCE")


with open('mémoire/RDM 3.0/build_rdm_v15_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("V15 builder script created with 'Back to Summary' buttons.")
