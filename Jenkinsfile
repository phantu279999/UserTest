pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/phantu279999/UserTest.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                "C:\\Users\\Welcome\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv venv
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automation') {
            steps {
                bat '''
                venv\\Scripts\\python main.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'log\\**', allowEmptyArchive: true
        }
        failure {
            echo 'Automation failed – check logs'
        }
        success {
            echo 'Automation passed'
        }
    }
}
