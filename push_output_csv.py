import git
import os

GIT_REPOSITORY = 'https://github.com/PlatinumGames-Inc/055-master-data.git'
OUTPUT_PATH = '055-master-data/sheet/'
REPOSITORY_PATH = '055-master-data'

os.chdir(REPOSITORY_PATH)os.environ['GIT_AUTHOR_NAME'] = 'PRJ055Jenkins'
os.environ['GIT_AUTHOR_EMAIL'] = 'prj055_appsheet@platinumgames.co.jp'
os.environ['GIT_COMMITTER_NAME'] = 'PRJ055Jenkins'
os.environ['GIT_COMMITTER_EMAIL'] = 'prj055_appsheet@platinumgames.co.jp'
repo = git.Repo()
o = repo.remotes.origin
o.pull()
if repo.is_dirty(untracked_files=True):
    repo.git.add('--all')
    repo.git.commit('.','-m','\"jenkins output commit\"')
    repo.git.push('origin', 'build-egt-master-test', env={'GIT_USERNAME': os.environ['USERNAME'], 'GIT_PASSWORD': os.environ['PERSONAL_ACCESS_TOKEN']})
else:
    print("nothing to commit")
