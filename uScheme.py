from flask import *
import jinja2, os
from gpaCalc import *
import re

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
	print(email)

	if submit:
		return redirect(url_for('landingPage'))
	return render_template('homepage.html')

@app.route('/main')
def landingPage():
	return render_template('landingpage.html')

@app.route('/gpa')
def gpa():
	submit = request.args.get("submit-gpa")
	grade = request.values.getlist('grade')
	creditHr = request.values.getlist('creditHr')

	length = len(creditHr)
	grade_point = 0
	total_hour = 0
	for i in range(length):
		if grade[i] == '' or creditHr[i] == '':
			continue
		print (grade[i], creditHr[i])
		grade_point += float(grade[i]) * float(creditHr[i])
		total_hour += float(creditHr[i])


	print (grade_point, total_hour)
	if total_hour and grade_point:
		gpa = grade_point / total_hour

		# pair = list(zip(creditHr,grade))
		gpa = round(gpa,2)

		return render_template('gpa.html', gpa=gpa)
	return render_template('gpa.html')

@app.route('/map')
def map():
	return render_template('maps.html')
'''
@app.route('/schedule')
def schedule():
	return render_template('schedule.html')


@app.route('/class')
def myclass():
	course_data = Course.get_course_name()
	return render_template('class.html', course_data)
@app.route('/grade')
def grade():
	return render_template('grade.html')

'''
if __name__ == '__main__':
	app.run(debug=True)
