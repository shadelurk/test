FROM python:3

RUN apt-get update
RUN apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
RUN pip install --upgrade pip google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install GitPython
RUN uname -a
