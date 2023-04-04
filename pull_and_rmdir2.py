import git
import os
import shutil

GIT_REPOSITORY = 'https://github.com/shadelurk/mdouttest.git'
OUTPUT_PATH = '055-master-data/master/p1/sheet_work/'
REPOSITORY_PATH = 'mdouttest'

if os.path.exists(REPOSITORY_PATH) != True:
    git.Repo.clone_from(
        GIT_REPOSITORY,
        REPOSITORY_PATH)

g = git.cmd.Git(REPOSITORY_PATH)
g.pull()

shutil.rmtree(OUTPUT_PATH)
os.makedirs(OUTPUT_PATH, exist_ok=True)
