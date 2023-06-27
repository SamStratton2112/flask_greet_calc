from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = add(a,b)
    return str(total)

@app.route('/sub')
def sub_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = sub(a,b)
    return str(total)

@app.route('/multi')
def multi_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = mult(a,b)
    return str(total)

@app.route('/div')
def div_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = div(a,b)
    return str(total)
