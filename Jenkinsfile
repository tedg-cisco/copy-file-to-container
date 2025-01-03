pipeline {
    agent {
        docker {
            image 'docker:24.0.5' // Ensure Docker CLI is available
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        MY_ENV_VAR = 'HelloWorld'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Python App') {
            steps {
                script {
                    sh 'echo "Installing Python dependencies..."'
                    sh 'pip install -r app/requirements.txt'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app ./app'
            }
        }
        stage('Copy File and Run Container') {
            steps {
                script {
                    // Copy the file to the container
                    sh '''
                    echo "Copying file and running container..."
                    docker run -d --name temp_container my-python-app
                    docker cp input.txt temp_container:/app/input.txt
                    docker commit temp_container my-python-app-with-file
                    docker rm -f temp_container
                    '''

                    // Run the updated container
                    sh 'docker run --rm -e MY_ENV_VAR=$MY_ENV_VAR my-python-app-with-file'
                }
            }
        }
    }
    post {
        always {
            sh 'docker system prune -f' // Cleanup
        }
    }
}
