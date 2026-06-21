import pandas as pd
import csv
import re
import unicodedata

def normalize(s):
    if not isinstance(s, str): return ""
    s = unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('utf-8')
    s = s.lower().replace('-', ' ').replace('_', ' ')
    s = re.sub(r'[^a-z0-9\s]', '', s)
    return " ".join(s.split())

def create_excel():
    csv_path = 'CLIENTS_Triage_Enrichi_V3_FINAL_REPAIRED.csv'
    excel_path = 'HAPPY_HOUSE_TRIAGE_MASTER_FINAL.xlsx'
    
    # 1. Read the repaired CSV data
    df = pd.read_csv(csv_path)
    
    # Create Excel writer with xlsxwriter engine
    writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
    
    # 2. Write Main Sheet: TRIAGE MASTER
    df.to_excel(writer, sheet_name='TRIAGE MASTER', index=False)
    
    # 3. Create dummy Source and Archives sheets
    pd.DataFrame().to_excel(writer, sheet_name='SOURCES', index=False)
    pd.DataFrame().to_excel(writer, sheet_name='ARCHIVES', index=False)
    
    workbook = writer.book
    worksheet = writer.sheets['TRIAGE MASTER']
    
    # Design Formats
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center',
        'fg_color': '#1F4E78', # Dark Blue
        'font_color': 'white',
        'border': 1
    })
    
    # Apply header format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
    
    # Freeze Panes (Row 1, Columns 1 & 2)
    worksheet.freeze_panes(1, 2)
    
    # Define Column Widths
    worksheet.set_column('A:A', 5)   # N°
    worksheet.set_column('B:B', 35)  # Nom
    worksheet.set_column('C:E', 15)  # Ville, Pays, Photos
    worksheet.set_column('F:F', 20)  # Statut
    worksheet.set_column('G:G', 15)  # Priorite
    worksheet.set_column('H:J', 10)  # Tech Yes/No
    worksheet.set_column('L:O', 15)  # Links
    worksheet.set_column('W:Y', 25)  # Contacts
    worksheet.set_column('Z:Z', 20)  # Alerte
    
    last_row = len(df) + 1
    
    # Re-insert Formulas as Excel formulas
    # Col G: Priorite (Index 6)
    # Formula: =IF(OR(E2<5, H2="NON", I2="NON", J2="NON"), "HAUTE", "MOYENNE")
    for row in range(1, last_row):
        r_idx = row + 1
        formula = f'=IF(OR(E{r_idx}<5, H{r_idx}="NON", I{r_idx}="NON", J{r_idx}="NON"), "HAUTE", "MOYENNE")'
        worksheet.write_formula(row, 6, formula)
        
        # Col Z: Alerte (Index 25)
        # Formula: =IF(AND(H2="OUI", I2="OUI", J2="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")
        formula_comp = f'=IF(AND(H{r_idx}="OUI", I{r_idx}="OUI", J{r_idx}="OUI"), "✅ COMPLET", "⚠️ À OPTIMISER")'
        worksheet.write_formula(row, 25, formula_comp)

    # Conditional Formatting
    # Priorite: HAUTE (Red), MOYENNE (Yellow)
    worksheet.conditional_format(1, 6, last_row-1, 6, {
        'type': 'cell', 'criteria': 'equal to', 'value': '"HAUTE"',
        'format': workbook.add_format({'bg_color': '#F4CCCC', 'font_color': '#990000'})
    })
    worksheet.conditional_format(1, 6, last_row-1, 6, {
        'type': 'cell', 'criteria': 'equal to', 'value': '"MOYENNE"',
        'format': workbook.add_format({'bg_color': '#FFF2CC', 'font_color': '#BF9000'})
    })
    
    # Alerte: COMPLET (Green), OPTIMISER (Orange)
    worksheet.conditional_format(1, 25, last_row-1, 25, {
        'type': 'text', 'criteria': 'containing', 'value': 'COMPLET',
        'format': workbook.add_format({'bg_color': '#D9EAD3', 'font_color': '#274E13'})
    })
    worksheet.conditional_format(1, 25, last_row-1, 25, {
        'type': 'text', 'criteria': 'containing', 'value': 'OPTIMISER',
        'format': workbook.add_format({'bg_color': '#FCE5CD', 'font_color': '#783F04'})
    })

    # Close and save
    writer.close()
    print(f"EXCEL GENERATED SUCCESSFULLY: {excel_path}")

if __name__ == "__main__":
    create_excel()
