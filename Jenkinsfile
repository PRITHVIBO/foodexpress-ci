pipeline {
    agent any

    environment {
        PATH = "D:\\AnacondaAIML;D:\\AnacondaAIML\\Scripts;${env.PATH}"
    }

    stages {
        stage('Build') {
            steps {
                bat 'where python'
                bat 'python --version'
                bat 'python -m pip --version'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }
    }
}