# ComputeSolutions/01-Create-WebApp/HelloWorldApp/app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, AZ-204! Web App Created."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)