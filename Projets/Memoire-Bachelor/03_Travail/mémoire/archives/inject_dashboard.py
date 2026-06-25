import re
import os

filename = 'RDM_STRATEGIC_COCKPIT_2026.html'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

dashboardCSS = """
        .dashboard-tile {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 18px !important;
            margin: 0 !important;
            transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: pointer;
            border: 1.5px solid rgba(212, 175, 55, 0.2) !important;
            background: rgba(255, 255, 255, 0.03) !important;
            border-radius: 8px;
            position: relative;
            overflow: hidden;
            z-index: 100;
        }
        .dashboard-tile:hover {
            background: rgba(212, 175, 55, 0.1) !important;
            border-color: #D4AF37 !important;
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.6);
        }
        .tile-status {
            font-size: 7pt;
            letter-spacing: 2px;
            border: 1px solid rgba(255,255,255,0.4);
            padding: 3px 8px;
            width: fit-content;
            margin-bottom: 12px;
            font-weight: 700;
            color: #fff;
        }
        .tile-icon {
            font-size: 26pt;
            color: #D4AF37;
            margin-bottom: 8px;
        }
        .tile-title {
            font-family: 'Cinzel';
            font-weight: 900;
            font-size: 12pt;
            color: #fff;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }
        .tile-desc {
            font-size: 8.5pt;
            line-height: 1.4;
            color: rgba(255,255,255,0.6);
            flex-grow: 1;
        }
        .tile-meta {
            font-size: 7pt;
            font-family: 'Cinzel';
            color: #D4AF37;
            text-align: right;
            margin-top: 15px;
            font-weight: 700;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(3, 1fr);
            gap: 20px;
            z-index: 100;
            flex-grow: 1;
            padding: 10px 0;
            position: relative;
        }
        /* Reset links color for dashboard */
        .dashboard-tile * { text-decoration: none !important; }
"""

# Inject CSS before </style>
content = content.replace('</style>', f"{dashboardCSS}\n    </style>")

dashboardBody = """
    <div class="page" id="p02">
        <div class="cockpit-frame"></div><div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content-body" style="padding: 10px 10px;">
            <h1 style="text-align:center; border-bottom: 2px solid var(--gold); padding-bottom:10px; margin-bottom: 10px;">STRATEGIC CONTROL CENTER</h1>
            <div style="text-align: center; color: var(--gold); letter-spacing: 5px; font-size: 9pt; margin-bottom: 25px; font-weight: 700;">NAVIGUER DANS LES MODULES DU MÉMOIRE</div>

            <div class="dashboard-grid">
                
                <div class="dashboard-tile" onclick="location.href='#p03'">
                    <div class="tile-status">SECURE</div>
                    <div class="tile-icon">◈</div>
                    <div class="tile-title">I. VISION</div>
                    <div class="tile-desc">Introduction, enjeux et trajectoire 2027 du réseau Happy House.</div>
                    <div class="tile-meta">ACCESS PAGE 03</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p10'">
                    <div class="tile-status">ACTIVE</div>
                    <div class="tile-icon">◎</div>
                    <div class="tile-title">II. IDENTITY</div>
                    <div class="tile-desc">Histoire, équipe clé et proposition de valeur "Casual Luxury".</div>
                    <div class="tile-meta">ACCESS PAGE 10</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p18'">
                    <div class="tile-status" style="color:#3498DB; border-color:#3498DB;">ANALYZE</div>
                    <div class="tile-icon">◬</div>
                    <div class="tile-title">III. DIAGNOSTICS</div>
                    <div class="tile-desc">Analyse profonde des forces du marché (PESTEL) et du réseau (SWOT).</div>
                    <div class="tile-meta">ACCESS PAGE 18</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p26'">
                    <div class="tile-status" style="color:#2ECC71; border-color:#2ECC71;">PERFORM</div>
                    <div class="tile-icon">⚙</div>
                    <div class="tile-title">IV. SALES ENGINE</div>
                    <div class="tile-desc">Ingénierie de la Sales Machine et automatisation CRM Maison.</div>
                    <div class="tile-meta">ACCESS PAGE 26</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p33'">
                    <div class="tile-status">PROOF</div>
                    <div class="tile-icon">☖</div>
                    <div class="tile-title">V. FIELD RESEARCH</div>
                    <div class="tile-desc">6 Interviews terrain et validation de la demande client.</div>
                    <div class="tile-meta">ACCESS PAGE 33</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p41'">
                    <div class="tile-status">RETAIN</div>
                    <div class="tile-icon">☍</div>
                    <div class="tile-title">VI. RETENTION</div>
                    <div class="tile-desc">Stratégie Double Détente : Afterworks et Webinaires.</div>
                    <div class="tile-meta">ACCESS PAGE 41</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p43'">
                    <div class="tile-status">CORE</div>
                    <div class="tile-icon">📶</div>
                    <div class="tile-title">VII. ONBOARDING</div>
                    <div class="tile-desc">Digitalisation de l'expérience hôte via NFC et QR codes.</div>
                    <div class="tile-meta">ACCESS PAGE 43</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p46'">
                    <div class="tile-status" style="color:var(--gold); border-color:var(--gold);">ROI</div>
                    <div class="tile-icon">⊘</div>
                    <div class="tile-title">VIII. PERFORMANCE</div>
                    <div class="tile-desc">Étude du Cas Durentie, CAC Elite et projections financières.</div>
                    <div class="tile-meta">ACCESS PAGE 46</div>
                </div>

                <div class="dashboard-tile" onclick="location.href='#p51'">
                    <div class="tile-status" style="color:#E74C3C; border-color:#E74C3C;">LOCKED</div>
                    <div class="tile-icon">🔒</div>
                    <div class="tile-title">IX. VAULT</div>
                    <div class="tile-desc">Annexes techniques, Playbook et justificatifs confidentiels.</div>
                    <div class="tile-meta">ACCESS PAGE 51</div>
                </div>

            </div>
        </div>
        <div class="footer"><div>SYSTEM DASHBOARD V.2026</div><div class="page-num">02</div></div>
    </div>
"""

# Regex substitution for page 02
content = re.sub('(?s)<div class="page" id="p02">.*?<div class="page" id="p03">', f"{dashboardBody}\n    <div class=\"page\" id=\"p03\">", content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard implemented.")
