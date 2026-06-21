import codecs

with open('mémoire/RDM 3.0/build_rdm_v13_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove backdrop-filter from glass-card
old_glass_card = ".glass-card { background: var(--glass); backdrop-filter: blur(10px); border: 1px solid var(--border-glass); padding: 15px; border-radius: 4px; margin: 20px 0; position: relative; }"
new_glass_card = ".glass-card { background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-glass); padding: 15px; border-radius: 4px; margin: 20px 0; position: relative; }"

c = c.replace(old_glass_card, new_glass_card)

# Let's also check if there are other backdrop-filters
c = c.replace("backdrop-filter: blur(10px);", "")

with open('mémoire/RDM 3.0/build_rdm_v13_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Removed backdrop-filter to fix PDF rendering bug.")
