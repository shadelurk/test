FROM python:3

RUN ls -l /etc
RUN cat /etc/os-release
RUN apt-get update
RUN apt-get install ca-certificates curl gnupg lsb-release
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
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
