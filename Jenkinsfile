pipeline {
    agent any
    stages {
        stage('Build') {
            steps { bat 'pip install pytest' }
        }
        stage('Test') {
            steps { bat 'pytest' }
        }
    }
}