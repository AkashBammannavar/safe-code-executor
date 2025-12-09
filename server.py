from flask import Flask, request, jsonify
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Safe Code Executor API is running!"

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data.get("code", "")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as f:
        f.write(code)
        temp_path = f.name

    try:
        docker_command = [
            "docker", "run", "--rm",

            "--memory=128m",        # Block memory abuse
            "--cpus=1",             # Limit CPU
            "--network", "none",    # Disable internet
            "--read-only",          # Block file writes

            "-v", f"{temp_path}:/app.py:ro",
            "python:3.11-slim",
            "python", "/app.py"
        ]

        result = subprocess.run(
            docker_command,
            capture_output=True,
            text=True,
            timeout=10
        )

        output = result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out after 10 seconds"}), 408

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
