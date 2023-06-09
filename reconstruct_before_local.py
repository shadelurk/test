"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.
"""
from __future__ import print_function

import os.path
import threading
import time
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/script.external_request','https://www.googleapis.com/auth/spreadsheets']

def main():
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
    thread_list = []
    num = len(sys.argv)
    count = 2
    if num < count + 1:
        print("error need parameter ex: python3 reconstruct_before.py 1.2.0 addTest date web version parameter")
    while count < num:
        thread = threading.Thread(target=exec_api, args=(sys.argv[1],sys.argv[count],creds,))
        thread.start()
        thread_list.append(thread)
        count += 1
    for thread in thread_list:
        thread.join()


def exec_api(version, folder, creds):
    try:
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        request = {
            'function': 'call_reconstruct_before',
            'parameters': [version, folder]
        }
        response = service.scripts().run(
            body=request,
            scriptId='AKfycbwQwd_m3oPtbrS_sCjbSzgtK-kp5UCUPRG8_k--SRG8CMg173jRNd6oSiupZ5UFjVdF'
        ).execute()
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)

if __name__ == '__main__':
    main()