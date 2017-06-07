from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
from binascii import hexlify
from os import urandom
import eval_server

EVAL_SERVER = eval_server.EvalServer()
UID_TABLE = {}
SUPPORTED_TYPES = [int, str, float, complex, bool]


def create_database_table():
    eval_database = EVAL_SERVER.database()
    return map(lambda itm: (itm[0], itm[1], str(eval_database[itm[1]].done())), UID_TABLE.items())


def generate_uid():
    return hexlify(urandom(32)).decode()


@app.route('/result/<uid>')
def result(uid):
    expression = UID_TABLE[uid]
    res = EVAL_SERVER.get_result(expression)
    done = "true"
    if res is not None:
        if type(res) in SUPPORTED_TYPES:
            result = "{} = {}".format(expression, res)
        else:
            result = "Something is wrong. Check your syntax."
    else:
        result = "{} is evaluating".format(expression)
        done = "false"
    return render_template("result_page.html", path=request.url_root, result=result, done=done)


@app.route("/")
def main_page():
    return render_template("main_page.html", path=request.url)


@app.route("/database")
def statistics():
    return render_template("database_table.html", table=create_database_table())


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

