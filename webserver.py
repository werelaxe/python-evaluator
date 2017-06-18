from flask import Flask, redirect, url_for, request, render_template
from binascii import hexlify
from os import urandom
import eval_server
from datetime import datetime

app = Flask(__name__)
EVAL_SERVER = eval_server.EvalServer()
UID_TABLE = {}


def create_database_table():
    eval_database = EVAL_SERVER.database()
    lst = map(lambda itm: (itm[0],) + itm[1], UID_TABLE.items())
    return map(lambda itm: (itm[0], itm[1], itm[2], itm[3], str(eval_database[itm[1]].done())), lst)


def generate_uid():
    return hexlify(urandom(32)).decode()


@app.route('/result/<uid>')
def result(uid):
    expression = UID_TABLE[uid][0]
    res = EVAL_SERVER.get_result(expression)
    done = "true"
    if res is not None:
        result = "{} = {}".format(expression, res)
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
        UID_TABLE[uid] = expression, request.remote_addr, datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        EVAL_SERVER.eval(expression)
        return redirect(url_for('result', uid=uid))
