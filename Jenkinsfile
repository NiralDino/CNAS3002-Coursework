pipeline {
    agent any

    stages {
        stage('Install dependancies'){
            steps {
                sh 'python3 -m venv venv'

                sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run unit tests'){
            steps {
                sh '''
                    source venv/bin/activate
                    python3 -m unittest discover -s tests -v
                '''
            }
        }
    }
}
