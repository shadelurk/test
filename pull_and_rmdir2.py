import git
import os
import shutil

GIT_URL = 'https://github.com/shadelurk/mdouttest.git'
GIT_TOKEN = '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'
REPOSITORY_PATH = 'mdouttest'
OUTPUT_PATH = '055-master-data/master/p1/sheet_work/'

if os.path.exists(REPOSITORY_PATH) != True:
    git.Repo.clone_from(GIT_URL, OUTPUT_PATH, branch='main', depth=1, auth=git.auth.HttpGitAuth('token', GIT_TOKEN))

g = git.cmd.Git(REPOSITORY_PATH)
g.pull()

shutil.rmtree(OUTPUT_PATH)
os.makedirs(OUTPUT_PATH, exist_ok=True)
