pipeline {
    agent any
    environment {
        MESSAGE = "Hello from Jenkins Pipeline!" // Environment variable for the container
    }
    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from source control
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image with a tag
                    sh 'docker build -t python-app .'
                }
            }
        }
        stage('Prepare Input File') {
            steps {
                script {
                    // Create an input file in the Jenkins workspace
                    writeFile file: 'input.txt', text: 'This is content from Jenkins input file.'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Run the container and mount the input file
                    sh '''
                        docker run -d \
                        --name my-running-container \
                        -e MESSAGE="$MESSAGE" \
                        -v $(pwd)/input.txt:/input.txt \
                        python-app
                    '''
                }
            }
        }
    }
//     post {
//         always {
//             // Cleanup any remaining artifacts
//             sh 'docker system prune -f'
//         }
//     }
}

