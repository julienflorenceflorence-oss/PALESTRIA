import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/documents'
]

token_path = r"C:\Users\julien\OneDrive\Bureau\geminicli\agent soutenance\token.json"

if os.path.exists(token_path):
    print("Loading credentials from token.json...")
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
else:
    print("token.json not found!")
    exit()

try:
    print("Building drive service...")
    service = build('drive', 'v3', credentials=creds)
    
    sheet_id = "1jgxlR0q_3iSkTgOBOt1shgXPwmXykQOOrAAdAyy2tiI"
    print(f"Fetching metadata for file {sheet_id}...")
    file_metadata = service.files().get(fileId=sheet_id).execute()
    print("Metadata:", file_metadata)
    
    print("Attempting to export as CSV...")
    content = service.files().export(fileId=sheet_id, mimeType='text/csv').execute()
    print("Export successful! Sample of content:")
    print(content[:500].decode('utf-8'))

except HttpError as error:
    print(f'An error occurred: {error}')
