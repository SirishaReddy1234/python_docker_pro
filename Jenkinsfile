pipeline {
    agent any

    stages {
        stage('CHECKOUT') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SirishaReddy1234/python_docker_pro.git']])
            }
        }
         stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build("image_docker")
                }
            }
            
                
            }
            stage('Tag') {
            steps {
                sh 'docker tag image_docker 448049823362.dkr.ecr.ap-south-1.amazonaws.com/myrepo:latest'
            }
        }
            stage('Pushing to ECR') {
            steps {
                script {
                    sh 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 448049823362.dkr.ecr.ap-south-1.amazonaws.com'
                    sh "docker push 448049823362.dkr.ecr.ap-south-1.amazonaws.com/myrepo:latest"
                }
            }
        }
            stage('Run Docker Container') {
            steps {
                script {
                    // Pull the image from ECR
                    
                    
                    // Run the Docker container
                    sh "docker run -d -p 8085:8085 --name my_app_container09 image_docker"
                    
                    // Print container details for verification
                    
                }
            }
            }
            
        }
    }
