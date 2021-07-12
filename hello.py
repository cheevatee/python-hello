from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)

#print(__name__)

endpoints = ('test', 'ping')

@app.route('/test')
def home():
    return render_template('home-hello.html', name='Test')

@app.route('/ping')
def about():
    return 'pong'

if __name__ == '__main__':  # Script executed directly?
     app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
