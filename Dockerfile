FROM python:3

RUN ls -l /etc
RUN cat /etc/os-release
RUN apt-get update
RUN apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
RUN docker run hello-world
RUN ls -l /var/run/
RUN pip install --upgrade pip google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install GitPython
RUN uname -a
RUN curl -SL https://github.com/docker/compose/releases/download/v2.18.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
RUN ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
