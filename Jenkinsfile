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
            mail to: 'your-email@youremail.com',
            subject: "Failed build Pipeline: ${currentBuild.fullDisplayName}",
            body: "The pipeline ${currentBuild.fullDisplayName} failed."
        }
        success {
            mail to: 'your-email@youremail.com',
            subject: "Completed Pipeline: ${currentBuild.fullDisplayName}",
            body: "Your build completed, please check: ${env.BUILD_URL}"
        }
    }
}


