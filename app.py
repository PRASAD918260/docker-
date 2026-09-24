from flask import Flask
import shutil

app = Flask(__name__)

@app.route("/")
def home():
    return "Python DevOps application is running"

@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "python-devops-app"
    }

@app.route("/disk")
def disk_usage():
    total, used, free = shutil.disk_usage("/")

    return {
        "total_gb": round(total / (1024 ** 3), 2),
        "used_gb": round(used / (1024 ** 3), 2),
        "free_gb": round(free / (1024 ** 3), 2)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)