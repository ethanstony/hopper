from flask import Flask
import raw
import topten

app = Flask(__name__)

@app.route("/<ticker>")
def sendRes(ticker):
    return raw.sendRaw(ticker)

# returns top ten gainers for sidebar
@app.route("/topTen")
def sendTopTen():
    return topten.getTopTen()