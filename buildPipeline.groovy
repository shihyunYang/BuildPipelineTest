node {
    env.UNITY_VERSION = '2021.3.6f1'        
    //python_path = "/opt/homebrew/bin/python3"
	python_path = "/usr/local/bin/python3"
    
    echo "environment var"    
    sh "env"    
    
    stage("checkout") {
        checkout scm
        //git url: 'https://github.com/shihyunYang/BuildPipelineTest.git', branch: 'main'
    }

    if(params.BUILD_COMMAND == "build") {
        build_title = "${params.BUILD_NAME}, ${params.BUILD_VERSION}(${params.BUILD_NUMBER})"
        try {
            
            stage('build') {                
                sh "${python_path} -u builder.py"
            }

            //stage("distribute") {
                //sh "${python_path} -u distributer.py ${params.BUILD_NAME}"
            //}
        }
        catch(Exception e) {            
            
        }
    }
}

def sendMessage(String message, String color='#00ff00') {
    echo "${message}"

    if(params.NOTIFY_SLACK == true) {
        slackSend(channel: params.SLACK_CHANNEL_ID, color: color, message: message)
    }
}