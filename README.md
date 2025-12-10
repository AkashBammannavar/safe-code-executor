🛡 Safe Code Executor

A secure API that allows users to run Python code safely inside Docker containers.
The system protects against infinite loops, memory abuse, and internet misuse using Docker security controls.

🚀 Features

✅ Execute Python code inside isolated Docker containers

✅ Time limit protection (10 seconds max)

✅ Memory restriction (128 MB)

✅ Read-only filesystem

✅ No internet access inside containers

✅ Clean Web UI (HTML, CSS)

✅ API-based execution /run endpoint

✅ Safe error handling

✅ Beginner-friendly project

⚙ System Requirements

Docker Desktop installed and running

Python 3.10+

Flask

📂 Folder Structure

safe-code-executor/
│
├── server.py
├── requirements.txt
└── templates/
    └── index.html

🔧 Setup Instructions
1️⃣ Clone the project

    git clone https://github.com/your-username/safe-code-executor.git
    cd safe-code-executor

2️⃣ Install Python dependencies

    pip install -r requirements.txt

3️⃣ Run the server

    python server.py

4️⃣ Open browser

   http://127.0.0.1:5000

🔌 API Usage
POST /run

Send Python code as JSON.

  

  



