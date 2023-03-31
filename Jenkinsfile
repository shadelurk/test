pipeline {
  agent { dockerfile true }
  environment {
      MY_TOKEN = credentials('TOKEN')
  }
  stages {
    stage('Test') {
      steps {
        sh 'python reconstruct_before.py ${MY_TOKEN} ${releaseVersion} ${folderName}'
        sh 'python reconstruct_after.py ${MY_TOKEN} ${folderName}'
        sh 'python pull_and_rmdir.py'
        sh 'python sheet_work_download.py'
        sh 'python push_sheet_work.py'
      }
    }
  }
}