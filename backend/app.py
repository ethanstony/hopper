from flask import Flask
import raw
import topten

app = Flask(__name__)

@app.route("/")
def sendRes():
    return raw.sendRaw()

# returns top ten gainers for sidebar
@app.route("/topTen")
def sendTopTen():
    return topten.getTopTen()