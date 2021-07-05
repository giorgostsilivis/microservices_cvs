pipeline {
    agent any

    stages {
        stage('Staging') {
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose down'
            }
        }
    }
}
