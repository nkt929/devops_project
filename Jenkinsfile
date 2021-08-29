pipeline {
    agent any
    stages {
        stage('install dependencies') {
            steps {
                sh '''
                    PATH=${PATH}:/usr/local/bin
                    ls
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