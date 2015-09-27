class Assignments():
    assignment_name = ""
    percentile = 0

    def __init__(self, assignment_name, percentile):
        self.assignment_name = assignment_name
        self.percentile = percentile



class User():
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Course():
    course_name = ""
    professor = ""
    assignment = Assignments


    def __init__(self, course_name, professor, assignment):
        self.course_name = course_name
        self.professor = professor
        self.assignment = assignment

    def get_course_name():
        return self.course_name


