# -*- coding:utf-8 -*-
from bottle import Bottle, run


app = Bottle()


@app.hook('before_request')
def hello():
    print 'hello before_request'


@app.route('/hello')
def hello2():
    return 'hello hello'


run(app, host='localhost', port=8080, reloader=True)

