pipeline {
    agent any

    stages {
        stage('Build requirements') {
            steps {
                    sh 'sudo pip3 install -r requirements.txt'
            }
        }
        stage('scheduler process') {
            steps {
                dir("nrv/") {
                    sh 'sudo mkdir downloads'
                    sh 'sudo python3 scheduler.py &'
                }
            }
        }
        stage('Staging') {
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose up -d'
            }
        }
    }
}
