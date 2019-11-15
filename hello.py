import sys


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi, World!'


if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
