import codecs

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the Tech Stack explanation in Chapter 4
old_tech_stack = """<div class="analytic-point">3. Les Preuves Chiffrées (L'Architecture de Filtrage via n8n)</div>
        <div class="analytic-content">Le tri n'est pas manuel, il est technologique. L'agent IA que j'ai configuré via l'outil <strong>n8n</strong> s'est branché sur l'API de <em>societe.fr</em> pour opérer une première scission automatisée : séparer les Hébergeurs Professionnels des Particuliers. Une seconde automatisation a évalué les critères de confort (3 à 5 étoiles), les prestations annexes (ventes additionnelles) et le volume d'avis clients. Ce scan exhaustif sur les <span class="analytic-highlight">126 000 lignes prospects</span> livre une répartition implacable"""

new_tech_stack = """<div class="analytic-point">3. Les Preuves Chiffrées (L'Architecture IA & Data)</div>
        <div class="analytic-content">Le tri de cette volumétrie n'est pas manuel, il est technologique. J'ai conçu et configuré un <strong>Agent IA (motorisé par Gemini Pro)</strong> couplé à une infrastructure d'automatisation sur <strong>Google Sheets</strong>. Le système s'est branché sur <em>societe.com</em> pour opérer la scission légale initiale : séparer les Hébergeurs Professionnels des Particuliers. L'Agent IA a ensuite évalué sémantiquement les critères de confort (3 à 5 étoiles), la présence de prestations annexes (ventes additionnelles) et le volume d'avis clients. Ce scan exhaustif sur les <span class="analytic-highlight">126 000 lignes prospects</span> livre une répartition implacable"""

c = c.replace(old_tech_stack, new_tech_stack)

# Also fix the Nurturing mention if it implied n8n wrongly
old_nurturing = """<div class="analytic-content">Le fichier de 126k contacts devient un outil de <em>Ciblage d'Urgence</em>. Une fois la sélection algorithmique terminée, n8n a orchestré la mise en relation automatisée avec les Offices du Tourisme locaux (prise de contact avec les responsables hébergement) couplée à l'envoi d'une série d'emails de chauffe ("Nurturing") pour préparer le terrain avant l'appel du SDR. """

new_nurturing = """<div class="analytic-content">Le fichier de 126k contacts devient un outil de <em>Ciblage d'Urgence</em>. Une fois la sélection IA terminée, les processus d'automatisation ont orchestré la mise en relation avec les Offices du Tourisme locaux (identification des responsables hébergement), couplée à l'envoi d'une série d'emails de chauffe ("Nurturing") pour préparer le terrain légitimé avant l'appel d'invitation du SDR. """

c = c.replace(old_nurturing, new_nurturing)

with open('mémoire/RDM 3.0/build_rdm_v7_mastodonte.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Tech stack corrected from n8n to Gemini Pro and Google Sheets.")
