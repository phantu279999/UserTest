pipeline {
    agent any

    triggers {
        cron('H 2 * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/phantu279999/UserTest.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automation') {
            steps {
                sh '''
                source venv/bin/activate
                python main.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'log/*.log, log/*.csv'
        }
        failure {
            echo 'Automation failed – check logs'
        }
        success {
            echo 'Automation passed'
        }
    }
}
