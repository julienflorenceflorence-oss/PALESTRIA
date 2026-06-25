import codecs
import re

with open('mémoire/RDM 3.0/build_rdm_v11_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update TOC (Shift pages by +1 due to new Executive Summary page)
old_toc = """chapitres = [
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 3),
    ("LEXIQUE & ACRONYMES", 5),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 6),
    ("II. LE MARCHÉ : LA FATIGUE NUMÉRIQUE", 9),
    ("III. AUDIT INTERNE : LA VULNÉRABILITÉ DU MODÈLE", 12),
    ("IV. AUDIT DATA : LE FILTRE LÉGAL ALUR (126k LEADS)", 15),
    ("V. AUDIT ACQUISITION : LIMITES DE L'OUTBOUND", 18),
    ("VI. L'ANATOMIE DU PIVOT INBOUND & PRICING", 21),
    ("VII. LA RÉTENTION : DÉPLOIEMENT DU DASHBOARD", 25),
    ("VIII. LE PLAN D'ACTION (BUDGET M12 & COPIL)", 28),
    ("IX. PLAN DE CARRIÈRE & BILAN PERSONNEL", 32),
    ("X. DÉCLARATION DE CONFORMITÉ IA", 34),
    ("XI. ANNEXES PHYSIQUES & MATRICES", 35),
    ("XII. EXTRAITS & DOSSIER DRIVE SÉCURISÉ", 45)
]"""

new_toc = """chapitres = [
    ("EXECUTIVE SUMMARY (SYNTHÈSE)", 3),
    ("PRÉAMBULE : LE RÉFÉRENTIEL D'ARBITRAGE", 4),
    ("LEXIQUE & ACRONYMES", 6),
    ("I. L'ENTREPRISE & LA PROBLÉMATIQUE", 7),
    ("II. LE MARCHÉ : LA FATIGUE NUMÉRIQUE", 10),
    ("III. AUDIT INTERNE : LA VULNÉRABILITÉ DU MODÈLE", 13),
    ("IV. AUDIT DATA : LE FILTRE LÉGAL ALUR (126k LEADS)", 16),
    ("V. AUDIT ACQUISITION : LIMITES DE L'OUTBOUND", 19),
    ("VI. L'ANATOMIE DU PIVOT INBOUND & PRICING", 22),
    ("VII. LA RÉTENTION : DÉPLOIEMENT DU DASHBOARD", 26),
    ("VIII. LE PLAN D'ACTION (BUDGET M12 & COPIL)", 29),
    ("IX. PLAN DE CARRIÈRE & BILAN PERSONNEL", 33),
    ("X. DÉCLARATION DE CONFORMITÉ IA", 35),
    ("XI. ANNEXES PHYSIQUES & MATRICES", 36),
    ("XII. EXTRAITS & DOSSIER DRIVE SÉCURISÉ", 46)
]"""
c = c.replace(old_toc, new_toc)


# 2. Add Executive Summary Page (Page 3)
exec_summary_code = """
# --- PAGE 3 : EXECUTIVE SUMMARY ---
pages.append({
    "section": "EXECUTIVE SUMMARY",
    "content": \"\"\"
        <a id="chapitre-0"></a>
        <h1 style="color: var(--gold); border-bottom: 2px solid var(--gold); padding-bottom: 10px;">Executive Summary (Synthèse)</h1>
        
        <div class="glass-card" style="border-left: 4px solid var(--gold); padding: 25px; margin-top: 30px;">
            <h3 style="margin-top: 0; color: #FFF; font-size: 13pt;">1. Le Contexte & La Problématique</h3>
            <p style="font-size: 10pt; line-height: 1.6; color: var(--text-muted);">
            <strong>Réseau B2B Premium :</strong> Happy House gère 170 hébergeurs (60% Pros / 40% Particuliers) avec une équipe Lean (4 ETP).<br>
            <strong>Problématique :</strong> Comment réduire l'attrition tout en restructurant une acquisition rentable sans épuiser l'équipe ni dégrader la marque ?
            </p>
            
            <h3 style="margin-top: 25px; color: #FFF; font-size: 13pt;">2. Le Diagnostic (Le double déficit)</h3>
            <ul style="line-height: 1.6; font-size: 10pt; color: var(--text-muted);">
                <li><strong>Acquisition inopérante (Outbound) :</strong> Le démarchage à froid se heurte à la fatigue numérique du marché. Résultat : 14 500 appels pour un CAC insoutenable de <strong>1 823 €</strong> (face à un ARPU de 226 €).</li>
                <li><strong>Rétention critique (Churn) :</strong> 80% d'attrition sur la cohorte prospectée à froid. Cause : résistance au changement (non-usage de la centrale d'achats). La LTV stagne à <strong>290 €</strong>. Le ratio vital LTV/CAC s'effondre à 0,16.</li>
            </ul>

            <h3 style="margin-top: 25px; color: #FFF; font-size: 13pt;">3. Les Recommandations Stratégiques (Le Pivot)</h3>
            <ul style="line-height: 1.6; font-size: 10pt; color: var(--text-muted);">
                <li><strong>Axe Inbound :</strong> Arrêt du "Cold Calling". Utilisation de l'IA pour auditer 126k contacts et inviter les cibles conformes à la Loi ALUR vers des Afterworks régionaux exclusifs. <strong>Objectif CPA : 166 €</strong>.</li>
                <li><strong>Axe Rétention :</strong> Création d'un outil "Low-Code" (Dashboard ROI trimestriel) pour objectiver les économies de l'hébergeur et forcer l'usage des outils d'optimisation.</li>
            </ul>
        </div>
    \"\"\"
})
"""
# Insert before "PAGE 3 : METHODOLOGIE" (which becomes PAGE 4)
c = c.replace("# --- PAGE 3 : METHODOLOGIE ---", exec_summary_code + "\n# --- PAGE 4 : METHODOLOGIE ---")


# 3. Add CAC Formula in Annexe 4
old_cac = """<div class="code-line" style="color: #E74C3C; font-weight: bold; font-size: 14pt;">=> Coût d'Acquisition Client (CAC) Fixé : 1 823 € par Membre.</div>"""
new_cac = """<div class="code-line" style="color: #E74C3C; font-weight: bold; font-size: 14pt;">=> Coût d'Acquisition Client (CAC) Fixé : 1 823 € par Membre.</div>
                
                <div style="background: rgba(255,255,255,0.05); border: 1px dashed #E74C3C; padding: 15px; margin-top: 15px;">
                    <strong style="color: #E74C3C; font-size: 9.5pt; display: block; margin-bottom: 5px;">NOTE MÉTHODOLOGIQUE DE CALCUL DU C.A.C :</strong>
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 9pt; color: #FFF; display: block; margin-bottom: 8px;">
                    Formule : (Coût salarial brut chargé du SDR + Coûts des outils téléphoniques mensuels) / Nombre de signatures générées.
                    </span>
                    <span style="font-family: 'Courier New', Courier, monospace; font-size: 9pt; color: var(--gold); font-style: italic;">
                    Exemple audité : (Salaire 1766€ + Outils 57€) / 1 signature = 1 823 €.
                    </span>
                </div>"""
c = c.replace(old_cac, new_cac)


# 4. Add Competencies Table in Chapter 9
old_bilan = """(Méthodologie comportementale DISC avec le SDR Younes).</p>"""
new_bilan = """(Méthodologie comportementale DISC avec le SDR Younes).</p>

        <h2 style="margin-top: 35px; color: var(--gold-light);">Bilan des Compétences Acquises</h2>
        <table style='width: 100%; border-collapse: collapse; font-size: 9.5pt; margin-top: 15px;'>
            <tr style='background: rgba(221, 168, 62, 0.2);'><th style='width: 50%; padding: 15px; text-align: center;'>HARD SKILLS (Savoir-Faire Technique)</th><th style='width: 50%; padding: 15px; text-align: center;'>SOFT SKILLS (Savoir-Être Managérial)</th></tr>
            <tr>
                <td style='padding: 15px; line-height: 1.6;'>
                    • <strong>Maîtrise de l'IA générative :</strong> Utilisation avancée de Gemini pour le traitement sémantique et la qualification de bases de données.<br><br>
                    • <strong>Data Analysis & Web-Scraping :</strong> Collecte, nettoyage et structuration de très gros volumes (126 000 leads).<br><br>
                    • <strong>Business Intelligence (BI) :</strong> Création de Dashboards ROI et modélisation financière (Calculs LTV/CAC, cohortes).
                </td>
                <td style='padding: 15px; line-height: 1.6;'>
                    • <strong>Résilience Politique :</strong> Capacité à accepter le refus d'un dirigeant et à rebondir sur une stratégie alternative adaptée à l'ADN de la marque.<br><br>
                    • <strong>Vulgarisation Analytique :</strong> Traduction de données complexes en enjeux métiers pour une gouvernance non-technique.<br><br>
                    • <strong>Co-construction & Leadership :</strong> Prise en compte accrue des avis collaborateurs pour favoriser l'implication collective et optimiser le pilotage d'équipe.
                </td>
            </tr>
        </table>"""
c = c.replace(old_bilan, new_bilan)


# 5. Version Upgrades
c = c.replace("RAPPORT_DE_MISSION_V11_SOUTENANCE.html", "RAPPORT_DE_MISSION_V12_SOUTENANCE.html")
c = c.replace("V11 SOUTENANCE", "V12 SOUTENANCE")
c = c.replace("ÉDITION V11 SOUTENANCE", "ÉDITION V12 SOUTENANCE")

with open('mémoire/RDM 3.0/build_rdm_v12_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("V12 builder script created with Exec Summary, CAC Formula, and Competencies table.")
