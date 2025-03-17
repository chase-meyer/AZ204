# Security/01-Auth-Demo/AuthDemoApp/app.py
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Azure App Service Auth Demo! <a href='/secure'>Go to Secure Page</a>"

@app.route('/secure')
def secure():
    # Check if user is authenticated via App Service headers
    user_id = request.headers.get('X-MS-CLIENT-PRINCIPAL-ID', None)
    if not user_id:
        return "Unauthorized - Please sign in.", 401
    
    # Extract user claims from headers
    claims = {
        "User ID": user_id,
        "Name": request.headers.get('X-MS-CLIENT-PRINCIPAL-NAME', 'Unknown'),
        "Provider": request.headers.get('X-MS-CLIENT-PRINCIPAL-IDP', 'Unknown'),
        "Token": request.headers.get('X-MS-TOKEN-AAD-ID-TOKEN', 'Not shown for brevity')
    }
    
    return f"""
    <h1>Secure Page</h1>
    <p>Welcome, authenticated user!</p>
    <pre>{json.dumps(claims, indent=2)}</pre>
    <a href="/.auth/logout">Logout</a>
    """

@app.route('/api-call')
def api_call():
    token = request.headers.get('X-MS-TOKEN-AAD-ID-TOKEN', None)
    if not token:
        return "No token available - Please sign in.", 401
    return f"Simulated API call with token: {token[:20]}... (truncated)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)