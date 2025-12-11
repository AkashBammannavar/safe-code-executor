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
    
![requrements](https://github.com/user-attachments/assets/784779c1-7ff4-4aeb-a833-004d88aad07c)


3️⃣ Run the server

    python server.py

    ![torun](https://github.com/user-attachments/assets/b18865be-eb06-4fbf-bb99-d34ebfdd9b21)


4️⃣ Open browser

   http://127.0.0.1:5000

   ![torunpython](https://github.com/user-attachments/assets/6f8f327e-903a-4762-bb21-bb7e9b4a8a06)


🔌 API Usage
POST /run

Send Python code as JSON.

  ✅ Example Request:

1. {
        print(2+2)
    }


  ![t2](https://github.com/user-attachments/assets/8fca251b-84ab-444d-b48a-498097f374ca)

2.

    ![T3](https://github.com/user-attachments/assets/0a1d9826-15c9-4016-8d7e-6021dd43b265)


🔐 Security Implementations

        Protection	Description

        Timeout	Kill execution after 10 seconds
        
        Memory Limit	128 MB enforced
        
        Network	No internet access    
        
        Filesystem	Read-only
        
        Isolation	Runs inside container
        
        Error Handling	Clean error responses


🧪 Safety Tests

 Infinite Loop Protection     while True:
                                  pass

    
    ![tt1](https://github.com/user-attachments/assets/99bda2fd-a012-4b80-aa3d-b44f8cea09f1)


Memory Attack Blocked

    ![t4](https://github.com/user-attachments/assets/e402424d-62ea-456a-a584-64b0786f3756)

Network Blocked

    ![t5](https://github.com/user-attachments/assets/bb29e9fe-d46c-4467-ba8d-44f023ebf918)


Write Protection

    ![t5](https://github.com/user-attachments/assets/9bc00f79-b20b-4314-a9c5-b5778c02cb82)

Read Test

    ![T6](https://github.com/user-attachments/assets/ac0522c4-c1f8-4d1c-83a3-54207700187d)

📘 What I Learned

Why executing untrusted code is dangerous

How Docker isolates environments

Real-world sandboxing basics

Limits of container security

Docker is not a full sandbox

Importance of memory & time control

How to deploy APIs securely

📦 Docker Hub Image

![dockerhubsafecose](https://github.com/user-attachments/assets/4b4aef96-6e9e-4855-82c6-c2198411e6d3)

