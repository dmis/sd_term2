from flask import Flask, request
from time import sleep

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    try:
        sleep(1)
    finally:
        return {'type': 'flask threaded'}


if __name__ == '__main__':
    app.run(threaded=True, port=8889)  # threaded variant
