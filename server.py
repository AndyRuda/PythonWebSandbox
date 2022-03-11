from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=['POST'])
def hello_world_POST():
    name = request.form['name']
    lastName = request.form['lastName']
    return f"<p>Hello, {name} {lastName} World!</p>" 

