#!/bin/bash

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
    creds = None
    num = len(sys.argv)
    count = 2
    if num < count + 1:
        print("error need parameter ex: python reconstruct_after.py ${MY_TOKEN} addTest date web version parameter", flush=True)
    else:
        creds = Credentials.from_authorized_user_file(sys.argv[1], SCOPES)
    if not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    thread_list = []
    while count < num:
        print('%d:%s', count, sys.argv[count], flush=True)
        thread = threading.Thread(target=exec_api, args=(sys.argv[count],creds,))
        thread.start()
        thread_list.append(thread)
        count += 1
    for thread in thread_list:
        thread.join()


def exec_api(folder, creds):
    try:
        service = build('script', 'v1', credentials=creds)

        request = {
            'function': 'call_reconstruct_after',
            'parameters': [folder]
        }
        response = service.scripts().run(
            body=request,
            scriptId='AKfycbw5a0dbQilBVuReCtR-YLMh0tbSkUiP7U6R5Y-ugDOMe4XxtNbf-Q3r4uPgHUglhSp2'
        ).execute()
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content, flush=True)

if __name__ == '__main__':
    main()