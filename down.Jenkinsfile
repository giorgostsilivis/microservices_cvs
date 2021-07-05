pipeline {
    agent any

    stages {
        stage('Staging') {
            steps {
                sh 'sudo cd ..'
                sh 'sudo cd microservices_csv'
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose down'
            }
        }
        stage('scheduler process') {
            steps {
                    sh 'sudo pkill -f scheduler.py'
            }
        }
    }
}
