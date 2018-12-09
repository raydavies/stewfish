from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get('https://twitter.com/')
    return r.url

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
