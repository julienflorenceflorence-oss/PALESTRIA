import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/documents']

def main():
    print("Script started...")
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0, open_browser=False)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': 'RDM_ULTIMATE_PRESTIGE_20_SUR_20',
            'mimeType': 'application/vnd.google-apps.document'
        }
        media = MediaFileUpload('RDM_ULTIMATE_PRESTIGE_20_20.html',
                                mimetype='text/html')
        
        print("Uploading file...")
        file = service.files().create(body=file_metadata, media_body=media,
                                    fields='id,webViewLink').execute()
        print(f"File ID: {file.get('id')}")
        print(f"File Link: {file.get('webViewLink')}")

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()
