import re

def count_words(text):
    text = re.sub('<[^>]*>', ' ', text)
    return len(text.split())

with open('RDM_FINAL_MASTER_JULIEN_FLORENCE.html', encoding='utf-8') as f:
    content = f.read()

# Remove style for count
clean_content = re.sub('(?s)<style>.*?</style>', '', content)
print(f"Total Words: {count_words(clean_content)}")

# Split content by the markers I inserted
# <!-- PAGE 03 --> etc.
chunks = re.split(r'<!-- PAGE \d+ -->', content)
print(f"Found {len(chunks)} chunks.")

for i, c in enumerate(chunks[:15]):
    print(f"Chunk {i}: {count_words(c)} words")
