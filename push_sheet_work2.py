import git
import os

GIT_REPOSITORY = 'https://github.com/shadelurk/mdouttest.git'
OUTPUT_PATH = '055-master-data/master/p1/sheet_work/'
REPOSITORY_PATH = 'mdouttest'

os.chdir(REPOSITORY_PATH)
repo = git.Repo()
o = repo.remotes.origin
o.pull()
repo.git.add('--all')
repo.git.commit('.','-m','\"GAS auto commit\"')
origin = repo.remote(name='origin')
origin.push()
