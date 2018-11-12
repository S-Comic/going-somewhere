from flask import render_template, Flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/course/')
def services():
    return render_template('course.html')

@app.route('/about/')
def about():
    return render_template('about.html')
