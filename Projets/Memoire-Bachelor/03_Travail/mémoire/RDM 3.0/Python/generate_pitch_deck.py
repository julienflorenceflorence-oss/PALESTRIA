import os
import asyncio
import sys

# Tentative d'import de Playwright
try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Playwright n'est pas installé. L'export PDF sera ignoré.")
    print("Exécutez : pip install playwright && playwright install chromium")

html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PITCH DECK - JULIEN FLORENCE - SOUTENANCE A150</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Montserrat:wght@200;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --gold: #D4AF37;
            --black: #0F1115;
            --dark-gray: #191B24;
            --card-bg: rgba(25, 27, 36, 0.6);
            --text-light: #F4F4F4;
            --red: #E74C3C;
            --green: #2ECC71;
            --border-color: rgba(212, 175, 55, 0.25);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--black);
            color: var(--text-light);
            overflow: hidden; /* Prevent scrolling, it's a presentation */
        }

        #presentation-container {
            width: 100vw;
            height: 100vh;
            position: relative;
        }

        .slide {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
            pointer-events: none;
            padding: 5% 8%;
        }

        .slide.active {
            opacity: 1;
            pointer-events: auto;
            z-index: 10;
        }

        /* --- TYPOGRAPHY --- */
        h1, h2, h3, .cinzel { font-family: 'Cinzel', serif; }
        
        .huge-number {
            font-family: 'Cinzel', serif;
            font-size: 8vw;
            font-weight: 900;
            color: var(--gold);
            line-height: 1;
            text-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
        }

        .big-title {
            font-size: 4vw;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            margin-bottom: 2vh;
            text-align: center;
            color: #FFF;
        }

        .subtitle {
            font-size: 1.8vw;
            color: var(--gold);
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 4vh;
            font-weight: 400;
            text-align: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1.5vh;
            width: 80%;
        }

        .label {
            font-size: 1.1vw;
            color: #888;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            font-weight: 600;
        }

        /* --- LAYOUTS & COMPONENTS --- */
        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4vw;
            width: 100%;
            max-width: 1300px;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 2.5vw;
            width: 100%;
            max-width: 1400px;
        }

        .card {
            border: 1px solid var(--border-color);
            padding: 2.5vw;
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border-radius: 4px;
            text-align: center;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: var(--gold);
        }

        .border-gold { border-left: 5px solid var(--gold); padding-left: 2vw; }
        .border-red { border-left: 5px solid var(--red); padding-left: 2vw; }
        .border-green { border-left: 5px solid var(--green); padding-left: 2vw; }

        .progress-bar {
            width: 100vw; height: 5px;
            background: #222;
            position: absolute; bottom: 0; left: 0;
            z-index: 100;
        }
        .progress-fill {
            height: 100%; background: var(--gold); width: 0%;
            transition: width 0.3s linear;
        }

        .slide-counter {
            position: absolute; bottom: 2vh; right: 3vw;
            font-family: 'Cinzel', serif; color: #555; font-size: 1vw;
            z-index: 100;
            letter-spacing: 2px;
        }

        /* Helpers */
        .text-gold { color: var(--gold); }
        .text-red { color: var(--red); }
        .text-green { color: var(--green); }
        .mt-2 { margin-top: 2vh; } 
        .mt-4 { margin-top: 4vh; }
        .font-weight-light { font-weight: 200; }
        .font-weight-bold { font-weight: 700; }
        
        /* Workflow layout specific */
        .workflow-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            max-width: 1200px;
            margin-top: 2vh;
        }
        .workflow-step {
            width: 28%;
            position: relative;
        }
        .workflow-arrow {
            width: 8%;
            font-size: 3vw;
            color: var(--gold);
            text-align: center;
        }

        /* --- STYLES D'IMPRESSION (PAYSAGE A4) --- */
        @page {
            size: A4 landscape;
            margin: 0;
        }
        @media print {
            * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
            body { overflow: visible !important; background-color: var(--black) !important; }
            #presentation-container { height: auto !important; }
            .slide {
                position: relative !important;
                display: flex !important;
                opacity: 1 !important;
                pointer-events: auto !important;
                page-break-after: always !important;
                break-after: page !important;
                width: 297mm !important;
                height: 210mm !important;
                padding: 15mm !important;
            }
            .slide-counter, .progress-bar { display: none !important; }
            .card { padding: 15px !important; }
        }

    </style>
</head>
<body>

    <div id="presentation-container">

        <!-- SLIDE 1 : COUVERTURE -->
        <div class="slide active" style="padding: 0; flex-direction: row; align-items: stretch; justify-content: stretch;">
            <!-- Left Panel: Content -->
            <div style="flex: 1.2; background: var(--black); display: flex; flex-direction: column; justify-content: center; align-items: flex-start; padding: 5% 6%; border-right: 1px solid var(--border-color); z-index: 2; position: relative;">
                <div class="label" style="margin-bottom: 2vh; color: var(--gold); font-size: 1.1vw; text-align: left;">AUDIT COMMERCIAL &amp; BLOCAGE ORGANISATIONNEL</div>
                <h1 class="big-title" style="text-align: left; font-size: 3.8vw; margin-bottom: 1vh; line-height: 1.1; letter-spacing: 0.1em; color: #FFF;">HAPPY HOUSE</h1>
                <div style="width: 10vw; height: 2px; background: var(--gold); margin: 2vh 0 3vh 0;"></div>
                <h2 class="cinzel text-gold" style="font-size: 1.6vw; font-weight: 400; letter-spacing: 3px; margin-bottom: 6vh; text-align: left; line-height: 1.4;">
                    LA RÉSISTANCE AU PIVOT STRATÉGIQUE
                </h2>
                
                <div style="border-top: 1px solid rgba(255,255,255,0.05); padding-top: 3vh; width: 100%;">
                    <p style="font-size: 1.4vw; font-weight: 700; letter-spacing: 3px; color: #FFF; margin-bottom: 0.5vh;">JULIEN FLORENCE</p>
                    <p style="font-size: 0.9vw; color: #888; margin-top: 0.5vh; letter-spacing: 1px;">DIRECTEUR DU DÉVELOPPEMENT STRATÉGIQUE</p>
                    <p style="font-size: 0.75vw; color: #555; margin-top: 0.5vh; letter-spacing: 2px;">VALIDATION MASTER (A150) — ROCKET SCHOOL</p>
                </div>
            </div>
            <!-- Right Panel: Image -->
            <div style="flex: 1; background: url('Images/LFDB_004.jpg') no-repeat center center; background-size: cover; position: relative;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(to right, rgba(15, 17, 21, 0.4) 0%, rgba(15, 17, 21, 0.0) 100%);"></div>
                <div style="position: absolute; left: 0; top: 0; bottom: 0; width: 1px; background: var(--gold); box-shadow: 0 0 15px var(--gold);"></div>
            </div>
        </div>

        <!-- SLIDE 2 : PROBLÉMATIQUE & RÉSISTANCE -->
        <div class="slide">
            <h2 class="subtitle">Problématique &amp; Friction Directeur</h2>
            <div class="grid-2" style="margin-top: 2vh; align-items: stretch;">
                <div class="card border-red" style="text-align: left;">
                    <div class="label" style="color: var(--red); margin-bottom: 2vh;">La Question Centrale</div>
                    <h3 class="cinzel" style="font-size: 1.6vw; margin-bottom: 3vh; color: #FFF; line-height: 1.4;">
                        Comment recommander un modèle de rupture commerciale face aux unit economics quand la direction refuse le changement opérationnel ?
                    </h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **Arbitrages bloqués** par Patrice (Dir. Général)<br>
                        • **Crainte du changement** : attachement au modèle relationnel historique<br>
                        • **Inaction** : maintien de l'outbound SDR traditionnel
                    </p>
                </div>
                <div class="card border-gold" style="text-align: left; background: rgba(212, 175, 55, 0.02);">
                    <div class="label" style="color: var(--gold); margin-bottom: 2vh;">Le Post-Mortem de l'Alternant</div>
                    <h3 class="cinzel" style="font-size: 1.6vw; margin-bottom: 3vh; color: #FFF; line-height: 1.4;">
                        L'ingénierie d'affaires ne se limite pas à la donnée. Elle se heurte à la politique et à la gouvernance d'entreprise.
                    </h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • Conception de **prototypes fonctionnels** validés<br>
                        • Devoir d'alerte et de recommandation face au crash comptable<br>
                        • Analyse objective de la résistance organisationnelle
                    </p>
                </div>
            </div>
        </div>

        <!-- SLIDE 3 : LE DIAGNOSTIC EXTERNE -->
        <div class="slide">
            <h2 class="subtitle">Diagnostic Externe : La Double Pression</h2>
            <div class="grid-3" style="margin-top: 2vh;">
                <div class="card border-red">
                    <div class="huge-number text-red" style="font-size: 5vw;">71%</div>
                    <div class="label mt-2" style="color: #FFF;">Le Monopole Booking.com</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.6;">
                        Booking capte 71 % du marché hôtelier européen en prélevant 15 % à 25 % de commissions directes sur la marge brute.
                    </p>
                </div>
                <div class="card border-gold">
                    <div class="huge-number text-gold" style="font-size: 5vw;">ALUR</div>
                    <div class="label mt-2" style="color: #FFF;">La Contrainte Légale</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.6;">
                        Menace d'interdiction de louer sur les DPE non-conformes et loi "anti-Airbnb" forçant à professionnaliser le secteur.
                    </p>
                </div>
                <div class="card border-green">
                    <div class="huge-number text-green" style="font-size: 5vw;">+45%</div>
                    <div class="label mt-2" style="color: #FFF;">Transition Verte</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.6;">
                        Explosion annuelle du label "Clef Verte". Fin de "Qualité Tourisme" au profit du label "Destination d'Excellence".
                    </p>
                </div>
            </div>
            <div class="card" style="width: 100%; max-width: 1400px; margin-top: 4vh; padding: 1.5vw; border-color: rgba(212,175,55,0.15);">
                <p style="font-size: 1.2vw; font-style: italic; color: #AAA; text-align: center;">
                    "L'hébergeur indépendant de charme subit une fatigue administrative et une érosion de ses marges opérationnelles."
                </p>
            </div>
        </div>

        <!-- SLIDE 4 : DOMINATION DES OTAS & FUITE DE MARGES -->
        <div class="slide">
            <h2 class="subtitle">L'Impact Macro : Domination des OTAs &amp; Fuite de Marges</h2>
            <div class="grid-3" style="margin-top: 2vh;">
                <div class="card border-red">
                    <div class="huge-number text-red" style="font-size: 5vw;">71%</div>
                    <div class="label mt-2" style="color: #FFF;">Domination Numérique</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.6;">
                        Part de marché de **Booking Holdings** en Europe. Les OTAs captent 29,6% du marché global des nuitées.
                    </p>
                </div>
                <div class="card border-gold">
                    <div class="huge-number text-gold" style="font-size: 5vw;">-25%</div>
                    <div class="label mt-2" style="color: #FFF;">Marge Perdue Hébergeurs</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.6;">
                        De commission systématique sur le CA. Soit une perte nette de **15k € à 30k €/an** par établissement indépendant.
                    </p>
                </div>
                <div class="card border-red">
                    <div class="huge-number text-red" style="font-size: 5vw;">IS</div>
                    <div class="label mt-2" style="color: #FFF;">Perte Collectivités</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.6;">
                        Optimisation fiscale internationale. Les commissions fuient vers l'étranger, privant les territoires d'investissements locaux.
                    </p>
                </div>
            </div>
            <div class="card" style="width: 100%; max-width: 1400px; margin-top: 4vh; padding: 1.5vw; border-color: var(--border-color); text-align: left;">
                <p style="font-size: 1.1vw; color: #DDD; text-align: center;">
                    **Fuite économique** : Pour 100 € dépensés par un voyageur, **15 € à 25 € quittent définitivement l'économie locale** française.
                </p>
            </div>
        </div>

        <!-- SLIDE 5 : LE DIAGNOSTIC INTERNE -->
        <div class="slide">
            <h2 class="subtitle text-red" style="border-color: rgba(231,76,60,0.25);">Diagnostic Interne : La Preuve du Crash</h2>
            <div class="grid-3" style="margin-top: 2vh;">
                <div class="card border-red">
                    <div class="label text-red">Efficacité Acquisition</div>
                    <div class="cinzel" style="font-size: 4vw; color: var(--red); font-weight: 700; margin: 1vh 0;">0,16</div>
                    <div class="label" style="color: #FFF;">Ratio LTV / CAC</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.5;">
                        CAC Outbound : **1 823 €**<br>
                        ARPU : **226 €/an** | LTV : **290 €**<br>
                        <span style="color: var(--red); font-weight: bold;">Chaque signature détruit 84% de sa valeur.</span>
                    </p>
                </div>
                <div class="card border-red">
                    <div class="label text-red">L'Hémorragie Client</div>
                    <div class="cinzel" style="font-size: 4.2vw; color: var(--red); font-weight: 700; margin: 1vh 0;">80%</div>
                    <div class="label" style="color: #FFF;">Taux de Churn Réel</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.5;">
                        Attrition massive sur la cohorte acquise par téléphone.<br>
                        Manque critique de perception de la valeur après la vente.
                    </p>
                </div>
                <div class="card border-red">
                    <div class="label text-red">Fatigue de la Plateforme</div>
                    <div class="cinzel" style="font-size: 4.2vw; color: var(--red); font-weight: 700; margin: 1vh 0;">5,5%</div>
                    <div class="label" style="color: #FFF;">Usage Commercial Actif</div>
                    <p style="font-size: 1vw; color: #888; margin-top: 2vh; line-height: 1.5;">
                        Seuls **8 hébergeurs sur 146** obtiennent des réservations actives via notre portail.<br>
                        Le reste du parc est inactif.
                    </p>
                </div>
            </div>
        </div>

        <!-- SLIDE 5 : LA RECOMMANDATION DE PIVOT (REJETÉE) -->
        <div class="slide">
            <h2 class="subtitle">La Proposition de Pivot &amp; Le Veto</h2>
            <div class="grid-2" style="margin-top: 2vh;">
                <div class="card border-green" style="text-align: left; background: rgba(46,204,113,0.01);">
                    <div class="label" style="color: var(--green); margin-bottom: 1.5vh;">Notre Recommandation (Julien/Ruddy)</div>
                    <h3 class="cinzel" style="font-size: 1.3vw; color: #FFF; margin-bottom: 2vh;">Inbound Sélectif &amp; Rétention Financière</h3>
                    <p style="font-size: 0.95vw; color: #999; line-height: 1.6;">
                        • **Acquisition** : Afterworks régionaux (CPA cible : 166 €).<br>
                        • **Proposition de valeur** : Centrale Entegra &amp; Cost-killing.<br>
                        • **Fidélisation** : Dashboard de preuve ROI en temps réel.
                    </p>
                </div>
                <div class="card border-red" style="text-align: left; background: rgba(231,76,60,0.01);">
                    <div class="label" style="color: var(--red); margin-bottom: 1.5vh;">La Décision de la Direction (Patrice)</div>
                    <h3 class="cinzel" style="font-size: 1.3vw; color: #FFF; margin-bottom: 2vh;">Refus du Pivot &amp; Maintien du Status Quo</h3>
                    <p style="font-size: 0.95vw; color: #999; line-height: 1.6;">
                        • **Aversion au Risque** : Peur de détruire l'image de relation premium.<br>
                        • **Refus du Cost-Killing** : Incompréhension du levier centrale d'achats.<br>
                        • **Arbitrage** : Poursuite de la prospection SDR traditionnelle.
                    </p>
                </div>
            </div>
            <div class="card" style="width: 100%; max-width: 1300px; margin-top: 4vh; border-color: var(--gold); padding: 1.5vw; text-align: left;">
                <div class="label" style="color: var(--gold); margin-bottom: 1vh;">Constat d'Inaction Opérationnelle</div>
                <p style="font-size: 1.1vw; color: #DDD;">
                    Suite au veto de Patrice, **aucune des transformations B2B préconisées n'a pu être implémentée**. Les processus commerciaux sont restés artisanaux et le CAC outbound est resté à son niveau de perte historique.
                </p>
            </div>
        </div>

        <!-- SLIDE 6 : LE PROTOTYPE DE SOURCING DATA -->
        <div class="slide">
            <h2 class="subtitle">Sourcing Automatisé : Preuve de Concept</h2>
            <div class="workflow-container">
                <div class="card workflow-step" style="border-color: rgba(255,255,255,0.15);">
                    <div class="label" style="margin-bottom: 1vh;">1. Extraction Brute</div>
                    <h3 class="cinzel text-gold" style="font-size: 1.8vw;">126k</h3>
                    <p style="font-size: 0.9vw; color: #888; margin-top: 1vh;">Établissements Sirene hôtellerie en France.</p>
                </div>
                <div class="workflow-arrow">➔</div>
                <div class="card workflow-step" style="border-color: var(--gold);">
                    <div class="label" style="margin-bottom: 1vh; color: var(--gold);">2. Orchestration IA</div>
                    <h3 class="cinzel" style="font-size: 1.4vw; color: #FFF;">n8n + Gemini</h3>
                    <p style="font-size: 0.9vw; color: #888; margin-top: 1vh;">Filtrage et scoring automatique Loi ALUR &amp; DPE.</p>
                </div>
                <div class="workflow-arrow">➔</div>
                <div class="card workflow-step" style="border-color: var(--gold); opacity: 0.5;">
                    <div class="label" style="margin-bottom: 1vh; color: var(--text-light);">3. Prototype Sheets</div>
                    <h3 class="cinzel" style="font-size: 1.4vw; color: #FFF;">Google Sheets</h3>
                    <p style="font-size: 0.9vw; color: #888; margin-top: 1vh;">Base qualifiée de démonstration (non déployée).</p>
                </div>
            </div>
            <div class="grid-2 mt-4" style="max-width: 1200px;">
                <div class="border-gold" style="text-align: left;">
                    <h4 style="font-size: 1.1vw; color: #FFF;">Preuve de Faisabilité Technique</h4>
                    <p style="font-size: 0.95vw; color: #888; margin-top: 0.5vh;">J'ai développé un pipeline fonctionnel sous n8n pour prouver qu'un sourcing qualifié à coût d'outillage direct de **0 €** est possible, malgré le refus de déploiement.</p>
                </div>
                <div class="border-red" style="text-align: left;">
                    <h4 style="font-size: 1.1vw; color: #FFF;">Limitation en Production</h4>
                    <p style="font-size: 0.95vw; color: #888; margin-top: 0.5vh;">Le script n'a pas été connecté au flux commercial, la direction préférant conserver les recherches manuelles et le cold calling à froid.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 : LE LEVIER COLLABORATIF -->
        <div class="slide">
            <h2 class="subtitle">Le Levier Collaboratif : Preuve par le Réseau</h2>
            <div class="label" style="margin-bottom: 2vh; color: var(--gold);">Cas d'école du Domaine de la Preuve (Cas Durentie dans le RDM)</div>
            <div class="grid-3" style="align-items: stretch; margin-top: 2vh;">
                <div class="card border-red" style="display: flex; flex-direction: column; justify-content: center;">
                    <div class="label text-red">Investissement Unique</div>
                    <div class="cinzel" style="font-size: 3.5vw; color: var(--red); font-weight: bold; margin: 1.5vh 0;">360&nbsp;€</div>
                    <div class="label" style="color: #FFF;">Cotisation Annuelle TTC</div>
                </div>
                <div class="card border-green" style="grid-column: span 2; text-align: left; background: rgba(46,204,113,0.02);">
                    <div class="label text-green" style="margin-bottom: 1.5vh;">Transfert Client Collaboratif (Membre-à-Membre)</div>
                    <div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 2vw; align-items: center;">
                        <div>
                            <h4 style="color: #FFF; font-size: 1.1vw;">Mécanisme de Synergie</h4>
                            <p style="font-size: 0.95vw; color: #aaa; margin-top: 1vh; line-height: 1.5;">
                                Un hébergeur membre complet réoriente gratuitement un voyageur haut de gamme vers un autre membre disponible du réseau.
                            </p>
                            <p style="font-size: 0.9vw; color: var(--gold); margin-top: 1vh; font-weight: bold;">
                                ➔ 0 % commission OTAs (Valeur brute 100% conservée)
                            </p>
                        </div>
                        <div>
                            <h4 style="color: #FFF; font-size: 1.1vw;">Réservation Générée</h4>
                            <p style="font-size: 2.2vw; color: var(--green); font-weight: 700; margin: 0.5vh 0;">11&nbsp;000&nbsp;€</p>
                            <p style="font-size: 0.9vw; color: #888;">(En une seule opération)</p>
                        </div>
                    </div>
                    <div style="border-top: 1px solid rgba(255,255,255,0.1); margin-top: 2vh; padding-top: 1.5vh; display: flex; justify-content: space-between; align-items: center;">
                        <span class="cinzel text-gold" style="font-size: 1.3vw;">Rentabilité Immédiate de l'Effet Réseau</span>
                        <span class="label text-green" style="font-size: 0.95vw; font-weight: bold;">ROI Direct : 30,5x l'adhésion</span>
                    </div>
                </div>
            </div>
            <div style="margin-top: 4vh; text-align: center; font-size: 1.1vw; color: var(--red); font-style: italic;">
                *Le cycle de vente initial a duré 5 mois par manque de métriques ROI souveraines, validant le besoin de transparence.*
            </div>
        </div>

        <!-- SLIDE 8 : IMPACT ENTEGRA & SIMULATIONS ROI -->
        <div class="slide">
            <h2 class="subtitle">L'Impact Entegra : Simulations ROI par Profil</h2>
            <div class="label" style="margin-bottom: 2vh; color: var(--gold);">Maquette du Dashboard ROI Conceptuel (Sur la base de la Centrale d'Achats)</div>
            
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5vw; width: 100%; max-width: 1400px; margin-top: 1vh;">
                <!-- Profil 1 -->
                <div class="card border-gold" style="padding: 1.5vw 1vw; text-align: left; background: #13151D;">
                    <div class="label" style="font-size: 0.85vw; color: #888;">Chambre d'hôte (1 ch.)</div>
                    <div class="cinzel" style="font-size: 1.6vw; color: #FFF; font-weight: bold; margin: 1vh 0;">CA 76,6k €</div>
                    <div class="label text-green" style="font-size: 0.9vw;">Gain : +2 292 €/an</div>
                    <p style="font-size: 0.8vw; color: #666; margin-top: 1vh;">(Rentabilité : +9.3% du CA)<br><strong>ROI Cible : 6,3x</strong></p>
                </div>
                <!-- Profil 2 -->
                <div class="card border-gold" style="padding: 1.5vw 1vw; text-align: left; background: #13151D;">
                    <div class="label" style="font-size: 0.85vw; color: #888;">Grand Gîte (8 pers.)</div>
                    <div class="cinzel" style="font-size: 1.6vw; color: #FFF; font-weight: bold; margin: 1vh 0;">CA 36,5k €</div>
                    <div class="label text-green" style="font-size: 0.9vw;">Gain : +1 340 €/an</div>
                    <p style="font-size: 0.8vw; color: #666; margin-top: 1vh;">(Rentabilité : +11.5% du CA)<br><strong>ROI Cible : 3,7x</strong></p>
                </div>
                <!-- Profil 3 -->
                <div class="card border-gold" style="padding: 1.5vw 1vw; text-align: left; background: #13151D;">
                    <div class="label" style="font-size: 0.85vw; color: #888;">Villa Premium (10 pers.)</div>
                    <div class="cinzel" style="font-size: 1.6vw; color: #FFF; font-weight: bold; margin: 1vh 0;">CA 80,3k €</div>
                    <div class="label text-green" style="font-size: 0.9vw;">Gain : +3 581 €/an</div>
                    <p style="font-size: 0.8vw; color: #666; margin-top: 1vh;">(Rentabilité : +11.4% du CA)<br><strong>ROI Cible : 9,9x</strong></p>
                </div>
                <!-- Profil 4 -->
                <div class="card border-green" style="padding: 1.5vw 1vw; text-align: left; background: rgba(46,204,113,0.03);">
                    <div class="label" style="font-size: 0.85vw; color: var(--green);">Vignoble (Hôtel + Resto)</div>
                    <div class="cinzel" style="font-size: 1.6vw; color: #FFF; font-weight: bold; margin: 1vh 0;">CA 1 126k €</div>
                    <div class="label text-green" style="font-size: 0.9vw; font-weight: bold;">Gain : +53 058 €/an</div>
                    <p style="font-size: 0.8vw; color: #666; margin-top: 1vh;">(Rentabilité : +9.4% du CA)<br><strong class="text-gold">ROI Cible : 147x</strong></p>
                </div>
            </div>
            
            <div style="border-top: 1px solid rgba(255,255,255,0.1); margin-top: 3vh; padding-top: 2vh; width: 100%; max-width: 1400px; display: flex; justify-content: space-between; align-items: center;">
                <span class="label" style="color: var(--red);">Dashboard non-déployé en production</span>
                <span class="cinzel text-gold" style="font-size: 1.2vw; font-weight: bold;">Réductions Entegra cibles : 15% à 25% de marge opérationnelle</span>
            </div>
        </div>

        <!-- SLIDE 9 : ANALYSE DU BLOCAGE & COÛT DE L'INACTION -->
        <div class="slide">
            <h2 class="subtitle">Analyse du Blocage &amp; Coût de l'Inaction</h2>
            <div class="grid-2" style="margin-top: 2vh;">
                <div class="card border-red" style="text-align: left;">
                    <div class="label" style="color: var(--red); margin-bottom: 1.5vh;">Les Facteurs du Refus Directeur</div>
                    <h3 class="cinzel" style="font-size: 1.4vw; color: #FFF; margin-bottom: 2vh;">Les Obstacles au Changement</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **Aversion technique** : Peur de complexifier la relation humaine.<br>
                        • **Crainte réglementaire** : Risque perçu sur l'automatisation IA.<br>
                        • **Biais de survie** : Illusion de rentabilité des ventes SDR historiques.
                    </p>
                </div>
                <div class="card border-red" style="text-align: left;">
                    <div class="label" style="color: var(--red); margin-bottom: 1.5vh;">Le Coût de l'Inaction (M12)</div>
                    <h3 class="cinzel" style="font-size: 1.4vw; color: #FFF; margin-bottom: 2vh;">Impact de la Décision Patrice</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **CAC commercial** bloqué à **1 823 €** (Prospection froide).<br>
                        • **Perte nette de marge** : pas d'économies d'échelle Entegra.<br>
                        • **Fidélisation** : Churn maintenu à son niveau critique de **80 %**.
                    </p>
                </div>
            </div>
        </div>

        <!-- SLIDE 10 : CONCLUSION & BILAN PERSONNEL -->
        <div class="slide">
            <h2 class="subtitle">Conclusion &amp; Bilan du Consultant</h2>
            <div class="grid-2" style="margin-top: 2vh; align-items: stretch;">
                <div class="card border-gold" style="text-align: left;">
                    <div class="label" style="color: var(--gold); margin-bottom: 1.5vh;">La Maturité Face au Réel</div>
                    <h3 class="cinzel" style="font-size: 1.5vw; color: #FFF; margin-bottom: 2vh;">Leçons de Conduite du Changement</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • Apprentissage de la **résistance organisationnelle**.<br>
                        • Importance de la négociation et de l'alignement des décideurs.<br>
                        • Capacité à concevoir des architectures techniques autonomes (0€).
                    </p>
                </div>
                <div class="card border-green" style="text-align: left; background: rgba(46, 204, 113, 0.02);">
                    <div class="label" style="color: var(--green); margin-bottom: 1.5vh;">La Suite (Horizon 2028)</div>
                    <h3 class="cinzel" style="font-size: 1.5vw; color: #FFF; margin-bottom: 2vh;">Direction du Développement — PalestrIA</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • Leadership d'affaires sur des stratégies B2B complexes.<br>
                        • Conception d'infrastructures IA adaptées à la culture d'entreprise.<br>
                        • Intégration de la donnée comme outil d'alignement exécutif.
                    </p>
                </div>
            </div>
            
            <div style="width: 100%; text-align: center; margin-top: 5vh;">
                <p style="font-size: 1.3vw; font-weight: 200; font-family: 'Cinzel', serif; letter-spacing: 2px;">
                    "L'HUMAIN SANS LA TECHNOLOGIE EST SA PROPRE LIMITE... MAIS LA TECHNOLOGIE SANS L'HUMAIN SE HEURTE AUX LIMITES DE L'ORGANISATION."
                </p>
            </div>
        </div>

        <!-- OVERLAYS -->
        <div class="slide-counter"><span id="current-slide">1</span> / 11</div>
        <div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
    </div>

    <script>
        const slides = document.querySelectorAll('.slide');
        const counter = document.getElementById('current-slide');
        const progress = document.getElementById('progress');
        let currentIndex = 0;

        function updateSlides() {
            slides.forEach((slide, index) => {
                if(index === currentIndex) {
                    slide.classList.add('active');
                } else {
                    slide.classList.remove('active');
                }
            });
            counter.innerText = currentIndex + 1;
            progress.style.width = ((currentIndex + 1) / slides.length) * 100 + '%';
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'Space' || e.key === 'Enter') {
                if (currentIndex < slides.length - 1) {
                    currentIndex++;
                    updateSlides();
                }
            } else if (e.key === 'ArrowLeft') {
                if (currentIndex > 0) {
                    currentIndex--;
                    updateSlides();
                }
            }
        });

        // Initialize click to next slide for easier presentation mode
        document.getElementById('presentation-container').addEventListener('click', (e) => {
             // Exclude clicks on links or buttons if any
             if (e.target.tagName !== 'A' && e.target.tagName !== 'BUTTON') {
                 if (currentIndex < slides.length - 1) {
                        currentIndex++;
                        updateSlides();
                 }
             }
        });

        updateSlides();
    </script>
</body>
</html>
"""

# Détermination des chemins absolus par rapport au script
script_dir = os.path.dirname(os.path.abspath(__file__))
# base_dir de la soutenance (parent du script) : mémoire/RDM 3.0/
base_dir = os.path.dirname(script_dir) 

# Le fichier HTML doit être écrit dans mémoire/RDM 3.0/PITCH_DECK_PRESTIGE_SOUTENANCE.html
html_path = os.path.join(base_dir, 'PITCH_DECK_PRESTIGE_SOUTENANCE.html')
# Le fichier PDF doit être écrit dans mémoire/presentations/Presentation Pitch Deck.pdf
pdf_path = os.path.normpath(os.path.join(base_dir, '..', 'presentations', 'Presentation Pitch Deck.pdf'))

# S'assurer que le dossier presentations existe
os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

# 1. Écrire le fichier HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"Pitch Deck Ultra-Prestige (HTML Interactive) généré avec succès dans : {html_path}")

# 2. Exporter en PDF avec Playwright
async def export_presentation_to_pdf():
    print(f"Exportation du Pitch Deck en PDF via Playwright...")
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(f"file://{html_path}", wait_until="networkidle")
            
            # Attente de chargement des polices Google
            await page.wait_for_timeout(2000)
            
            await page.pdf(
                path=pdf_path,
                format="A4",
                landscape=True,
                print_background=True,
                margin={
                    "top": "0mm",
                    "right": "0mm",
                    "bottom": "0mm",
                    "left": "0mm",
                }
            )
            await browser.close()
        print(f"[OK] Succès ! Le PDF de la présentation a été mis à jour dans : {pdf_path}")
    except Exception as e:
        print(f"[ERREUR] Impossible de générer le PDF : {e}")

# Lancement de l'export asynchrone
if 'playwright' in sys.modules:
    try:
        asyncio.run(export_presentation_to_pdf())
    except KeyboardInterrupt:
        print("\\nArrêt par l'utilisateur.")
