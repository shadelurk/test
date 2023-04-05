import git
from git import Repo
import os
import shutil

OUTPUT_PATH = '055-master-data/master/p1/sheet_work/'
REPOSITORY_PATH = '055-master-data'

remote = f"https://{os.environ['GIT_USERNAME']}:{os.environ['GIT_PASSWORD']}@github.com/PlatinumGames-Inc/055-master-data.git"

if os.path.exists(REPOSITORY_PATH) != True:
    Repo.clone_from(remote,REPOSITORY_PATH)

g = git.cmd.Git(REPOSITORY_PATH)
g.pull()

shutil.rmtree(OUTPUT_PATH)
os.makedirs(OUTPUT_PATH, exist_ok=True)


