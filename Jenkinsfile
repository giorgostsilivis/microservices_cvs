pipeline {
    agent any

    parameters {
        choice(choices:['start','stop'], description: 'Users Choice', name: 'Service')
    }

    stages {
        stage('Build requirements') {
            when {
                expression { env.CHOICE == 'start' }
            }
            steps {
                    sh 'sudo pip3 install -r requirements.txt'
            }
        }
        stage('scheduler process') {
            when {
                expression { env.CHOICE == 'start' }
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
                expression { env.CHOICE == 'start' }
            }
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Staging') {
            when {
                expression { env.CHOICE == 'stop' }
            }
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo ../microservices_csv/docker-compose down'
            }
        }
        stage('scheduler process') {
            when {
                expression { env.CHOICE == 'stop' }
            }
            steps {
                    sh 'sudo pkill -f scheduler.py'
            }
        }
    }
}
