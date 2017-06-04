from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
from binascii import hexlify
from os import urandom
import eval_server

EVAL_SERVER = eval_server.EvalServer()
UID_TABLE = {}


def generate_uid():
    return hexlify(urandom(32)).decode()


@app.route('/result/<uid>')
def result(uid):
    expression = UID_TABLE[uid]
    res = EVAL_SERVER.get_result(expression)
    if res is not None:
        if type(res) == int:
            return "{} = {}".format(expression, res)
        else:
            return "Something is wrong. Don't use ascii letters and check your syntax."
    return "{} is evaluating".format(expression)


@app.route("/")
def mainpage():
    return render_template("mainpage.html", path=request.url)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        expression = request.form['nm']
        uid = generate_uid()
        UID_TABLE[uid] = expression
        EVAL_SERVER.eval(expression)
        return redirect(url_for('result', uid=uid))


if __name__ == '__main__':

    app.run(host="0.0.0.0")

