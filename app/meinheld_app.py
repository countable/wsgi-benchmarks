from flask import Flask, render_template
from meinheld import server

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    server.listen("0.0.0.0", 8000)
    server.run(app) 
