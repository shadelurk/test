pipeline {
  agent { dockerfile true }
  environment {
      MY_TOKEN = credentials('TOKEN')
  }
  stages {
    stage('Test') {
      steps {
        withCredentials([usernamePassword(credentialsId: '055build', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
          sh 'python sheet_work_download.py ${MY_TOKEN}'
        }
      }
    }
  }
}