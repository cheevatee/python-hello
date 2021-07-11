from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

#print(__name__)

@app.route('/')
def home():
#    return 'Hello Flask!'
#    return render_template('home-hello.html')
    return render_template('home-hello.html', name='Tee')

@app.route('/about')
def about():
    return 'This is a about page'
