import csv

months_order = [
    'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
    'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
]

data = []
with open('Copie de Exercice KPI Bizdev - Data.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert numeric fields
        row['chiffre_affaires_total'] = int(row['chiffre_affaires_total'])
        row['nouvelles_opportunités'] = int(row['nouvelles_opportunités'])
        row['cycle_vente_moyen_jours'] = int(row['cycle_vente_moyen_jours'])
        row['Taux convertion'] = float(row['Taux convertion'].replace(',', '.'))
        data.append(row)

# Analysis
revenue_by_bizdev = {}
monthly_evolution = {m: 0 for m in months_order}
conv_rates = {}
counts = {}

for row in data:
    bd = row['business_developer']
    rev = row['chiffre_affaires_total']
    m = row['mois']
    cr = row['Taux convertion']
    
    revenue_by_bizdev[bd] = revenue_by_bizdev.get(bd, 0) + rev
    monthly_evolution[m] += rev
    
    conv_rates[bd] = conv_rates.get(bd, 0) + cr
    counts[bd] = counts.get(bd, 0) + 1

avg_conv_rates = {bd: conv_rates[bd] / counts[bd] for bd in conv_rates}

total_revenue = sum(revenue_by_bizdev.values())
total_ops = sum(row['nouvelles_opportunités'] for row in data)
avg_cycle = sum(row['cycle_vente_moyen_jours'] for row in data) / len(data)

print("--- REVENUE BY BIZDEV ---")
for bd, rev in revenue_by_bizdev.items():
    print(f"{bd}: {rev}")

print("\n--- MONTHLY EVOLUTION ---")
for m in months_order:
    print(f"{m}: {monthly_evolution[m]}")

print("\n--- CONVERSION RATES ---")
for bd, cr in avg_conv_rates.items():
    print(f"{bd}: {cr:.2f}%")

print("\n--- SUMMARY ---")
print(f"Total Revenue: {total_revenue}")
print(f"Total Opportunities: {total_ops}")
print(f"Average Sales Cycle: {avg_cycle:.2f} days")
