from flask import Flask, render_template

app = Flask(__name__)

#print(__name__)

@app.route('/')
def home():
#    return 'Hello Flask!'
#    return render_template('home-hello.html')
    return render_template('home-hello.html', name='Tee')

@app.route('/about')
def about():
    return 'This is a about page'
