pipeline {
    agent any

    environment {
        DOCKER_REPO = "tanzila123/selenium"
        DOCKER_TAG  = "selenium.image"
    }

    stages {
        stage('Check Python') {
            steps {
                echo "Verifying Python installation"
                bat 'where python3'
                bat 'python3 --version'
                bat 'python3 -m pip --version'
            }
        }

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Install Python dependencies
                bat 'python3 -m pip install -r requirements.txt'

                // Start Flask app in background
                bat 'start /B python3 app.py'

                // Wait for Flask to start
                bat 'ping 127.0.0.1 -n 5 > nul'

                // Run Selenium tests
                bat 'python3 -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                bat "docker build -t ${DOCKER_REPO}:${DOCKER_TAG} ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"
                bat 'docker login -u tanzila123 -p Tan@12345'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub"
                bat "docker push ${DOCKER_REPO}:${DOCKER_TAG}"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    bat 'kubectl apply -f deployment.yaml --validate=false'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check the logs.'
        }
    }
}
