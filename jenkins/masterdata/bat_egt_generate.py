import git
import os
import docker

client = docker.from_env()

os.system('pwd')
os.system('docker-compose --version')
os.system('/usr/local/bin/docker-compose --version')
os.system('bash 055-server/bat/egt_generate.sh')