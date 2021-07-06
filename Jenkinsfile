pipeline {
    agent any

    parameters {
        choice(choices:['Hello','Bye'], description: 'Users Choice', name: 'CHOICE')
    }

    stages {
        stage('Build requirements') {
            when {
                expression { env.CHOICE == 'Hello' }
            }
            steps {
                    sh 'sudo pip3 install -r requirements.txt'
            }
        }
        stage('scheduler process') {
            when {
                expression { env.CHOICE == 'Hello' }
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
                expression { env.CHOICE == 'Hello' }
            }
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose up -d'
            }
        }
        stage('Staging') {
            when {
                expression { env.CHOICE == 'Bye' }
            }
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo ../microservices_csv/docker-compose down'
            }
        }
        stage('scheduler process') {
            when {
                expression { env.CHOICE == 'Bye' }
            }
            steps {
                    sh 'sudo pkill -f scheduler.py'
            }
        }
    }
}
