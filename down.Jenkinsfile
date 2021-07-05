pipeline {
    agent any

    stages {
        stage('Staging') {
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo ../microservices_csv/docker-compose down'
            }
        }
        stage('scheduler process') {
            steps {
                    sh 'sudo pkill -f scheduler.py'
            }
        }
    }
}
