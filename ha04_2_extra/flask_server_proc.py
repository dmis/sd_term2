from flask import Flask, request
from time import sleep

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    try:
        sleep(1)
    finally:
        return {'type': 'flask processed'}


if __name__ == '__main__':
    app.run(threaded=False, processes=4, port=8887)  # processed variant
