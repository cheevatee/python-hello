from flask import Flask, render_template
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from flask_prometheus_metrics import register_metrics


app = Flask(__name__)

#print(__name__)

@app.route('/')
def home():
#    return 'Hello Flask!'
#    return render_template('home-hello.html')
    return render_template('home-hello.html', name='Tee')

@app.route('/ping')
def about():
    return 'pong'

register_metrics(app, app_version="v0.1.2", app_config="staging")

## Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {'/metrics': make_wsgi_app()})

if __name__ == '__main__':  # Script executed directly?
#    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
#    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)
    run_simple("0.0.0.0", 8080, app.wsgi_app(), use_reloader=True, use_debugger=True, use_evalex=True,)
