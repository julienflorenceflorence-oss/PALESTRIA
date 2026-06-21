import codecs

with open('build_rdm.py', 'r', encoding='utf-8') as f:
    c = f.read()

old_proofs = """        <div style="display: flex; flex-direction: column; gap: 15px; align-items: center;">
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/annexe/Pack%20Communication%202%20HH.pdf.pdf.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                📄 1. Pack Communication & Branding
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/doc%20HH/Process%20d'int%C3%A9gration%201.1.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                🤝 2. Contrats & Cadre de Confiance
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/doc%20HH/PMS%20CONNECT%C3%89S.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                🏢 3. Justificatif d'Activité n°2
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/rachive/DATA_DEMONSTRATION_FORCE.html" target="_blank" class="btn-nav" style="width: 80%;">
                📦 4. Livrable Mission n°1
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/annexe/Process%20Commercial%20%26%20KPIs%20-%20Happy%20House%20Edition%20Prestige.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                📊 5. Relevés de Performance & Stats
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/RDM%203.0/HTML/DASHBOARD_HEBERGEURS.html" target="_blank" class="btn-nav" style="width: 80%;">
                ⚙️ 6. Archive Technique & Preuve n°3
            </a>
        </div>"""

new_proofs = """        <div style="display: flex; flex-direction: column; gap: 15px; align-items: center;">
            <h2 style='font-size: 11pt; color: var(--gold-light); margin-bottom: 5px; margin-top: 0;'>A. LIVRABLES & PREUVES (CLOUD)</h2>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/annexe/Pack%20Communication%202%20HH.pdf.pdf.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                📄 1. Pack Communication & Branding
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/doc%20HH/PMS%20CONNECT%C3%89S.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                🏢 2. Justificatif d'Activité n°2
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/rachive/DATA_DEMONSTRATION_FORCE.html" target="_blank" class="btn-nav" style="width: 80%;">
                📦 3. Livrable Mission n°1
            </a>
            <a href="https://github.com/julienflorenceflorence-oss/PALESTRIA/blob/main/super-agent-consulting/m%C3%A9moire/annexe/Process%20Commercial%20%26%20KPIs%20-%20Happy%20House%20Edition%20Prestige.pdf" target="_blank" class="btn-nav" style="width: 80%;">
                📊 4. Relevés de Performance & Stats
            </a>

            <h2 style='font-size: 11pt; color: var(--gold-light); margin-bottom: 5px; margin-top: 15px;'>B. SOCIAL SELLING & EXPERTISE LINKEDIN</h2>
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_oenotourisme-artdevivre-vignobles-activity-7421884268253057024-Ofgh?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 80%;">
                🍇 1. Œnotourisme & Art de Vivre
            </a>
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_serviceclient-excellence-sommelier-activity-7418976158194552832-DbgX?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 80%;">
                🍷 2. Excellence & Service Client (Sommelier)
            </a>
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_effetwaouh-hospitalitaez-happyhouse-activity-7417883359349022720-amMw?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 80%;">
                ✨ 3. L'Effet Waouh en Hospitalité
            </a>
            <a href="https://www.linkedin.com/posts/julien-florence-2536a083_happyhouse-ecotourisme-toulouse-activity-7415346621812645890-4xin?utm_source=share&utm_medium=member_desktop&rcm=ACoAABG4o18BLawDZS3rFCCggwVoWwgws6scy_U" target="_blank" class="btn-nav" style="width: 80%;">
                🌿 4. Écotourisme & Engagement Happy House
            </a>
        </div>"""

c = c.replace(old_proofs, new_proofs)

with open('build_rdm.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("LinkedIN buttons added")
