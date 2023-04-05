# -*- coding: utf-8 -*-
from __future__ import print_function
import os.path
import io
import sys

# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']
FOLDER_NAME = 'sheet_work'
OUTPUT_PATH = '055-master-data/master/p1/sheet_work/'

def main():
    # OAuth
    drive = None
    """Calls the Apps Script API.
    """
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
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    if creds and creds.valid:
        drive = build('drive', 'v3', credentials=creds)
    if not drive: print('Drive auth failed.')

    # Folfer list
    folders = None
    if drive: 
        results = drive.files().list(
            pageSize=100, 
            fields='nextPageToken, files(id, name)',
            q='name="' + FOLDER_NAME + '" and mimeType="application/vnd.google-apps.folder"'
            ).execute()
        folders = results.get('files', [])
        if not folders: print('No folders found.')

    # File list
    files = None
    if folders:
        query = ''
        for folder in folders:
            if query != '' : query += ' or '
            query += '"' + folder['id'] + '" in parents and mimeType="application/vnd.google-apps.folder"'
            print('folder:' + folder['id'] + " name:" + folder['name'])
        query = '(' + query + ')'
        results = drive.files().list(
            q=query
            ).execute()
        childFolders = results.get('files', [])
        print('query:' + query)
            
        query = ''
        for folder in folders:
            if query != '' : query += ' or '
            # query += '"' + folder['id'] + '" in parents and trashed != true'
            query += '"' + folder['id'] + '" in parents and mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" and trashed != true'
            print('folder:' + folder['id'] + " name:" + folder['name'])
        for childFolder in childFolders:
            if query != '' : query += ' or '
            # query += '"' + childFolder['id'] + '" in parents and trashed != true'
            query += '"' + childFolder['id'] + '" in parents and mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" and trashed != true'
            print('childFolder:' + childFolder['id'] + " name:" + childFolder['name'])
        query = '(' + query + ')'
        print('query:' + query)

        results = drive.files().list(
            q=query
            ).execute()
        files = results.get('files', [])
        if not files: print('No files found.')

    # Download
    if files:
        for file in files:
            print(file['mimeType'] + " " + file['id'] + " name:" + file['name'])
            if file['mimeType'] != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                continue
            print('fileId:' + file['id'] + " name:" + file['name'])
            request = drive.files().get_media(fileId=file['id'])
            # request = drive.files().export(fileId=file['id'], mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            fh = io.FileIO(OUTPUT_PATH + file['name'], mode='wb')
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                _, done = downloader.next_chunk()

if __name__ == '__main__':
    main()