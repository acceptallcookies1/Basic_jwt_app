from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

# Fake user database
fake_users_db = {
    "john_doe": "password123",
    "alice": "mypassword"
}

# Homepage route
@app.route("/")
def home():
    return "Welcome to the Basic JWT App!"

# Login route
@app.route("/login", methods=["POST"])
def login():
    # Get the JSON data from the request
    data = request.get_json()
    
    # Check if username and password are provided
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    # Validate the credentials
    if username in fake_users_db and fake_users_db[username] == password:
        return jsonify({"message": f"Welcome, {username}!"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
