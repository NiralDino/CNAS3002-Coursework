pipeline {
    agent any

    environment {
        IMAGE_NAME = "flaskcoursework_app"
        CONTAINER_NAME = "flaskcoursework_container"
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
    
        stage('Building Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Flask App Test') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER} python -m pytest"
            }
        }

        stage('Deploying Applicatiom') {
            steps {
                sh """
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true

                docker run -d -p 5050:5050 --name ${CONTAINER_NAME} ${IMAGE_NAME}:${BUILD_NUMBER}
                """
    }
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
