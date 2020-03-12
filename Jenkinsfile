pipeline {
	agent any
	    stages {
	        stage('Check who the user is ') {
	        /* Cloning the repository to our workspace */
		        steps {
		        	echo whoami
		        }
		    }

	        stage('Cloning Source Repository') {
	        /* Cloning the repository to our workspace */
		        steps {
		        	checkout scm
		        }
	   		}

		   stage('Stop and Remove old container') {
		        steps {

                sh '''
                    sudo docker container stop asmiflaskapp
                    sudo docker container rm asmiflaskapp
                '''
		        }
		   }

		   stage('Remove old image and build new one') {
		        steps {
		        sh 'sudo docker image rm alpine-flask:1.0.0'
		        sh 'sudo docker build -t alpine-flask:1.0.0 .'
		        }
		   }

		   stage('Run Image') {
		        steps {
		        sh 'sudo docker run -d -p 5000:4000 --name asmiflaskapp alpine-flask:1.0.0'
		        }
		   }
		   stage('Testing'){
		        steps {
		            echo 'Testing..'
		            }
		   }

    	}
}