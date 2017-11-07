from flask import Flask, jsonify
from meinheld import server

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"hello": "world"})


if __name__ == '__main__':
    server.listen("0.0.0.0", 8000)
    server.run(app) 
