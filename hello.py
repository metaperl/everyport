import sys
import uuid

from flask import Flask, session


app = Flask(__name__)
app.secret_key = '8asd234ASFASDQ$^^^^$RQAFD' # = str(uuid.uuid1())
print("Secret = {secret}.".format(secret=app.secret_key))


@app.route('/')
def hello_world():
    if 'visits' in session:
        v = session['visits']
    else:
        v = 0
    v += 1
    session['visits'] = v
    return 'Hi, World! {visits}'.format(**session)


if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port)
