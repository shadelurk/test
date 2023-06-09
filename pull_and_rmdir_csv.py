import git
from git import Repo
import os
import shutil

OUTPUT_PATH = '055-master-data/output/csv/'
REPOSITORY_PATH = '055-master-data'

remote = f"https://{os.environ['USERNAME']}:{os.environ['PERSONAL_ACCESS_TOKEN']}@github.com/PlatinumGames-Inc/055-master-data.git"

if os.path.exists(REPOSITORY_PATH) != True:
    Repo.clone_from(remote,REPOSITORY_PATH)

g = git.cmd.Git(REPOSITORY_PATH)
g.pull()

shutil.rmtree(OUTPUT_PATH)
os.makedirs(OUTPUT_PATH, exist_ok=True)


