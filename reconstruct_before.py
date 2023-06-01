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
    count_test = 0
    num_test = len(sys.argv)
    print("count_test start", flush=True)
    while count_test < num_test:
        print(count_test, flush=True)
        print(sys.argv[count_test], flush=True)
        count_test += 1
    print("count_test end", flush=True)

    creds = None
    num = len(sys.argv)
    count = 3
    if num < count + 1:
        print("error need parameter ex: python reconstruct_before.py ${MY_TOKEN} 1.2.0 addTest date web version parameter")
    else:
        creds = Credentials.from_authorized_user_file(sys.argv[1], SCOPES)
    if not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    thread_list = []
    while count < num:
        print('%d:%s', count, sys.argv[count], flush=True)
        thread = threading.Thread(target=exec_api, args=(sys.argv[2],sys.argv[count],creds,))
        thread.start()
        thread_list.append(thread)
        count += 1
    for thread in thread_list:
        thread.join()


def exec_api(version, folder, creds):
    try:
        service = build('script', 'v1', credentials=creds)

        request = {
            'function': 'call_reconstruct_before',
            'parameters': [version, folder]
        }
        response = service.scripts().run(
            body=request,
            scriptId='AKfycbzDyTydwtKQKKzvOiUXAGouZzhfuiOUg3QH2ORpPgmD5u1BO8qgWMx5UddmMNqx_Kfq'
        ).execute()
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)

if __name__ == '__main__':
    main()