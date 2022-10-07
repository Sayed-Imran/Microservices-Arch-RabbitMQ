pipeline {
    agent any
    environment {
        
        AWS_DEFAULT_REGION='ap-south-1'
    }
    stages {
        stage('Start AWS EC2 Instances') {
            steps {
                withCredentials([aws(accessKeyVariable:'AWS_ACCESS_KEY_ID',credentialsId:'aws-ec2-creds',secretKeyVaraiable:'AWS_SECRET_ACCESS_KEY')]) {
                  sh '''
	                aws ec2 start-instances --instance-ids 	i-072a35f48879eeeab
	                '''
                }
            }
        }
        stage('Building product Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker system prune -f
                    docker build -t sayedimran/product-service:v1 ./backend/product/
                '''
            }
        }
         stage('Building main Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker build -t sayedimran/main-service:v1 ./backend/main/
                '''
            }
        }
         stage('Building auth Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker build -t sayedimran/auth-service:v1 ./backend/auth/
                '''
            }
        }
        stage('Pushing the product Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker push sayedimran/product-service:v1
                '''
            }
        }
        stage('Pushing the main Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker push sayedimran/main-service:v1
                '''
            }
        }
        
        stage('Pushing the auth Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker push sayedimran/auth-service:v1
                '''
            }
        }
         stage('Building Docker Image for consumer of product service '){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                 docker system prune -f
                 docker build -t sayedimran/consumer-prod:v1 ./backend/consumer-product/
                '''
            }
        }
         stage('Building Docker Image for consumer of main service'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                 docker build -t sayedimran/consumer-main:v1 ./backend/consumer-main/
                '''
            }
        }
        stage('Pushing Docker Images of consumers'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                 docker push sayedimran/consumer-prod:v1
                 docker push sayedimran/consumer-main:v1
                '''
            }
        }
        stage('Building frontend Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker system prune -f
                    docker build -t sayedimran/microservice-frontend:v1  ./frontend/
                '''
            }
        }
        stage('Pushing the frontend Docker Image'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker push sayedimran/microservice-frontend:v1
                '''
            }
        }
        stage('Cleaning Up the temporary images'){
            agent{
                label 'docker'
            }
            steps{
                sh'''
                    docker system prune -f
                '''
            }
        }
         stage('Stop AWS EC2 Instances') {
              steps {
                  withCredentials([aws(accessKeyVariable:'AWS_ACCESS_KEY_ID',credentialsId:'aws-ec2-creds',secretKeyVaraiable:'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                    aws ec2 stop-instances --instance-ids 	i-072a35f48879eeeab
                    '''
                  }
              }
          }
	stage('Eliminating the existing containers'){
            steps{
                sh'''
                    docker stop frontend product main auth consumer-main consumer-prod
                    docker rm frontend product main auth consumer-main consumer-prod
                    docker rmi sayedimran/micorservice-frontend:v1 sayedimran/consumer-main:v1 sayedimran/main-service:v1 sayedimran/consumer-prod:v1 sayedimran/product-service:v1 sayedimran/auth-service:v1 
                '''
            }
        }
        stage('Pulling the backend and frontend Images'){
            steps{
                sh'''
                    docker pull sayedimran/micorservice-frontend:v1
                    docker pull sayedimran/consumer-main:v1
                    docker pull sayedimran/main-service:v1
                    docker pull sayedimran/consumer-prod:v1
                    docker pull sayedimran/product-service:v1
                    docker pull sayedimran/auth-service:v1
                '''
            }
        }
        stage('Updating the backend and frontend containers'){
            steps{
                sh'''
                  docker run -d --name auth -p 7070:7070 -e MONGO_URI=mongodb://13.233.137.44:27017/ sayedimran/auth-service:v1
                  docker run -d -p 9090:9090 --name main  -e  MONGO_URI=mongodb://13.233.137.44:27017/ -e RABBIT_MQ_URI=13.233.137.44 sayedimran/main-service:v1
                  docker run -d -p 8080:8080 --name product -e  MONGO_URI=mongodb://13.233.137.44:27017/ -e RABBIT_MQ_URI=13.233.137.44 sayedimran/product-service:v1
                  docker run -d --name consumer-main -e MONGO_URI=mongodb://13.233.137.44:27017/ -e RABBIT_MQ_URI=13.233.137.44 sayedimran/consumer-main:v1
                  docker run -d --name consumer-prod -e  MONGO_URI=mongodb://13.233.137.44:27017/ -e RABBIT_MQ_URI=13.233.137.44 sayedimran/consumer-prod:v1
                  docker run -d --name frontend -p 80:80 -e MICROSERVICE_1=http://13.233.137.44:7070 -e MICROSERVICE_2=http://13.233.137.44:8080 -e MICROSERVICE_3=http://13.233.137.44:9090 sayedimran/micorservice-frontend:v1
                '''
            }
        }
    }
}
