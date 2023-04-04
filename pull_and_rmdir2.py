import git
from git import Repo
import os
import shutil

GIT_REPOSITORY = 'https://github.com/PlatinumGames-Inc/055-master-data.git'
OUTPUT_PATH = 'mdouttest/055-master-data/master/p1/sheet_work/'
REPOSITORY_PATH = 'mdouttest'

full_local_path = "mdouttest"
remote = f"https://{os.environ['GIT_USERNAME']}:{os.environ['GIT_PASSWORD']}@github.com/shadelurk/mdouttest.git"

print('debug 1')
if os.path.exists(REPOSITORY_PATH) != True:
    print('debug 2')
    Repo.clone_from(remote,full_local_path)

print('debug 3')

g = git.cmd.Git(full_local_path)
g.pull()

print('debug 4')
shutil.rmtree(OUTPUT_PATH)
os.makedirs(OUTPUT_PATH, exist_ok=True)


