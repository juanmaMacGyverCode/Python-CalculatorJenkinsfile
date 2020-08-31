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
            slackSend channel: '#general',
            color: 'danger',
            message: "The pipeline ${currentBuild.fullDisplayName} failed."
        }
        success {
            slackSend channel: '#general',
            color: 'success',
            message: "The pipeline ${currentBuild.fullDisplayName} success. Ustéh he uhn crah!!!"
        }
    }
}


