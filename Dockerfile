FROM python:3

RUN pip install --upgrade pip google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install GitPython
