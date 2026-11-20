import os
from flask import Flask

app = Flask(__name__)

# Read configuration from environment variables
APP_NAME = os.getenv("APP_NAME", "My DevOps Application")
APP_ENV = os.getenv("APP_ENV", "development")
PORT = int(os.getenv("PORT", 5000))


@app.route("/")
def home():
    return f"""
    <h1>{APP_NAME}</h1>
    <p>Application is running successfully!</p>
    <p>Environment: {APP_ENV}</p>
    <p>Welcome to my Application Maintenance Project.</p>
    """


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "environment": APP_ENV
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False)