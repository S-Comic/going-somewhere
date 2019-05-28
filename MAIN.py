from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pizza')
def pizza():
    return render_template('pizza.html')
