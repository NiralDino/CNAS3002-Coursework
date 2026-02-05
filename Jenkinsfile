pipeline {
    agent any

    stages {
        stage('Install dependancies'){
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run unit tests'){
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }
    }
}
