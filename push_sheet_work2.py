import git
import os

GIT_REPOSITORY = 'https://github.com/PlatinumGames-Inc/055-master-data.git'
OUTPUT_PATH = '055-master-data/master/p1/sheet_work/'
REPOSITORY_PATH = '055-master-data'

os.chdir(REPOSITORY_PATH)
repo = git.Repo()
repo.config_writter().set_value('user', 'name', 'prj055')
repo.config_writter().set_value('user', 'email', 'prj055_appsheet@platinumgames.co.jp')
repo.config_writter().write()
o = repo.remotes.origin
o.pull()
repo.git.add('--all')
repo.git.commit('.','-m','\"GAS auto commit\"')
origin = repo.remote(name='origin')
origin.push()
