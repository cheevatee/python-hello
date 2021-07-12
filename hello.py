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

@app.route('/ping')
def about():
    return 'pong'

@app.route('/one')
def first_route():
    time.sleep(random.random() * 0.2)
    return 'ok'

@app.route('/error')
def oops():
    return ':(', 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True, use_reloader=True)

