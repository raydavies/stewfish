from flask import Flask
import oauth2 as oauth
import os

app = Flask(__name__)

@app.route("/")
def index():
    consumer = oauth.Consumer(
        os.environ.get("TWITTER_API_KEY"),
        os.environ.get("TWITTER_API_SECRET")
    )
    client = oauth.Client(consumer)

    url = "https://api.twitter.com/1.1/search/tweets.json?q=covfefe"
    resp, content = client.request(url, "GET")
    return content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
