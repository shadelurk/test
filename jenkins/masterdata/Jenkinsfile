pipeline {
  agent { dockerfile true }
  environment {
      MY_TOKEN = credentials('TOKEN')
  }
  stages {
    stage('Test') {
      steps {
        withCredentials([usernamePassword(credentialsId: '055build', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
          sh 'python reconstruct_before.py ${MY_TOKEN} ${scriptId} ${releaseVersion} ${folderName}'
          sh 'python reconstruct_after.py ${MY_TOKEN} ${scriptId} ${folderName}'
          sh 'python pull_and_rmdir.py'
          sh 'python sheet_work_download.py ${MY_TOKEN}'
          sh 'python push_sheet_work.py'
        }
      }
    }
  }
}