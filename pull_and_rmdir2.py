import git
from git import Repo
import os
import shutil

OUTPUT_PATH = 'mdouttest/055-master-data/master/p1/sheet_work/'
REPOSITORY_PATH = 'mdouttest'

full_local_path = "mdouttest"
remote = f"https://{os.environ['GIT_USERNAME']}:{os.environ['GIT_PASSWORD']}@github.com/shadelurk/mdouttest.git"

if os.path.exists(REPOSITORY_PATH) != True:
    Repo.clone_from(remote,full_local_path)

g = git.cmd.Git(full_local_path)
g.pull()

shutil.rmtree(OUTPUT_PATH)
os.makedirs(OUTPUT_PATH, exist_ok=True)


