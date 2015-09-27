from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/grade')
def grade():
    return render_template('grade.html')
'''
@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/class')
def myclass():
    return render_template('class.html')

@app.route('/gpa')
def grade():
    return render_template('gpa.html')
'''
if __name__ == '__main__':
    app.run(debug=True)
