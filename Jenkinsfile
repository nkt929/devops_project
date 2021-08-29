pipeline {
    agent { docker { image 'python:3.9-slim' } }
    stages {
        stage('install dependencies') {
            steps {
                sh '''
                    cd app_python
                    pip install Flask pytz
                '''
            }
        }
        stage('testing') {
            steps {
                sh '''
                    black --check .
                    python time_update_test.py
                '''
                }
            }
        }

}