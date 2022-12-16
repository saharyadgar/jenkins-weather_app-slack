pipeline {
    agent any

    environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
	}

    stages {
        stage(‘Clean’) {
            steps {
                sh 'sudo docker system prune -a --volumes -f'
            }
        }
        
        stage(‘Build’) {
            agent {
                label 'agent1'
            }
            steps {
                sh 'sudo docker-compose build'
            }
        }

        stage(‘Deploy_agent1’) {
            agent {
                label 'agent1'
            }
            steps {
                sh 'sudo docker-compose up -d'
                sh 'sleep 5'
            }
        }

        stage(‘Test’) {
            agent {
                label 'agent1'
            }
            steps {
                sh 'python3 test_main.py'
            }
        }
        
        stage('Login_agent1') {
            agent {
                label 'agent1'
            }
			steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
    }
        stage('Push') {
            agent {
                label 'agent1'
            }
			steps {
				sh 'docker tag web_app:1.0 saharyadgar/sahar_repo:web_app'
                sh 'docker tag proxy_server saharyadgar/sahar_repo:proxy_server'
                    
                sh 'docker push saharyadgar/sahar_repo:web_app'
                sh 'docker push saharyadgar/sahar_repo:proxy_server'

			    }
            }
    
        stage('Deploy_agent2') {
            agent {
                label 'agent2'
            }
			steps { 
                sh 'docker-compose up -d'
			    }
        }
    
    }

    post{
        success{
            slackSend( channel: "#succeeded-build", token: "slack", message: "build number: ${env.BUILD_NUMBER} succeeded!")
        }
        
        failure{
            slackSend( channel: "#devops-alert", token: "slack", message: "Pipeline failed...")
        }

        always {
            sh 'sudo docker-compose down --remove-orphans -v'
        }
        
    }
}
