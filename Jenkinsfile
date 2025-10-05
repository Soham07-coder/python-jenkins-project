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
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Application & Tests') {
            steps {
                // 1. Run the Flask app in the background (start /b)
                // 2. Wait 5 seconds for the app to start
                // 3. Activate venv and run pytest
                bat 'start /b cmd /c "flask --app app run --port=5001"'
                bat 'timeout /t 5'
                bat '.venv\\Scripts\\activate && pytest'
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
