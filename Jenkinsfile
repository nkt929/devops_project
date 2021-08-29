pipeline {
    agent {
        docker { image 'node:14-alpine' }
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
}