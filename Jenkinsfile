pipeline {
    agent any

    environment {
        IMAGE_NAME = "flaskcoursework_app"
        CONTAINER_NAME = "Flaskcoursework_container"
    }

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/NiralDino/CNAS3002-Coursework.git'
            }
        }
    }
    
        stage('Building Image') {
            steps {
                sh "docker build -t flaskcoursework_app:12"
            }
        }

        stage('Flask App Test') {
            steps {
                sh "docker run --rm flaskcoursework_app:12 pytest"
            }
        }

        stage('Deploying Applicatiom') {
            steps {
                sh """
                docker stop flaskcoursework_container || true
                docker rm flaskcoursework_container || true

                docker rum -d -p 5050:5050 --name flaskcoursework_container flaskcoursework_app:12
                """
    }
        }
        
    post {
        success {
            echo 'Deployment has completed successfully'
        }
        failure {
            echo 'Pipepline has failed'
        }
    }
}
