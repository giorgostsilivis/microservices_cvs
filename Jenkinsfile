pipeline {
    agent any

    stages {
        // stage('Testing Environment') {
        //     steps {
        //         dir("server/") {
        //             sh 'mvn test -Dtest=ControllerAndServiceSuite'
        //             sh 'mvn test -Dtest=IntegrationSuite'
        //         }
        //     }
        // }
        // stage('Build requirements') {
        //     steps {
        //             sh 'sudo pip3 install requirements.txt'
        //     }
        // }
        // stage('scheduler process') {
        //     steps {
        //         dir("nrv/") {
        //             sh 'sudo python3 scheduler.py'
        //         }
        //     }
        // }
        stage('Staging') {
            steps {
                // sh 'sudo docker-compose build'
                sh 'sudo docker-compose up -d'
            }
        }
        // stage('end2end Tests') {
        //     steps {
        //         dir("server/") {
        //             sh 'mvn test -Dtest=SeleniumSuite'
        //         }
        //     }
        // }
    }
}
