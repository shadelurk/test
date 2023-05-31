import git
from git import Repo
import os
import shutil

REPOSITORY_PATH = '055-server'

remote = f"https://{os.environ['GIT_USERNAME']}:{os.environ['GIT_PASSWORD']}@github.com/PlatinumGames-Inc/055-server.git"

if os.path.exists(REPOSITORY_PATH) != True:
    Repo.clone_from(remote,REPOSITORY_PATH)

g = git.cmd.Git(REPOSITORY_PATH)
g.pull()


