FROM python:3

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install GitPython
RUN pip install docker
RUN chmod 666 /var/run/docker.sock
RUN curl -SL https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
RUN ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

CMD [ "python", "./quickstart.py" ]