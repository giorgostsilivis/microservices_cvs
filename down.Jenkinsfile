pipeline {
    agent any

    stages {
        stage('Staging') {
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose down'
            }
        }
        stage('scheduler process') {
            steps {
                dir("nrv/") {
                    sh 'pkill -f scheduler.py'
                }
            }
        }
    }
}
