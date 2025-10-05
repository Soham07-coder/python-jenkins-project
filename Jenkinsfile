pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from your main branch
                git url: 'https://github.com/Soham07-coder/python-jenkins-project.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                // For Windows agents in Jenkins: Install venv and dependencies
                // Note: Jenkins will run these commands from the project directory.
                bat '"C:\\Users\\soham\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m venv .venv'
                bat '.venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Application & Tests') {
            steps {
                // 1. Activate venv AND start Flask in the background
                // We use 'call' to run the activate script and keep the environment persistent.
                bat 'start "flask_server" /B cmd /c "call .venv\\Scripts\\activate && flask --app app run --port=5001"'
                
                // 2. Use a simple 'ping' command as a robust alternative to 'timeout'
                // Ping waits for 1+ seconds per ping. This waits ~5 seconds.
                bat 'ping -n 6 127.0.0.1 > NUL'
                
                // 3. Activate venv AND run Pytest
                bat 'call .venv\\Scripts\\activate && pytest'
            }
        }
    }
    post {
        // Post-build actions, e.g., cleaning up background process (optional but good practice)
        always {
            // Find and kill the Flask process to free the port for next run
            bat 'taskkill /F /IM python.exe'
        }
    }
}
