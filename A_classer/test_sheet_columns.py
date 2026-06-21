import urllib.request
import csv
import io

sheet_id = "1jgxlR0q_3iSkTgOBOt1shgXPwmXykQOOrAAdAyy2tiI"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

try:
    print(f"Fetching {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        for i in range(5):
            row = next(reader, None)
            if row:
                print(f"Row {i}: {row}")
            else:
                break
except Exception as e:
    print("Error:", e)
