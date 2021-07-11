from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
#metrics = PrometheusMetrics(app)

#metrics.info('app_info', 'Application info', version='1.0.3')

#print(__name__)

@app.route('/')
def home():
#    return 'Hello Flask!'
#    return render_template('home-hello.html')
    return render_template('home-hello.html', name='Tee')

@app.route('/test')
def about():
    return 'Hello test'

@app.route('/metrics/')
def metrics():
    return PrometheusMetrics(app)

if __name__ == '__main__':  # Script executed directly?
#    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
     app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
