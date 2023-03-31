FROM python:3

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install GitPython

CMD [ "python", "./quickstart.py" ]