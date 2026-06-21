import codecs

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Modify the assembly loop to omit the footer entirely for the cover page
old_cover_assembly = """    <div class="page cover">
        <div class="cover-bg"></div>
        <a id="page-{page_number}"></a>
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content cover-content">
            {p["content"]}
        </div>
        <div class="footer">
            <div style="color: #DDA83E;">HAPPY HOUSE & ROCKET SCHOOL</div>
            <div class="page-number" style="color: #DDA83E;">{page_number:02d}</div>
        </div>
    </div>"""

new_cover_assembly = """    <div class="page cover">
        <div class="cover-bg"></div>
        <a id="page-{page_number}"></a>
        <div class="corner top-left"></div><div class="corner top-right"></div><div class="corner bottom-left"></div><div class="corner bottom-right"></div>
        <div class="content cover-content">
            {p["content"]}
        </div>
        <!-- No footer on cover page -->
    </div>"""

c = c.replace(old_cover_assembly, new_cover_assembly)

with open('mémoire/RDM 3.0/build_rdm_v9_soutenance.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Cover page footer (page number) removed.")
