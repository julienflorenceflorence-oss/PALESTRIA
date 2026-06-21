import csv

\# Ensuring chronological order for the wine sector's seasonal cycle  
months\_order \= \[  
    'January', 'February', 'March', 'April', 'May', 'June',   
    'July', 'August', 'September', 'October', 'November', 'December'  
\]

data \= \[\]  
\# Assuming the file is named 'Wine\_Sales\_Data.csv'  
try:  
    with open('Wine\_Sales\_Data.csv', mode='r', encoding='utf-8') as f:  
        reader \= csv.DictReader(f)  
        for row in reader:  
            \# Data Cleaning & Type Conversion  
            row\['total\_revenue'\] \= int(row\['total\_revenue'\])  
            row\['new\_opportunities'\] \= int(row\['new\_opportunities'\])  
            row\['avg\_sales\_cycle\_days'\] \= int(row\['avg\_sales\_cycle\_days'\])  
            \# Handling European decimal format (commas)  
            row\['conversion\_rate'\] \= float(row\['conversion\_rate'\].replace(',', '.'))  
            data.append(row)  
except FileNotFoundError:  
    print("Error: The CSV file was not found.")  
    exit()

\# Analytical Structures  
revenue\_by\_region \= {}  
monthly\_evolution \= {m: 0 for m in months\_order}  
conv\_rates \= {}  
counts \= {}

\# Processing Data by Wine Region  
for row in data:  
    region \= row\['wine\_region'\] \# Replaces business\_developer  
    rev \= row\['total\_revenue'\]  
    m \= row\['month'\]  
    cr \= row\['conversion\_rate'\]  
      
    \# Revenue aggregation by Terroir/Region  
    revenue\_by\_region\[region\] \= revenue\_by\_region.get(region, 0\) \+ rev  
      
    \# Time-series aggregation  
    if m in monthly\_evolution:  
        monthly\_evolution\[m\] \+= rev  
      
    \# Tracking for average calculation  
    conv\_rates\[region\] \= conv\_rates.get(region, 0\) \+ cr  
    counts\[region\] \= counts.get(region, 0\) \+ 1

\# Calculating average conversion rates per region  
avg\_conv\_rates \= {region: conv\_rates\[region\] / counts\[region\] for region in conv\_rates}

\# High-level KPIs  
total\_revenue \= sum(revenue\_by\_region.values())  
total\_ops \= sum(row\['new\_opportunities'\] for row in data)  
avg\_cycle \= sum(row\['avg\_sales\_cycle\_days'\] for row in data) / len(data) if data else 0

\# \--- STRATEGIC OUTPUT \---

print("--- REVENUE BY WINE REGION \---")  
\# Sorted by revenue (descending) for immediate prioritization  
for region, rev in sorted(revenue\_by\_region.items(), key=lambda x: x\[1\], reverse=True):  
    print(f"{region}: €{rev:,}")

print("\\n--- MONTHLY REVENUE EVOLUTION \---")  
for m in months\_order:  
    print(f"{m}: €{monthly\_evolution\[m\]:,}")

print("\\n--- AVERAGE CONVERSION RATE BY REGION \---")  
for region, cr in avg\_conv\_rates.items():  
    print(f"{region}: {cr:.2f}%")

print("\\n--- GLOBAL PERFORMANCE SUMMARY \---")  
print(f"Total Revenue: €{total\_revenue:,}")  
print(f"Total Opportunities: {total\_ops}")  
print(f"Average Sales Cycle: {avg\_cycle:.2f} days")  
