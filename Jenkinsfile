pipeline {
    agent any

    parameters {
        choice(choices:['start','stop'], description: 'Users Choice', name: 'Service')
    }

    stages {
        stage('Build requirements') {
            when {
                expression { params.Service == 'start' }
            }
            steps {
                    sh 'sudo pip3 install -r requirements.txt'
            }
        }
        stage('scheduler process') {
            when {
                expression { params.Service == 'start' }
            }
            steps {
                dir("nrv/") {
                    sh 'sudo mkdir downloads'
                    sh 'sudo python3 scheduler.py &'
                }
            }
        }
        stage('Staging') {
            when {
                expression { params.Service == 'start' }
            }
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Staging down') {
            when {
                expression { params.Service == 'stop' }
            }
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo ../microservices_csv/docker-compose down'
            }
        }
        stage('scheduler process down') {
            when {
                expression { params.Service == 'stop' }
            }
            steps {
                    sh 'sudo pkill -f scheduler.py'
            }
        }
    }
}
