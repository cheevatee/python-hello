from flask import Flask, render_template

app = Flask(__name__)

#print(__name__)

@app.route('/')
def home():
    return 'Hello World!'
#    return render_template('home-hello.html')
#    return render_template('home-hello.html', name='Tee')

@app.route('/about')
def about():
    return 'This is a about page'

if __name__ == '__main__':  # Script executed directly?
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
