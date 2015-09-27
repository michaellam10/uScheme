from flask import *
import jinja2, os
app = Flask(__name__)


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def render(template, **params):
    return render_template(render_str(template, **params))

@app.route('/')
def index():
    submit = request.args.get("in")
    email = request.args.get("email")
    password = request.args.get("password")
    if submit:
        return redirect(url_for('grade'))
    return render_template('homepage.html')

@app.route('/grade')
def grade():

    return render_template('grade.html')
'''
@app.route('/main')
def landingPage():
    return render_template('landingPage.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/class')
def myclass():
    course_data = Course.get_course_name()
    return render_template('class.html', course_data)

@app.route('/gpa')
def grade():
    return render_template('gpa.html')
'''
if __name__ == '__main__':
    app.run(debug=True)
