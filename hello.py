import sys
import uuid

from flask import Flask, session


app = Flask(__name__)
app.secret = str(uuid.uuid1)
print("Secret = {secret}.".format(secret=app.secret))


@app.route('/')
def hello_world():
    if 'visits' not in session:
        v = 0
    v += 1
    session['visits'] = v
    return 'Hi, World! {visits}'.format(**session)


if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
