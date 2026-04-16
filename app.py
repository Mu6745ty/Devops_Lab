# 1. Import Flask
from flask import Flask, jsonify

# 2. Create Flask app
app = Flask(__name__)


# 3. Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Hello from CI/CD Pipeline!",
        "status": "running"
    })


# 4. Health route
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200


# 5. Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
