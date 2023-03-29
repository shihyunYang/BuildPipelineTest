node {
    env.UNITY_VERSION = '2021.3.6f1'        
    //python_path = "/opt/homebrew/bin/python3"
	python_path = "/usr/local/bin/python3"
    
    echo "environment var"    
    sh "env"    
    
    stage("checkout") {
        checkout scm
        //git url: 'https://hongjeongtae@bitbucket.org/projectball/client.git', branch: 'develop'
    }

	echo "build-test"    
    if(params.BUILD_COMMAND == "build") 
	{
		echo "build-test2"    
        build_title = "${params.BUILD_NAME}, ${params.BUILD_VERSION}(${params.BUILD_NUMBER})"
        try {
            
            stage('build') {                
                sh "${python_path} -u builder.py"
            }

            stage("distribute") {
                sh "${python_path} -u distributer.py"
            }
        }
        catch(Exception e) {            
            sendMessage("[빌드 실패] - ${build_title}", '#ff0000')
			echo "build-test3"   
        }
    }
	echo "build-test1"   
}

def sendMessage(String message, String color='#00ff00') {
    echo "${message}"
}