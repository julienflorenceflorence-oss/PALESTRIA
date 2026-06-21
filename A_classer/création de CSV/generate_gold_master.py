import pandas as pd
import os

def create_complete_excel():
    csv_path = 'CLIENTS_Triage_Enrichi_V3_FINAL_REPAIRED.csv'
    jf_path = 'prompt générato/Liste des lieux vu par JF - Tableau de suivi.csv'
    excel_path = 'HAPPY_HOUSE_GOLD_STANDARD_MASTER.xlsx'
    
    # Load Main Data
    df_master = pd.read_csv(csv_path)
    
    # Load JF Data if exists
    df_jf = pd.DataFrame()
    if os.path.exists(jf_path):
        try:
            df_jf = pd.read_csv(jf_path, encoding='utf-8-sig')
        except:
            df_jf = pd.read_csv(jf_path, encoding='latin1')

    # Create Excel writer
    writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
    workbook = writer.book
    
    # --- COMMON FORMATS ---
    header_blue = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#1F4E78', 'font_color': 'white', 'border': 1})
    header_green = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#70AD47', 'font_color': 'white', 'border': 1})
    header_orange = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#ED7D31', 'font_color': 'white', 'border': 1})
    header_purple = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#7030A0', 'font_color': 'white', 'border': 1})
    
    # 1. DASHBOARD (Dynamic Stats)
    df_dash = pd.DataFrame({'Indicateur': ['Total Clients', 'Publiés', 'A décider', 'NO GO', 'Complétude ✅'], 'Valeur': [len(df_master), 0, 0, 0, 0]})
    df_dash.to_excel(writer, sheet_name='Dashboard', index=False)
    ws_dash = writer.sheets['Dashboard']
    ws_dash.set_column('A:A', 30)
    ws_dash.set_column('B:B', 15)
    
    # 2. TRIAGE MASTER (The Engine)
    df_master.to_excel(writer, sheet_name='TRIAGE MASTER', index=False)
    ws_master = writer.sheets['TRIAGE MASTER']
    for col_num, value in enumerate(df_master.columns.values):
        ws_master.write(0, col_num, value, header_blue)
    ws_master.freeze_panes(1, 2)
    ws_master.set_column('A:A', 5); ws_master.set_column('B:B', 35); ws_master.set_column('F:G', 15); ws_master.set_column('W:Y', 25)
    
    # Formulas for Master
    last_row = len(df_master) + 1
    for row in range(1, last_row):
        r = row + 1
        ws_master.write_formula(row, 6, f'=IF(OR(E{r}<5, H{r}="NON", I{r}="NON", J{r}="NON"), "HAUTE", "MOYENNE")')
        ws_master.write_formula(row, 25, f'=IF(AND(H{r}="OUI", I{r}="OUI", J{r}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")')

    # 3. RDV JULIEN (From JF Suivi)
    df_jf.to_excel(writer, sheet_name='RDV Julien', index=False)
    ws_jf = writer.sheets['RDV Julien']
    for col_num, value in enumerate(df_jf.columns.values):
        ws_jf.write(0, col_num, value, header_green)
    ws_jf.freeze_panes(1, 1)
    ws_jf.set_column('A:A', 30); ws_jf.set_column('F:I', 15)

    # 4. GUIDE (Instructions)
    guide_data = [
        ["SECTION", "RÈGLE", "DESCRIPTION"],
        ["IDENTITÉ", "MAJUSCULES", "Les noms de famille doivent être en majuscules."],
        ["TECH", "OUI/NON", "Utiliser 'OUI' ou 'NON' pour SITE WEB, DROPBOX, APP."],
        ["PRIORITÉ", "Automatique", "Calculée sur la colonne G : < 5 photos ou manque tech = HAUTE."],
        ["CONTACT", "+33", "Format international obligatoire pour les téléphones."],
        ["COMPLÉTUDE", "Automatique", "Calculée sur la colonne Z : Nécessite SITE HH + DROPBOX + APP."]
    ]
    pd.DataFrame(guide_data).to_excel(writer, sheet_name='Guide', index=False, header=False)
    ws_guide = writer.sheets['Guide']
    ws_guide.set_column('A:C', 30)
    for c in range(3): ws_guide.write(0, c, guide_data[0][c], header_purple)

    # 5. SUIVI APPELS
    df_calls = pd.DataFrame(columns=['Date', 'Client', 'Agent', 'Durée', 'Résultat', 'Commentaire'])
    df_calls.to_excel(writer, sheet_name='Suivi Appels', index=False)
    ws_calls = writer.sheets['Suivi Appels']
    for col_num, value in enumerate(df_calls.columns.values):
        ws_calls.write(0, col_num, value, header_orange)
    ws_calls.set_column('A:F', 20)

    # 6. HISTORIQUE
    df_hist = pd.DataFrame(columns=['Date', 'Action', 'Utilisateur', 'Détails'])
    df_hist.to_excel(writer, sheet_name='Historique', index=False)
    ws_hist = writer.sheets['Historique']
    for col_num, value in enumerate(df_hist.columns.values):
        ws_hist.write(0, col_num, value, header_blue)

    # 7. LOGS
    df_logs = pd.DataFrame(columns=['Timestamp', 'Type', 'Message', 'Severity'])
    df_logs.to_excel(writer, sheet_name='Logs', index=False)

    # 8. SOURCES & ARCHIVES
    pd.DataFrame().to_excel(writer, sheet_name='SOURCES', index=False)
    pd.DataFrame().to_excel(writer, sheet_name='ARCHIVES', index=False)

    # Conditional Formatting for Master
    fmt_red = workbook.add_format({'bg_color': '#F4CCCC', 'font_color': '#990000'})
    fmt_yellow = workbook.add_format({'bg_color': '#FFF2CC', 'font_color': '#BF9000'})
    fmt_green = workbook.add_format({'bg_color': '#D9EAD3', 'font_color': '#274E13'})
    
    ws_master.conditional_format(1, 6, last_row-1, 6, {'type': 'cell', 'criteria': 'equal to', 'value': '"HAUTE"', 'format': fmt_red})
    ws_master.conditional_format(1, 6, last_row-1, 6, {'type': 'cell', 'criteria': 'equal to', 'value': '"MOYENNE"', 'format': fmt_yellow})
    ws_master.conditional_format(1, 25, last_row-1, 25, {'type': 'text', 'criteria': 'containing', 'value': 'COMPLET', 'format': fmt_green})

    writer.close()
    print(f"COMPLETE GOLD MASTER GENERATED: {excel_path}")

if __name__ == "__main__":
    create_complete_excel()
