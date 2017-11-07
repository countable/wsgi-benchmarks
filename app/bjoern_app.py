from flask import Flask, jsonify
import bjoern

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({"hello": "world"})


if __name__ == '__main__':
    server.listen(app, "0.0.0.0", 8000)
    bjorn.run()
