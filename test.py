import requests
from requests.auth import HTTPBasicAuth
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a decorator for requiring authentication
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'message': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated

# Function to validate the username and password
def check_auth(username, password):
    # Add your own logic to validate the credentials
    # For example, you could check against a database of users
    # or validate against a third-party authentication service
    valid_username = 'admin'
    valid_password = 'password'
    return username == valid_username and password == valid_password

# Protected API endpoint
@app.route('/api/protected', methods=['GET'])
@requires_auth
def protected_endpoint():
    return jsonify({'message': 'You are authorized to access this endpoint'})

# Unprotected API endpoint
@app.route('/api/unprotected', methods=['GET'])
def unprotected_endpoint():
    return jsonify({'message': 'This endpoint does not require authentication'})

if __name__ == '__main__':
    app.run()
