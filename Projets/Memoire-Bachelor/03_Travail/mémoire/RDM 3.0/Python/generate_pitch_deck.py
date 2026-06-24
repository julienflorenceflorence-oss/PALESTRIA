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
        <div class="slide active">
            <div class="label" style="margin-bottom: 2vh; color: var(--gold); font-size: 1.2vw;">CONSULTING STRATÉGIQUE & INGÉNIERIE COMMERCIALE</div>
            <h1 class="big-title">HAPPY HOUSE</h1>
            <div style="width: 15vw; height: 2px; background: var(--gold); margin: 2vh 0 4vh 0;"></div>
            <h2 class="cinzel text-gold" style="font-size: 2.2vw; font-weight: 400; letter-spacing: 4px; margin-bottom: 6vh; text-align: center;">LE PIVOT DE LA PÉRENNITÉ</h2>
            
            <div style="text-align: center; margin-top: 4vh;">
                <p style="font-size: 1.6vw; font-weight: 700; letter-spacing: 4px; color: #FFF;">JULIEN FLORENCE</p>
                <p style="font-size: 1.1vw; color: #777; margin-top: 1.5vh; letter-spacing: 2px;">DIRECTEUR DU DÉVELOPPEMENT STRATÉGIQUE</p>
                <p style="font-size: 0.9vw; color: #555; margin-top: 1vh; letter-spacing: 3px;">VALIDATION MASTER (A150) — ROCKET SCHOOL</p>
            </div>
        </div>

        <!-- SLIDE 2 : PROBLÉMATIQUE & HYPOTHÈSE -->
        <div class="slide">
            <h2 class="subtitle">Problématique & Hypothèse</h2>
            <div class="grid-2" style="margin-top: 2vh; align-items: stretch;">
                <div class="card border-red" style="text-align: left;">
                    <div class="label" style="color: var(--red); margin-bottom: 2vh;">Le Défi SMART (2026)</div>
                    <h3 class="cinzel" style="font-size: 1.8vw; margin-bottom: 3vh; color: #FFF; line-height: 1.4;">
                        Comment structurer un modèle commercial capable de réduire le CAC, de verrouiller la rétention et de croître sans autre budget que nos salaires ?
                    </h3>
                    <p style="font-size: 1.1vw; color: #999; line-height: 1.6;">
                        • Cibler l'efficience opérationnelle<br>
                        • Mettre fin aux processus manuels et diffus<br>
                        • Financer le développement sur la trésorerie
                    </p>
                </div>
                <div class="card border-green" style="text-align: left; background: rgba(46, 204, 113, 0.03);">
                    <div class="label" style="color: var(--green); margin-bottom: 2vh;">L'Hypothèse Arithmétique</div>
                    <h3 class="cinzel" style="font-size: 1.8vw; margin-bottom: 3vh; color: #FFF; line-height: 1.4;">
                        La croissance ne dépend pas de l'intensité de l'effort humain, mais de la qualification en amont et de la valeur en aval.
                    </h3>
                    <p style="font-size: 1.1vw; color: #999; line-height: 1.6;">
                        • **Qualification IA** : Zéro coût d'outillage direct<br>
                        • **Coût-Killing B2B** : Valeur immédiate via centrale d'achat<br>
                        • **Dashboard ROI** : Matérialisation de la preuve
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

        <!-- SLIDE 4 : LE DIAGNOSTIC INTERNE -->
        <div class="slide">
            <h2 class="subtitle text-red" style="border-color: rgba(231,76,60,0.25);">Diagnostic Interne : Le Double Effondrement</h2>
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

        <!-- SLIDE 5 : LE PIVOT STRATÉGIQUE -->
        <div class="slide">
            <h2 class="subtitle">Le Pivot : Rationalisation & Rôles</h2>
            <div class="grid-2" style="margin-top: 2vh;">
                <div class="card border-red" style="text-align: left;">
                    <div class="label" style="color: var(--red); margin-bottom: 1.5vh;">Ancien Modèle (Déficitaire)</div>
                    <h3 class="cinzel" style="font-size: 1.4vw; color: #FFF; margin-bottom: 2vh;">Prospection Téléphonique Cold Calling</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **Coût unitaire SDR** : 1 823 € par signature.<br>
                        • **Cible** : Listing brut et non-qualifié.<br>
                        • **Positionnement** : Outil commercial de visibilité incertaine.
                    </p>
                </div>
                <div class="card border-green" style="text-align: left; background: rgba(46,204,113,0.02);">
                    <div class="label" style="color: var(--green); margin-bottom: 1.5vh;">Nouveau Modèle (Viable)</div>
                    <h3 class="cinzel" style="font-size: 1.4vw; color: #FFF; margin-bottom: 2vh;">Inbound Qualifié & Rétention Financière</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **Canal d'Acquisition** : Afterworks régionaux (CPA cible : 166 €).<br>
                        • **Proposition de valeur** : Centrale d'achat & Cost-killing direct.<br>
                        • **Sécurisation** : Onboarding axé usage & Suivi Dashboard.
                    </p>
                </div>
            </div>
            <div class="card" style="width: 100%; max-width: 1300px; margin-top: 4vh; border-color: var(--gold); padding: 1.5vw; text-align: left;">
                <div class="label" style="color: var(--gold); margin-bottom: 1vh;">Synergie du Binôme : Répartition Rigoureuse</div>
                <p style="font-size: 1.1vw; color: #DDD;">
                    • **Ruddy Marie-Luce** : Trafic voyageur, SEO & Génération de demande organique à coût zéro.<br>
                    • **Julien Florence** : Structuration de l'offre B2B, négociation grand compte, automatisation IA & Rétention.
                </p>
            </div>
        </div>

        <!-- SLIDE 6 : L'INGÉNIERIE ACQUISITION DATA -->
        <div class="slide">
            <h2 class="subtitle">Qualification Data : n8n & Gemini AI</h2>
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
                    <p style="font-size: 0.9vw; color: #888; margin-top: 1vh;">Filtrage et scoring automatique Loi ALUR & DPE.</p>
                </div>
                <div class="workflow-arrow">➔</div>
                <div class="card workflow-step" style="border-color: var(--green); background: rgba(46,204,113,0.02);">
                    <div class="label" style="margin-bottom: 1vh; color: var(--green);">3. Leads Actionnables</div>
                    <h3 class="cinzel text-green" style="font-size: 1.4vw;">Google Sheets</h3>
                    <p style="font-size: 0.9vw; color: #888; margin-top: 1vh;">Base VIP pour ciblage prioritaire des afterworks.</p>
                </div>
            </div>
            <div class="grid-2 mt-4" style="max-width: 1200px;">
                <div class="border-gold" style="text-align: left;">
                    <h4 style="font-size: 1.1vw; color: #FFF;">Sourcing Inbound Ciblé</h4>
                    <p style="font-size: 0.95vw; color: #888; margin-top: 0.5vh;">Nos équipes n'interviennent que sur des prospects dont la maturité et les besoins de conformité réglementaire sont scientifiquement qualifiés.</p>
                </div>
                <div class="border-green" style="text-align: left;">
                    <h4 style="font-size: 1.1vw; color: #FFF;">Coût d'infrastructure direct</h4>
                    <p style="font-size: 0.95vw; color: #888; margin-top: 0.5vh;">**0 € de coût récurrent d'outillage**. Exploitation d'outils open source gratuits et d'API à faible coût marginal par exécution.</p>
                </div>
            </div>
        </div>

        <!-- SLIDE 7 : RÉTENTION & CENTRALE D'ACHAT ENTEGRA -->
        <div class="slide">
            <h2 class="subtitle">Le Levier Rétention : Centrale Entegra</h2>
            <div class="label" style="margin-bottom: 2vh; color: var(--gold);">Étude de cas pilote : Domaine de la Preuve</div>
            <div class="grid-3" style="align-items: stretch;">
                <div class="card border-red" style="display: flex; flex-direction: column; justify-content: center;">
                    <div class="label text-red">Investissement Hébergeur</div>
                    <div class="cinzel" style="font-size: 3.5vw; color: var(--red); font-weight: bold; margin: 1.5vh 0;">360&nbsp;€</div>
                    <div class="label" style="color: #FFF;">Cotisation Annuelle HT</div>
                </div>
                <div class="card border-green" style="grid-column: span 2; text-align: left; background: rgba(46,204,113,0.02);">
                    <div class="label text-green" style="margin-bottom: 1.5vh;">Économies Opérationnelles Réelles Négociées</div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2vw;">
                        <div>
                            <h4 style="color: #FFF; font-size: 1.1vw;">F&B (Alimentaire)</h4>
                            <p style="font-size: 1.8vw; color: var(--green); font-weight: 700; margin: 0.5vh 0;">- 2&nbsp;145&nbsp;€</p>
                            <p style="font-size: 0.9vw; color: #888;">(Gain de 15% sur 14 300 € d'achats)</p>
                        </div>
                        <div>
                            <h4 style="color: #FFF; font-size: 1.1vw;">Blanchisserie & Gaz</h4>
                            <p style="font-size: 1.8vw; color: var(--green); font-weight: 700; margin: 0.5vh 0;">- 910&nbsp;€</p>
                            <p style="font-size: 0.9vw; color: #888;">(Gain négocié avec nos prestataires régionaux)</p>
                        </div>
                    </div>
                    <div style="border-top: 1px solid rgba(255,255,255,0.1); margin-top: 2vh; padding-top: 1.5vh; display: flex; justify-content: space-between; align-items: center;">
                        <span class="cinzel text-gold" style="font-size: 1.3vw;">Gain Net Annuel : + 3&nbsp;055&nbsp;€</span>
                        <span class="label text-green" style="font-size: 0.9vw;">ROI Client : 8,5x la cotisation</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- SLIDE 8 : PREUVE DE PERFORMANCE (DASHBOARD ROI) -->
        <div class="slide">
            <h2 class="subtitle">Preuve de Performance : Dashboard ROI</h2>
            <div class="card" style="width: 100%; max-width: 1100px; text-align: left; padding: 2.5vw; border-color: var(--gold); background: #13151D;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 2vh; margin-bottom: 3vh;">
                    <div>
                        <span class="label" style="color: var(--gold);">Suivi du Retour sur Investissement</span>
                        <h3 class="cinzel" style="color: #FFF; font-size: 1.8vw; margin-top: 0.5vh;">DOMAINE DE LA PREUVE</h3>
                    </div>
                    <div style="background: rgba(46,204,113,0.15); border: 1px solid var(--green); color: var(--green); padding: 5px 15px; border-radius: 20px; font-size: 0.9vw; font-weight: bold; letter-spacing: 1px;">
                        ADHÉSION ACTIVÉE & RENTABILISÉE
                    </div>
                </div>
                
                <div class="grid-3">
                    <div style="border-right: 1px solid rgba(255,255,255,0.1); padding-right: 1vw;">
                        <span class="label">Cotisation payée</span>
                        <p class="cinzel text-red" style="font-size: 2.5vw; font-weight: 700; margin-top: 1vh;">- 360&nbsp;€</p>
                    </div>
                    <div style="border-right: 1px solid rgba(255,255,255,0.1); padding-right: 1vw; padding-left: 1vw;">
                        <span class="label">Économies cumulées (Entegra)</span>
                        <p class="cinzel text-green" style="font-size: 2.5vw; font-weight: 700; margin-top: 1vh;">+ 3&nbsp;055&nbsp;€</p>
                    </div>
                    <div style="padding-left: 1vw;">
                        <span class="label">Valeur Résas Directes</span>
                        <p class="cinzel text-green" style="font-size: 2.5vw; font-weight: 700; margin-top: 1vh;">+ 1&nbsp;200&nbsp;€</p>
                    </div>
                </div>
                
                <div style="border-top: 1px solid rgba(255,255,255,0.1); margin-top: 3vh; padding-top: 2vh; display: flex; justify-content: space-between; align-items: center;">
                    <span class="label" style="color: #888;">Gains cumulés Happy House : <strong>4 255 €</strong></span>
                    <span class="cinzel text-gold" style="font-size: 1.6vw; font-weight: bold;">Indice ROI Global : 11,8x</span>
                </div>
            </div>
        </div>

        <!-- SLIDE 9 : PLAN M12, BUDGET & GOUVERNANCE RSE -->
        <div class="slide">
            <h2 class="subtitle">Plan d'Action M12 & Sécurisation</h2>
            <div class="grid-2" style="margin-top: 2vh;">
                <div class="card border-gold" style="text-align: left;">
                    <div class="label" style="color: var(--gold); margin-bottom: 1.5vh;">Budget & Actions M12</div>
                    <h3 class="cinzel" style="font-size: 1.5vw; color: #FFF; margin-bottom: 2vh;">3&nbsp;500&nbsp;€ réalloués</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **Financement** : Suppression des charges SDR.<br>
                        • **Actions** : Organisation de 6 Afterworks locaux VIP.<br>
                        • **Frais** : Location de lieux, communication, serveurs n8n.
                    </p>
                </div>
                <div class="card border-red" style="text-align: left;">
                    <div class="label" style="color: var(--red); margin-bottom: 1.5vh;">Triggers de Risque & COPIL</div>
                    <h3 class="cinzel" style="font-size: 1.5vw; color: #FFF; margin-bottom: 2vh;">Règles de Pilotage strictes</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • **Alerte CPA** : Si CPA > 200 €, analyse corrective d'urgence.<br>
                        • **Plan de Contingence** : Si 2ème échec consécutif, arrêt immédiat du canal afterwork et focus sur la rétention pure.
                    </p>
                </div>
            </div>
            <div class="card" style="width: 100%; max-width: 1300px; margin-top: 4vh; border-color: rgba(46,204,113,0.3); padding: 1.5vw; text-align: left; background: rgba(46,204,113,0.01);">
                <div class="label" style="color: var(--green); margin-bottom: 1vh;">Gouvernance & Intégration RSE</div>
                <p style="font-size: 1.1vw; color: #DDD;">
                    • **Loi ALUR** : Validation stricte des dossiers d'adhésion pour éliminer les risques de non-conformité administrative.<br>
                    • **Approvisionnement Responsable** : Réduction carbone via le groupement régional de fournisseurs Entegra.
                </p>
            </div>
        </div>

        <!-- SLIDE 10 : CONCLUSION & BILAN PERSONNEL -->
        <div class="slide">
            <h2 class="subtitle">Conclusion & Bilan Personnel</h2>
            <div class="grid-2" style="margin-top: 2vh; align-items: stretch;">
                <div class="card border-gold" style="text-align: left;">
                    <div class="label" style="color: var(--gold); margin-bottom: 1.5vh;">Maturité Acquise</div>
                    <h3 class="cinzel" style="font-size: 1.5vw; color: #FFF; margin-bottom: 2vh;">Directeur du Développement Stratégique</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • Rigueur analytique face aux *unit economics* B2B.<br>
                        • Compétences de négociation grand compte (Partenariat Entegra).<br>
                        • Conception d'architectures d'automatisation IA (no-code / API).
                    </p>
                </div>
                <div class="card border-green" style="text-align: left; background: rgba(46, 204, 113, 0.02);">
                    <div class="label" style="color: var(--green); margin-bottom: 1.5vh;">La Suite (Horizon 2028)</div>
                    <h3 class="cinzel" style="font-size: 1.5vw; color: #FFF; margin-bottom: 2vh;">Direction du Développement — PalestrIA</h3>
                    <p style="font-size: 1vw; color: #999; line-height: 1.6;">
                        • Leadership d'affaires sur des stratégies B2B Premium.<br>
                        • Synergie opérationnelle poussée entre l'Intelligence Artificielle et le commerce de relations.<br>
                        • Résolution de problèmes complexes sous contrainte budgétaire.
                    </p>
                </div>
            </div>
            
            <div style="width: 100%; text-align: center; margin-top: 5vh;">
                <p style="font-size: 1.4vw; font-weight: 200; font-family: 'Cinzel', serif; letter-spacing: 2px;">
                    "L'HUMAIN SANS LA TECHNOLOGIE EST SA PROPRE LIMITE DE CROISSANCE... MAIS LA TECHNOLOGIE SANS L'HUMAIN MANQUE D'EFFICIENCE."
                </p>
            </div>
        </div>

        <!-- OVERLAYS -->
        <div class="slide-counter"><span id="current-slide">1</span> / 10</div>
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
