from flask import Flask
import raw

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/sendRaw")
def sendRes():
    return raw.sendRaw()
