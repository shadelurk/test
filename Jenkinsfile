pipeline {
  agent { dockerfile true }
  environment {
      MY_TOKEN = credentials('TOKEN')
  }
  stages {
    stage('Test') {
      steps {
        withCredentials([usernamePassword(credentialsId: '055build', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
          sh 'python reconstruct_before.py ${MY_TOKEN} ${releaseVersion} ${folderName}'
          sh 'python reconstruct_after.py ${MY_TOKEN} ${folderName}'
        }
      }
    }
  }
}