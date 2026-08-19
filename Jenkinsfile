pipeline {
    agent any

    environment {
        PYTHON_HOME = 'D:\\AnacondaAIML'
        PATH = "D:\\AnacondaAIML;D:\\AnacondaAIML\\Scripts;${env.PATH}"
    }

    stages {

        stage('Build') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install flake8'
            }
        }

        stage('Code Quality') {
            steps {
                bat 'python -m flake8 cart.py test_cart.py || exit /b 0'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Package') {
            steps {
                bat 'python -m zipfile -c foodexpress.zip cart.py test_cart.py requirements.txt'
                archiveArtifacts artifacts: 'foodexpress.zip', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All stages passed and the artifact was created.'
        }

        failure {
            echo 'FAILURE: One stage failed. Open the red stage to see why.'
        }
    }
}