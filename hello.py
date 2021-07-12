import time
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

#print(__name__)

endpoints = ('test', 'ping')

@app.route('/test')
def home():
    return 'test'

@app.route('/ping')
def about():
    return 'pong'

if __name__ == '__main__':  # Script executed directly?
     app.run(host="0.0.0.0", port=5000, threaded=True, debug=True,use_reloader=True)
