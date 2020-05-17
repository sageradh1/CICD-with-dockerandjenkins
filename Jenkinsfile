pipeline {
	agent any
	    stages {


	        stage('Cloning Source Repository') {
	        /* Cloning the repository to our workspace */
		        steps {
		        	checkout scm
		        }
	   		}

			/* For first run there is no need to remove old images and container */


		   stage('Build first image') {
		        steps {
		        	sh 'sudo docker build -t asmi-clothing-backend:1.0.0 Dockerfile'
		        }
		   }

			/* For later runs*/
		//    stage('Stop and Remove old container') {
		//         steps {

        //         sh '''
        //             sudo docker container stop asmi-clothing-api-app
        //             sudo docker container rm asmi-clothing-api-app
        //         '''
		//         }
		//    }

		//    stage('Remove old image and build new one') {
		//         steps {
		//         sh 'sudo docker image rm asmi-clothing-backend:1.0.0'
		//         sh 'sudo docker build -t asmi-clothing-backend:1.0.0 .'
		//         }
		//    }

		   stage('Run Image') {
		        steps {
		        	sh 'sudo docker run -d -p 5000:4000 --name asmi-clothing-api-app asmi-clothing-backend:1.0.0'
		        }
		   }
		   stage('Testing'){
		        steps {
		            echo 'Testing..'
		        }
		   }

    	}
}