import re
import os

def clean_html(content):
    # Remove script tags and style tags for word count
    content = re.sub('(?s)<style>.*?</style>', '', content)
    content = re.sub('(?s)<script>.*?</script>', '', content)
    # Remove HTML tags
    text = re.sub('<[^>]*>', ' ', content)
    return text

def count_words(text):
    return len(text.split())

batches = ['batch1.html', 'batch2.html', 'batch3.html', 'batch4.html', 'annexes.html']
total_text = ""

for b in batches:
    if os.path.exists(b):
        with open(b, 'r', encoding='utf-8') as f:
            total_text += clean_html(f.read())

print(f"Total Words in batches: {count_words(total_text)}")
