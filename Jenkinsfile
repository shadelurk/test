pipeline {
  agent { dockerfile true }
  environment {
      MY_TOKEN = credentials('TOKEN')
  }
  stages {
    stage('Test') {
      steps {
        withCredentials([usernamePassword(credentialsId: '055build', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
          sh 'docker-compose -f ./055-master-data/docker-compose.egt.yml build'
          sh 'docker-compose -f ./055-master-data/docker-compose.egt.yml run --rm egt /egt/egt-exec.sh ./egt/properties/md.properties'
        }
      }
    }
  }
}