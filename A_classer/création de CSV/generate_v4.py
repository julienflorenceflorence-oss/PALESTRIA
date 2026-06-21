import pandas as pd
import os

def create_v4_excel():
    csv_path = 'CLIENTS_Triage_Enrichi_V3_FINAL_REPAIRED.csv'
    jf_path = 'prompt générato/Liste des lieux vu par JF - Tableau de suivi.csv'
    excel_path = 'HAPPY_HOUSE_V4_AVEC_ONGLETS.xlsx'
    
    # Chargement des données sources
    df_master = pd.read_csv(csv_path)
    
    df_jf = pd.DataFrame()
    if os.path.exists(jf_path):
        try:
            df_jf = pd.read_csv(jf_path, encoding='utf-8-sig')
        except:
            df_jf = pd.read_csv(jf_path, encoding='latin1')

    # Création du fichier Excel
    writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
    workbook = writer.book
    
    # --- FORMATS ---
    header_blue = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#1F4E78', 'font_color': 'white', 'border': 1})
    header_green = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#70AD47', 'font_color': 'white', 'border': 1})
    header_orange = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#ED7D31', 'font_color': 'white', 'border': 1})
    header_purple = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'fg_color': '#7030A0', 'font_color': 'white', 'border': 1})
    fmt_red = workbook.add_format({'bg_color': '#F4CCCC', 'font_color': '#990000'})
    fmt_yellow = workbook.add_format({'bg_color': '#FFF2CC', 'font_color': '#BF9000'})
    fmt_green = workbook.add_format({'bg_color': '#D9EAD3', 'font_color': '#274E13'})

    # 1. DASHBOARD
    pd.DataFrame({'KPI': ['Total Clients', 'Publiés', 'A décider', 'NO GO', 'Complétude ✅'], 'Valeur': [len(df_master), 0, 0, 0, 0]}).to_excel(writer, sheet_name='Dashboard', index=False)
    ws_dash = writer.sheets['Dashboard']
    ws_dash.set_column('A:B', 25)

    # 2. TRIAGE MASTER
    df_master.to_excel(writer, sheet_name='TRIAGE MASTER', index=False)
    ws_master = writer.sheets['TRIAGE MASTER']
    for col_num, value in enumerate(df_master.columns.values):
        ws_master.write(0, col_num, value, header_blue)
    ws_master.freeze_panes(1, 2)
    ws_master.set_column('A:A', 5); ws_master.set_column('B:B', 40); ws_master.set_column('F:G', 15); ws_master.set_column('W:Z', 25)
    
    last_row = len(df_master) + 1
    for row in range(1, last_row):
        r = row + 1
        ws_master.write_formula(row, 6, f'=IF(OR(E{r}<5, H{r}="NON", I{r}="NON", J{r}="NON"), "HAUTE", "MOYENNE")')
        ws_master.write_formula(row, 25, f'=IF(AND(H{r}="OUI", I{r}="OUI", J{r}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")')
    ws_master.conditional_format(1, 6, last_row-1, 6, {'type': 'cell', 'criteria': 'equal to', 'value': '"HAUTE"', 'format': fmt_red})
    ws_master.conditional_format(1, 6, last_row-1, 6, {'type': 'cell', 'criteria': 'equal to', 'value': '"MOYENNE"', 'format': fmt_yellow})
    ws_master.conditional_format(1, 25, last_row-1, 25, {'type': 'text', 'criteria': 'containing', 'value': 'COMPLET', 'format': fmt_green})

    # 3. RDV Julien
    df_jf.to_excel(writer, sheet_name='RDV Julien', index=False)
    ws_jf = writer.sheets['RDV Julien']
    for col_num, value in enumerate(df_jf.columns.values):
        ws_jf.write(0, col_num, value, header_green)
    ws_jf.freeze_panes(1, 1)
    ws_jf.set_column('A:A', 35); ws_jf.set_column('B:Z', 20)

    # 4. Guide
    guide = [["ONGLET", "UTILISATION"], ["TRIAGE MASTER", "Gestion quotidienne des clients et complétude tech."], ["RDV Julien", "Suivi des échanges et appels commerciaux."], ["Dashboard", "Vision globale des statistiques."]]
    pd.DataFrame(guide).to_excel(writer, sheet_name='Guide', index=False, header=False)
    ws_guide = writer.sheets['Guide']
    ws_guide.write(0, 0, "ONGLET", header_purple); ws_guide.write(0, 1, "UTILISATION", header_purple)
    ws_guide.set_column('A:B', 30)

    # 5. Suivi Appels
    pd.DataFrame(columns=['Date', 'Client', 'Agent', 'Notes']).to_excel(writer, sheet_name='Suivi Appels', index=False)
    ws_calls = writer.sheets['Suivi Appels']
    for c, v in enumerate(['Date', 'Client', 'Agent', 'Notes']): ws_calls.write(0, c, v, header_orange)
    ws_calls.set_column('A:D', 20)

    # 6. Historique & Logs
    pd.DataFrame(columns=['Date', 'Action', 'Auteur']).to_excel(writer, sheet_name='Historique', index=False)
    pd.DataFrame(columns=['Timestamp', 'Log']).to_excel(writer, sheet_name='Logs', index=False)

    # 7. SOURCES & ARCHIVES
    pd.DataFrame().to_excel(writer, sheet_name='SOURCES', index=False)
    pd.DataFrame().to_excel(writer, sheet_name='ARCHIVES', index=False)

    writer.close()
    print(f"Fichier V4 généré : {excel_path}")

if __name__ == "__main__":
    create_v4_excel()
