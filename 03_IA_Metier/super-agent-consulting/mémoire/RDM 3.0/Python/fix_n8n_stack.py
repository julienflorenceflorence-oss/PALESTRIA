import codecs

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the Tech Stack explanation to match exact user requirement
old_tech_stack = """<div class="analytic-content">Le tri de cette volumétrie n'est pas manuel, il est technologique. J'ai conçu et configuré un <strong>Agent IA (motorisé par Gemini Pro)</strong> couplé à une infrastructure d'automatisation sur <strong>Google Sheets</strong>. Le système s'est branché sur <em>societe.com</em> pour opérer la scission légale initiale : séparer les Hébergeurs Professionnels des Particuliers. L'Agent IA a ensuite évalué sémantiquement les critères de confort (3 à 5 étoiles), la présence de prestations annexes (ventes additionnelles) et le volume d'avis clients. Ce scan exhaustif sur les <span class="analytic-highlight">126 000 lignes prospects</span> livre une répartition implacable"""

new_tech_stack = """<div class="analytic-content">Le tri de cette volumétrie n'est pas manuel, il est technologique. J'ai conçu et configuré un <strong>Agent IA (motorisé par Gemini Pro)</strong> couplé à une infrastructure d'automatisation <strong>n8n</strong> pour orchestrer un workflow entre <strong>Google Sheets, societe.com et ma propre adresse email</strong>. Le système s'est branché sur societe.com pour opérer la scission légale initiale : séparer les Hébergeurs Professionnels des Particuliers. L'Agent IA a ensuite évalué sémantiquement les critères de confort (3 à 5 étoiles), la présence de prestations annexes (ventes additionnelles) et le volume d'avis clients. Ce scan exhaustif sur les <span class="analytic-highlight">126 000 lignes prospects</span> livre une répartition implacable"""

c = c.replace(old_tech_stack, new_tech_stack)

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Tech stack explicitly updated to include n8n orchestration with Gemini, Sheets, societe.com and email.")
