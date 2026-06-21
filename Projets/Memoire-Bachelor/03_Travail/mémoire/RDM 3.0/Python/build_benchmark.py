import os
import sys
import subprocess
import asyncio

def generate_csv(csv_path):
    csv_content = """annee;type;zone;indicateur;valeur;source
2013;OTA;Europe;Part de marché OTAs distribution hôtelier;19.7%;HOTREC Study 2013
2015;OTA;Europe;Part de marché OTAs (nuitées);22.0%;Eurostat Tourism 2015
2016;OTA;France;Français réservant par OTA;44.0%;Baromètre du Numérique 2016
2016;OTA;France;Français réservant sur Internet;72.0%;Baromètre du Numérique 2016
2019;OTA;Europe;Part de marché OTAs;29.2%;HOTREC Study 2019
2019;OTA;France;Part de marché OTAs distribution hôtelier;27.6%;Coach Omnium 2019
2021;OTA;Europe;Part de marché OTAs;28.8%;HOTREC Study 2021
2023;OTA;Europe;Part de marché OTAs;29.6%;HOTREC / Phocuswright 2023
2023;OTA;Europe;Booking Holdings part de marché;71.0%;HOTREC Study 2023
2023;OTA;Europe;Expedia part de marché;14.4%;HOTREC Study 2023
2023;OTA;Europe;HRS part de marché;4.6%;HOTREC Study 2023
2024;OTA;Europe;Booking.com part de marché;69.3%;HOTREC / D-EDGE 2024
2024;OTA;Europe;Expedia part de marché;11.5%;HOTREC / D-EDGE 2024
2024;OTA;Mondial;Marché OTA (milliards $);253.2;Statista Report 2024
2024;OTA;Mondial;Revenus 4 grandes OTAs (milliards $);58.0%;SEC Filings 2024
2024;OTA;Loisirs;Part OTAs revenus loisirs;18.0%;Phocuswright B2B 2024
2022;Label;France;Clef Verte établissements;855;Teragir / Clef Verte 2022
2023;Label;France;Clef Verte établissements;1077;Teragir / Clef Verte 2023
2024;Label;France;Clef Verte établissements;1564;Teragir / Clef Verte 2024
2025;Label;France;Clef Verte établissements;2428;Teragir / Clef Verte 2025
2005;Label;France;Création Qualité Tourisme;2005;DGE Historique
2013;Label;France;Qualité Tourisme établissements;5600;DGE Statistiques 2013
2021;Label;France;Qualité Tourisme établissements;4000;Ministère de l'Économie 2021
2024;Label;France;Qualité Tourisme établissements;5000;DGE Bilan 2024
2024;Label;France;Tourisme et Handicap établissements;3500;DGE Bilan 2024
2024;Label;France;Fin attribution Qualité Tourisme;31/08/2024;Décret Destination d'Excellence
2024;Label;France;Destination Excellence premier labellisés;203;DGE Bilan Sept 2024
2026;Label;France;Disparition totale Qualité Tourisme;31/12/2026;Décret Destination d'Excellence
2024;Label;Europe/France;Écolabel européen produits/services;98977;Commission Européenne 2024
2024;Label;Europe/France;Écolabel européen licences;2983;Commission Européenne 2024
"""
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(csv_content)
    print(f"[OK] CSV généré dans : {csv_path}")

def generate_html(html_path):
    html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BENCHMARK STRATÉGIQUE : OTAs & LABELS TOURISTIQUES</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@300;400;600&family=Playfair+Display:ital,wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #D4AF37;
            --gold-light: #F3E5AB;
            --bg-dark: #0F1115;
            --card-bg: rgba(255, 255, 255, 0.03);
            --border-gold: rgba(212, 175, 55, 0.2);
            --text-main: rgba(255, 255, 255, 0.9);
            --text-muted: rgba(255, 255, 255, 0.6);
        }

        @page { size: A4; margin: 0; }
        * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }

        body {
            margin: 0; padding: 0;
            background-color: #1a1a1a;
            color: var(--text-main);
            font-family: 'Montserrat', sans-serif;
            font-size: 11pt; line-height: 1.6;
        }

        .page {
            width: 210mm; height: 297mm;
            margin: 20px auto; background-color: var(--bg-dark);
            position: relative; overflow: hidden;
            display: flex; flex-direction: column;
            box-shadow: 0 0 50px rgba(0,0,0,0.5);
            page-break-after: always;
        }

        @media print {
            body { background: none; }
            .page { margin: 0; box-shadow: none; }
        }

        .page::before {
            content: ''; position: absolute;
            top: 10mm; left: 10mm; right: 10mm; bottom: 10mm;
            border: 1px solid var(--border-gold);
            pointer-events: none; z-index: 1;
        }

        .corner { position: absolute; width: 15mm; height: 15mm; border: 2px solid var(--gold); z-index: 2; }
        .top-left { top: 8mm; left: 8mm; border-right: none; border-bottom: none; }
        .top-right { top: 8mm; right: 8mm; border-left: none; border-bottom: none; }
        .bottom-left { bottom: 8mm; left: 8mm; border-right: none; border-top: none; }
        .bottom-right { bottom: 8mm; right: 8mm; border-left: none; border-top: none; }

        .content { padding: 25mm 20mm; position: relative; z-index: 10; flex-grow: 1; display: flex; flex-direction: column; justify-content: flex-start; }

        h1 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 20pt; text-transform: uppercase; letter-spacing: 4px; margin-bottom: 25px; text-align: center; font-weight: 700; }
        h2 { font-family: 'Cinzel', serif; color: var(--gold-light); font-size: 14pt; border-left: 3px solid var(--gold); padding-left: 15px; margin: 25px 0 15px 0; text-transform: uppercase; letter-spacing: 2px; }
        h3 { font-family: 'Cinzel', serif; color: var(--gold); font-size: 12pt; margin: 15px 0 10px 0; }
        p { margin-bottom: 15px; text-align: justify; }

        .glass-card { background: var(--card-bg); backdrop-filter: blur(10px); border: 1px solid var(--border-gold); padding: 20px; border-radius: 4px; margin: 15px 0; position: relative; }
        .glass-card::after { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, var(--gold), transparent); }

        .footer { position: absolute; bottom: 10mm; left: 20mm; right: 20mm; display: flex; justify-content: space-between; align-items: center; font-family: 'Cinzel', serif; font-size: 8pt; color: var(--gold); letter-spacing: 2px; z-index: 100; border-top: 1px solid rgba(212, 175, 55, 0.3); padding-top: 5px; }
        .page-number { font-weight: 700; }

        .cover { justify-content: center; align-items: center; text-align: center; background-color: var(--bg-dark); }
        .cover-content { width: 100%; height: 100%; padding: 30mm 20mm; display: flex; flex-direction: column; justify-content: space-between; align-items: center; }
        .tagline { font-family: 'Cinzel', serif; font-size: 11pt; color: var(--gold); letter-spacing: 6px; margin-bottom: 10px; }
        .main-title { font-size: 26pt; line-height: 1.2; margin: 30px 0; font-family: 'Cinzel', serif; font-weight: 900; color: #FFF; }
        .author-box { margin-top: 50px; font-family: 'Cinzel', serif; }
        .author-name { font-size: 18pt; font-weight: 900; letter-spacing: 3px; color: var(--gold); }
        .author-role { color: #FFF; font-size: 9pt; text-transform: uppercase; letter-spacing: 2px; margin-top: 5px; }

        table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 8.5pt; }
        th { background: rgba(212, 175, 55, 0.1); color: var(--gold); font-family: 'Cinzel', serif; padding: 8px 10px; border: 1px solid var(--border-gold); text-align: left; font-size: 8pt; }
        td { padding: 8px 10px; border: 1px solid var(--border-gold); background: rgba(255,255,255,0.01); color: #fff; vertical-align: top; }
        
        .source-tag { font-size: 7.5pt; color: var(--gold-light); font-style: italic; }
    </style>
</head>
<body>

    <!-- PAGE 1 : COUVERTURE -->
    <div class="page cover">
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="cover-content">
            <div class="tagline">ÉTUDE COMPARATIVE ET BENCHMARK</div>
            <h1 class="main-title">ANALYSE DOCUMENTÉE<br>DES OTAs & LABELS TOURISTIQUES<br>(2013 - 2026)</h1>
            <div style="width: 80px; height: 3px; background: var(--gold); margin: 20px auto;"></div>
            
            <div class="glass-card" style="width: 90%; max-width: 500px; margin: 20px auto; padding: 20px; text-align: left;">
                <h3 style="margin-top: 0; text-align: center;">Synthèse Métrique</h3>
                <p style="font-size: 9pt; color: var(--text-muted); margin-bottom: 0; text-align: justify; line-height: 1.5;">
                    Ce recueil de données consolidées dresse l'état des lieux de la distribution numérique hôtelière (OTAs) et de l'évolution réglementaire des labels de tourisme durable et de qualité en France et en Europe sur la décennie 2013-2024. Il sert de cadre de référence pour justifier les arbitrages de distribution.
                </p>
            </div>

            <div class="author-box">
                <div class="author-name">JULIEN FLORENCE</div>
                <div class="author-role">Directeur du Développement Stratégique</div>
                <div style="margin-top: 10px; font-size: 8pt; color: var(--text-muted);">DOSSIER DE VEILLE - SOUTENANCE 2026</div>
            </div>
        </div>
        <div class="footer">
            <div style="color: var(--gold);">EDITION PRESTIGE</div>
            <div class="page-number">01</div>
        </div>
    </div>

    <!-- PAGE 2 : ANALYSE OTAs & LABELS -->
    <div class="page">
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content">
            <h1>1. La Pression des OTAs & Labels</h1>
            
            <h2>L'Hégémonie des OTAs (2013 - 2024)</h2>
            <p>
                La distribution hôtelière en Europe a subi une mutation numérique structurelle. Les plateformes de réservation en ligne (OTAs) ont vu leur part de marché passer de <strong>19,7% en 2013</strong> à <strong>29,6% en 2023</strong>. Ce quasi-monopole de distribution est dominé par <strong>Booking Holdings</strong>, qui capte <strong>71% de parts de marché en Europe</strong>, suivi d'Expedia Group (14,4%). En France, la dépendance reste forte avec 27,6% des réservations captées par les OTAs dès 2019. 
            </p>
            <p>
                Cette intermédiation forcée pèse lourdement sur les exploitants indépendants. Booking.com génère à lui seul 43% du chiffre d'affaires en ligne des hôtels en Europe, prélevant des commissions systématiques de 15% à 25% qui amputent directement l'EBE des hébergeurs.
            </p>

            <h2>La Révolution Verte des Labels (2014 - 2025)</h2>
            <p>
                Parallèlement à l'étau numérique des OTAs, les hébergeurs font face à une pression environnementale et réglementaire. Le label historique de l'État <strong>"Qualité Tourisme"</strong> (créé en 2005) a vu ses attributions s'arrêter définitivement le 31 août 2024, au profit du nouveau label <strong>"Destination d'Excellence"</strong>. Ce dernier intègre des critères stricts d'éco-responsabilité et d'accessibilité.
            </p>
            <p>
                En réponse aux nouvelles attentes des voyageurs, les certifications éco-responsables explosent. Le label international <strong>"Clef Verte"</strong> est ainsi passé de <strong>855 établissements en 2022</strong> à une projection de <strong>2 428 établissements en 2025</strong>, soit une hausse spectaculaire de 45% par an, démontrant l'obligation pour l'hôtellerie de charme de matérialiser ses engagements durables.
            </p>
        </div>
        <div class="footer">
            <div style="color: var(--gold);">EDITION PRESTIGE</div>
            <div class="page-number">02</div>
        </div>
    </div>

    <!-- PAGE 3 : TABLEAU BENCHMARK -->
    <div class="page">
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content">
            <h1>2. Tableau de Synthèse Comparative</h1>
            
            <table>
                <thead>
                    <tr>
                        <th style="width: 8%;">Année</th>
                        <th style="width: 10%;">Axe</th>
                        <th style="width: 12%;">Zone</th>
                        <th style="width: 40%;">Indicateur de Performance</th>
                        <th style="width: 10%;">Valeur</th>
                        <th style="width: 20%;">Source Officielle</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>2013</td><td>OTA</td><td>Europe</td><td>Part de marché des OTAs dans la distribution hôtelière</td><td>19,7%</td><td class="source-tag">HOTREC Study 2013</td></tr>
                    <tr><td>2015</td><td>OTA</td><td>Europe</td><td>Part de marché des OTAs (nuitées cumulées)</td><td>22.0%</td><td class="source-tag">Eurostat Tourism</td></tr>
                    <tr><td>2016</td><td>OTA</td><td>France</td><td>Voyageurs réservant via une plateforme OTA</td><td>44.0%</td><td class="source-tag">Baromètre Numérique</td></tr>
                    <tr><td>2016</td><td>OTA</td><td>France</td><td>Français réservant leur voyage en ligne</td><td>72.0%</td><td class="source-tag">Baromètre Numérique</td></tr>
                    <tr><td>2019</td><td>OTA</td><td>Europe</td><td>Part de marché des OTAs dans la distribution hôtelière</td><td>29.2%</td><td class="source-tag">HOTREC Study 2019</td></tr>
                    <tr><td>2019</td><td>OTA</td><td>France</td><td>Part de marché des OTAs dans la distribution hôtelière</td><td>27.6%</td><td class="source-tag">Coach Omnium</td></tr>
                    <tr><td>2021</td><td>OTA</td><td>Europe</td><td>Part de marché des OTAs dans la distribution hôtelière</td><td>28.8%</td><td class="source-tag">HOTREC Study 2021</td></tr>
                    <tr><td>2023</td><td>OTA</td><td>Europe</td><td>Part de marché des OTAs dans la distribution hôtelière</td><td>29.6%</td><td class="source-tag">HOTREC / Phocuswright</td></tr>
                    <tr><td>2023</td><td>OTA</td><td>Europe</td><td>Poids de Booking Holdings dans le marché OTA européen</td><td>71.0%</td><td class="source-tag">HOTREC Study 2023</td></tr>
                    <tr><td>2023</td><td>OTA</td><td>Europe</td><td>Poids d'Expedia Group dans le marché OTA européen</td><td>14.4%</td><td class="source-tag">HOTREC Study 2023</td></tr>
                    <tr><td>2024</td><td>OTA</td><td>Europe</td><td>Poids de Booking.com dans le marché OTA européen</td><td>69.3%</td><td class="source-tag">HOTREC / D-EDGE</td></tr>
                    <tr><td>2024</td><td>OTA</td><td>Mondial</td><td>Volume du marché mondial des OTAs (Milliards $)</td><td>253.2</td><td class="source-tag">Statista Report 2024</td></tr>
                    <tr><td>2024</td><td>OTA</td><td>Loisirs</td><td>Part des OTAs dans les revenus des loisirs</td><td>18.0%</td><td class="source-tag">Phocuswright B2B</td></tr>
                    <tr><td>2022</td><td>Label</td><td>France</td><td>Nombre d'établissements labellisés Clef Verte</td><td>855</td><td class="source-tag">Teragir / Clef Verte</td></tr>
                    <tr><td>2023</td><td>Label</td><td>France</td><td>Nombre d'établissements labellisés Clef Verte</td><td>1077</td><td class="source-tag">Teragir / Clef Verte</td></tr>
                    <tr><td>2024</td><td>Label</td><td>France</td><td>Nombre d'établissements labellisés Clef Verte</td><td>1564</td><td class="source-tag">Teragir / Clef Verte</td></tr>
                    <tr><td>2025</td><td>Label</td><td>France</td><td>Projection établissements labellisés Clef Verte</td><td>2428</td><td class="source-tag">Teragir / Clef Verte</td></tr>
                    <tr><td>2013</td><td>Label</td><td>France</td><td>Nombre d'établissements Qualité Tourisme</td><td>5600</td><td class="source-tag">DGE Statistiques</td></tr>
                    <tr><td>2021</td><td>Label</td><td>France</td><td>Nombre d'établissements Qualité Tourisme</td><td>4000</td><td class="source-tag">Ministère Économie</td></tr>
                    <tr><td>2024</td><td>Label</td><td>France</td><td>Nombre d'établissements Qualité Tourisme</td><td>5000</td><td class="source-tag">DGE Bilan 2024</td></tr>
                    <tr><td>2024</td><td>Label</td><td>France</td><td>Fin des attributions Qualité Tourisme</td><td>31 Aoû</td><td class="source-tag">Décret d'application</td></tr>
                    <tr><td>2024</td><td>Label</td><td>France</td><td>Lancement "Destination d'Excellence" (labellisés)</td><td>203</td><td class="source-tag">DGE Septembre 2024</td></tr>
                    <tr><td>2026</td><td>Label</td><td>France</td><td>Disparition définitive de la marque Qualité Tourisme</td><td>31 Déc</td><td class="source-tag">Décret d'application</td></tr>
                    <tr><td>2024</td><td>Label</td><td>Europe</td><td>Nombre de produits/services certifiés Écolabel Européen</td><td>98 977</td><td class="source-tag">Commission Européenne</td></tr>
                </tbody>
            </table>
        </div>
        <div class="footer">
            <div style="color: var(--gold);">EDITION PRESTIGE</div>
            <div class="page-number">03</div>
        </div>
    </div>

</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] HTML généré dans : {html_path}")

async def compile_pdf(html_path, pdf_path):
    from playwright.async_api import async_playwright
    print(f"[*] Compilation PDF via Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 720})
        page = await context.new_page()
        
        try:
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            await page.wait_for_timeout(2000) 
            await page.pdf(
                path=pdf_path,
                format="A4",
                print_background=True,
                display_header_footer=False,
                margin={"top": "0mm", "right": "0mm", "bottom": "0mm", "left": "0mm"},
                prefer_css_page_size=True
            )
            print(f"[OK] PDF généré avec succès dans : {pdf_path}")
        except Exception as e:
            print(f"[ERREUR] Échec de la génération PDF : {str(e)}")
            sys.exit(1)
        finally:
            await browser.close()

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.normpath(os.path.join(base_path, ".."))
    
    csv_path = os.path.join(project_path, "Data", "labels_otas_tourisme_10ans.csv")
    html_path = os.path.join(project_path, "HTML", "labels_otas_tourisme_10ans.html")
    pdf_path = os.path.join(project_path, "PDF", "labels_otas_tourisme_10ans.pdf")
    
    generate_csv(csv_path)
    generate_html(html_path)
    
    try:
        asyncio.run(compile_pdf(html_path, pdf_path))
    except KeyboardInterrupt:
        print("\nArrêt par l'utilisateur.")

if __name__ == "__main__":
    main()
