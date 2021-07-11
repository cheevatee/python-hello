from flask import Flask, render_template, jsonify
##from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import make_wsgi_app
from flask_prometheus_metrics import register_metrics

app = Flask(__name__)
##metrics = PrometheusMetrics(app)

#print(__name__)

# static information as metric
##metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def home():
#    return 'Hello World!'
#    return render_template('home-hello.html')
    return render_template('home-hello.html', name='Tee')

@app.route('/about')
def about():
    return 'This is a about page'

register_metrics(app, app_version="v0.1.2", app_config="staging")
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

if __name__ == '__main__':  # Script executed directly?
#    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
