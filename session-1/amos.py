from flask import Flask
app = Flask(__name__)

import requests


@app.route('/')
def cookie():
    response = requests.get("http://127.0.0.1:5000/gayturtle")
    return response.text


if __name__ == '__main__':
    app.run(port=5001)
