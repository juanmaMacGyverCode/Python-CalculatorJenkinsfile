pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage("Unit test") {
            steps {
                sh "python test_calculator.py"
            }
        }
    }
    post {
        failure {
            mail to: 'juanma_9_verde@hotmail.com',
            subject: "Failed build Pipeline: ${currentBuild.fullDisplayName}",
            body: "The pipeline ${currentBuild.fullDisplayName} failed."
        }
    }
}


