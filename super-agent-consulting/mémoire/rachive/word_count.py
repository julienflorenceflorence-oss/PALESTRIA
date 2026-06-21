import re
import sys

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove script and style tags
    content = re.sub(r'<(script|style).*?>.*?</\1>', '', content, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', ' ', content)
    # Count words
    words = content.split()
    return len(words)

if __name__ == "__main__":
    print(count_words(sys.argv[1]))
