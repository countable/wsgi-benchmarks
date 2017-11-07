from flask import Flask, render_template
import bjoern

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    server.listen(app, "0.0.0.0", 8000)
    bjorn.run()
