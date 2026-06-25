import re

def count_words(text):
    return len(re.sub('<[^>]*>', ' ', text).split())

with open('RDM_FINAL_MASTER_JULIEN_FLORENCE.html', encoding='utf-8') as f:
    content = f.read()

# Find style block
style_match = re.search('(?s)<style>.*?</style>', content)
total_words = count_words(re.sub('(?s)<style>.*?</style>', '', content))
print(f"Total Words (sans style): {total_words}")

# Find pages
pages = re.findall('(?s)<div class="page" id="p\d+">.*?</div>', content)
print(f"Found {len(pages)} pages.")

for i, p in enumerate(pages[:10]):
    print(f"Page {i+1}: {count_words(p)} words")
