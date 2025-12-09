from flask import Flask, request, jsonify, render_template
import subprocess
import tempfile
import os

app = Flask(__name__)

MAX_CODE_LENGTH = 5000


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()

    if "code" not in data:
        return jsonify({"error": "Missing code"}), 400

    code = data["code"]

    if len(code) > MAX_CODE_LENGTH:
        return jsonify({"error": "Code too long (max 5000 characters)"}), 400

    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as f:
        f.write(code.encode())
        file_path = f.name

    docker_cmd = [
        "docker", "run", "--rm",
        "--network", "none",
        "--memory", "128m",
        "--cpus", "1.0",
        "--pids-limit", "64",
        "--read-only",
        "-v", f"{file_path}:/app/code.py:ro",
        "python:3.11-slim",
        "python", "/app/code.py"
    ]

    try:
        result = subprocess.run(
            docker_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
        )

        output = result.stdout.decode().strip()
        error = result.stderr.decode().strip()

        if error:
            return jsonify({"error": error})

        return jsonify({"output": output})

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Execution timed out after 10 seconds"})

    finally:
        os.remove(file_path)


if __name__ == "__main__":
    app.run(debug=True)
