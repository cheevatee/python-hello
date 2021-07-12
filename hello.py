import time
import random

from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

endpoints = ('one', 'two', 'three', 'four', 'five', 'error')

@app.route('/')
def home():
    return render_template('home-hello.html', name='Tee')

@app.route('/one')
def one():
    time.sleep(random.random() * 0.2)
    return 'pong'

@app.route('/two')
def two():
    time.sleep(random.random() * 0.4)
    return 'ok'

@app.route('/three')
def three():
    time.sleep(random.random() * 0.6)
    return 'ok'

@app.route('/four')
def four():
    time.sleep(random.random() * 0.8)
    return 'ok'

@app.route('/error')
def oops():
    return ':(', 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, threaded=True)
