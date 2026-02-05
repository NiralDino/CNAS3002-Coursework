pipeline {
    agent any

    stages {
        stage('Install dependancies'){
            steps {
                sh 'python3 -m venv venv'

                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run unit tests'){
            steps {
                sh './venv/bin/python3 -m unittest discover -s . -p "test_*.py" -v'
            }
        }
    }
}
