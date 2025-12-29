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

        stage('Start Selenium Grid') {
            steps {
                bat '''
                cd docker
                docker-compose up -d
                '''
            }
        }

        stage('Wait for Grid') {
            steps {
                bat '''
                timeout /t 10 /nobreak
                '''
            }
        }

        stage('Run Automation') {
            steps {
                bat '''
                venv\\Scripts\\python main.py --driver grid
                '''
            }
        }
    }

    post {
        always {
            bat '''
            cd docker
            docker-compose down
            '''
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
