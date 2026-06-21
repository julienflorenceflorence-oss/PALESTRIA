import os

def clean_encoding_scories(file_path):
    replacements = {
        'Ã©': 'é',
        'Ã¨': 'è',
        'Ã ': 'à',
        'Ã¢': 'â',
        'Ã´': 'ô',
        'Ã»': 'û',
        'Ã®': 'î',
        'Ã«': 'ë',
        'Ã¯': 'ï',
        'Ã§': 'ç',
        'Ãª': 'ê',
        'Ã¹': 'ù',
        'Ã‰': 'É',
        'Ãˆ': 'È',
        'Ã€': 'À',
        'Â«': '«',
        'Â»': '»',
        'âž”': '➔',
        'â€¢': '•',
        'â€“': '–',
        'â€”': '—',
        'Â ': ' ',
        'Ã': 'à' # Souvent le cas quand suivi d'un espace insécable invisible
    }
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Nettoyage de {file_path} terminé.")

if __name__ == "__main__":
    clean_encoding_scories('RDM_PRESTIGE_FINAL.html')
