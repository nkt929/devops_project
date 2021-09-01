pipeline {
    agent any
    stages {
        stage('test') {
            agent {
                docker {
                    image 'python:3.9-alpine'
                }
            }
            steps {
                sh 'pip3 install Flask pytz'
                sh 'python3 app_python/time_update_test.py'
            }
        }
        stage('docker') {
            steps {
                script {
                    img = docker.build('nkt929/devops_project', './app_python')
                    docker.withRegistry('', 'docker') {
                        img.push("latest")
                    }
                }
            }
        }
    }
}