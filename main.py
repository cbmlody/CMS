import sys
from flask import Flask, render_template, request, redirect, url_for, session, g
from time import strftime as stime
from models import Assignment, Team, Attendance, Checkpoint, User, Submission, CheckpointGrades
from models.database import init_db
import os
from functools import wraps


app = Flask(__name__)
app.secret_key = os.urandom(24)


# ------------------------------------------LOGIN PAGE SIDE----------------------------------------------------#

def security(f):
    """Creates a security decorator checking session"""

    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('username'):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))

    return decorated


@app.context_processor
def inject_user():
    """Returns object of current user"""
    return dict(user=g.user)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main login page, checks if login and username are correct(whether it exists in database)"""
    if request.method == 'POST':
        for user in User.get_all():
            if request.form['username'] == user.login and request.form['password'] == user.password:
                session['username'] = request.form['username']
                session['password'] = request.form['password']
                session['id'] = user.id
                session['role'] = user.role_id
                return redirect(url_for('protected'))
        error = "Wrong username or password!"
        return render_template('index.html', error=error)
    if request.method == 'GET':
        if not g.user:
            return render_template('index.html')
        else:
            return redirect('/main')


@app.route('/protected')
def protected():
    """If user is logged in, it shows only his personal todo items list"""
    if g.user:
        return redirect(url_for('main'))
    return redirect(url_for('index'))


@app.before_request
def before_request():
    """Method nothing return it's used to register username before user request"""
    g.user = None
    if 'username' in session:
        g.user = User.get_by_login(session['username'])


@app.route('/getsession')
def getsession():
    """Method returns username of current logged user"""
    if 'username' in session:
        return '{}: {} level of access'.format(session['username'], session['role'])
    return 'Not logged in'


@app.route('/dropsession')
def dropsession():
    """Method is used to drop session of logged in user"""
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    """Method is used to logout user, it uses /dropsession method"""
    return redirect(url_for('dropsession'))


# --------------------------------------------- CONTENT --------------------


@app.route('/main', methods=['GET', 'POST'])
def main():
    """For logged user returns main page, otherwise redirects to login"""
    if g.user:
        return render_template('main.html')
    return render_template('index.html')


@app.route('/login')
def login():
    """Allows user to log in"""
    return render_template('index.html')


@app.route('/assignment')
@security
def assignment():
    """Returns a page with list of assignments"""
    assignments_list = Assignment.get_all()
    return render_template('assignment_list.html', assignments=assignments_list)


@app.route('/assignment/<assignment_id>/submit', methods=['GET', 'POST'])
@security
def submit(assignment_id):
    """Allows a student to submit an assignment"""
    if request.method == "POST":
        assignment = Assignment.get_by_id(assignment_id)
        if assignment.as_team:
            team_id = g.user.team_id
        else:
            team_id = None
        Submission.save(g.user.id, request.form['link'], assignment.id, team_id)
        return redirect('/assignment')
    return render_template('submit_ass.html', assignment_id=assignment_id)


@app.route('/assignment/add', methods=['GET', 'POST'])
@security
def add_assignment():
    """Allows mentor to add an assignment"""
    if request.method == "POST":
        if 'as-team' in request.form:
            as_team = 1
        else:
            as_team = 0
        Assignment(request.form['title'], request.form['due-date'], request.form['max-points'], as_team).add()

        return redirect('/assignment')
    return render_template('assignment_add.html')


@app.route('/submissions')
@security
def submissions():
    """Returns a page with list of submissions"""
    if g.user.role_id < 3:
        submission_list = Submission.get_all()
    else:
        submission_list = Submission.get_by_user_id(g.user.id)
    return render_template('submissions_list.html', submissions=submission_list)


@app.route('/submissions/<submission_id>/grade')
@security
def grade(submission_id):
    """Shows a commercial of our premium DLC"""
    return render_template('grade_assignment.html')


@app.route('/student')
@security
def student():
    """Returns a page with list of students"""
    students = User.get_all(User.STUDENT_ROLE)
    cards = {student.id: CheckpointGrades.get_user_checkpoints(student.id) for student in students}
    return render_template('students_view.html', students=students, cards=cards, user=g.user)


@app.route('/student/add', methods=['GET'])
@security
def student_new():
    """Allows mentor or manager to add new student"""
    url = url_for('student_new')
    if g.user.role_id == 3:
        return redirect('error_404')
    else:
        return render_template('student_mentor_form.html', form_url=url)


@app.route('/student/add', methods=['POST'])
@security
def student_create():
    """Gets new student's data from add form"""
    url = url_for('student_new')
    fullname = request.form['fullname']
    username = request.form['username']
    paswd = request.form['pass']
    rpaswd = request.form['rpass']
    if paswd != rpaswd:
        error = "Passwords does not match"
        return render_template('student_mentor_form.html', form_url=url, error=error)
    else:
        User(username, paswd, fullname, User.STUDENT_ROLE, None).add()
        return redirect(url_for('student'))


@app.route('/student/<id>/teams', methods=['GET'])
@security
def add_to_team(id):
    """Allows mentor to assign student to a certain team"""
    teams = Team.get_all()
    return render_template('add_to_team.html', teams=teams)


@app.route('/student/<id>/teams', methods=['POST'])
@security
def assign_to_team(id):
    """Assigns student to a certain team"""
    student = User.get_by_id(id)
    try:
        team_id = request.form['add-to-team']
        student.assign_team(team_id)
    except Exception:
        pass
    return redirect('student')


@app.route('/student/<id>/delete')
@security
def delete_student(id):
    """Allows mentor to remove certain student"""
    if g.user.role_id == 3:
        return redirect('error_404')
    else:
        to_delete = User.get_by_id(id)
        to_delete.delete()
        return redirect('/student')


@app.route('/student/<id>/grades', methods=['GET'])
@security
def student_grades(id):
    """Returns a page with certains student's grades"""
    submissions = Submission.get_by_user_id(id)
    assignment_ids = []
    for submission in submissions:
        assignment_ids.append(str(submission.assignment_id))
    assignments = Assignment.get_by_ids(assignment_ids)
    assignments = {assignment.id: assignment for assignment in assignments}
    if g.user.role_id == 3 and g.user.id != int(id):
        return redirect('error_404')
    return render_template('grades.html', submissions=submissions, assignments=assignments)


@app.route('/student/<id>/attendance')
@security
def student_attendance(id):
    """Returns a page with a certain student's attendance history"""
    attendances = Attendance.get_by_id(id)
    if (g.user.role_id == 3 and g.user.id != int(id)):
        return redirect('error_404')
    return render_template('view_attendance.html', attendances=attendances)


@app.route('/mentor')
@security
def mentor():
    """Returns a page with the list of all mentors"""
    mentors = User.get_all(User.MENTOR_ROLE)
    return render_template('mentors_view.html', mentors=mentors)


@app.route('/mentor/add', methods=['GET'])
@security
def mentor_new():
    """Allows manager to add new mentor"""
    url = url_for('mentor_new')
    if g.user.role_id == 0:
        return render_template('student_mentor_form.html', form_url=url)
    else:
        return redirect('error_404')


@app.route('/mentor/add', methods=['POST'])
@security
def mentor_create():
    """Gets new mentor's data from a form"""
    url = url_for('mentor_new')
    fullname = request.form['fullname']
    username = request.form['username']
    paswd = request.form['pass']
    rpaswd = request.form['rpass']
    if paswd != rpaswd:
        error = "Passwords does not match"
        return render_template('student_mentor_form.html', form_url=url, error=error)
    else:
        User(username, paswd, fullname, User.MENTOR_ROLE, None).add()
        return redirect(url_for('mentor'))


@app.route('/mentor/<id>/delete')
@security
def delete_mentor(id):
    """Allows manager to remove a mentor"""
    if g.user.role_id == 0:
        to_delete = User.get_by_id(id)
        to_delete.delete()
        return redirect('/mentor')
    else:
        redirect('error_404')


@app.route('/change_password', methods=['GET', 'POST'])
@security
def change_password():
    """Allows user to change his password"""
    if request.method == 'GET':
        return render_template('change_password.html')
    else:
        password = request.form['password']
        repeat_pass = request.form['rpassword']
        user = inject_user()
        user_obj = None
        for key, value in user.items():
            user_obj = value
        change_pass = user_obj.change_password(password, repeat_pass)
        return render_template('change_password.html', change_pass=change_pass)


@app.route('/teams')
@security
def teams():
    """Returns a page with list of all teams"""
    teams = Team.get_all()
    return render_template('teams_view.html', teams=teams)


@app.route('/teams/add', methods=['GET'])
@security
def teams_new():
    """Allows mentor to create new team"""
    if g.user.role_id == 3:
        return redirect('error_404')
    else:
        return render_template('team_add_form.html')


@app.route('/teams/add', methods=['POST'])
@security
def teams_create():
    """Gets new team data from a form"""
    team_name = request.form['team-name']
    new_team = Team(team_name)
    exists = None
    for team in Team.get_all():
        if new_team.name == team.name or len(new_team.name) == 0:
            exists = True
    if exists:
        error = "Team exists or you provide empty team name!"
        return render_template('team_add_form.html', error=error)
    else:
        new_team.add()
        return redirect(url_for('teams'))


@app.route('/attendance')
@security
def attendance_list():
    """Allows mentor to check attendance"""
    if g.user.role_id == 3:
        return redirect(page_not_found)
    else:
        students = User.get_all(User.STUDENT_ROLE)
        return render_template('attendance_view.html', students=students)


@app.route('/attendance', methods=['POST'])
@security
def attendance_listpost():
    """Gets attendance check data"""
    date_now = stime("%d-%m-%Y")
    if request.method == 'POST':
        to_parse = request.form
        data = dict(to_parse)
        for key, value in data.items():
            if "present" in value:
                Attendance(key, date_now, 1).add()
            else:
                Attendance(key, date_now, 0).add()
        return redirect(url_for('student'))


@app.route('/checkpoint', methods=['GET'])
@security
def checkpoint():
    """Returns a webpage with list of checkpoints, allowing mentor or manager to grade"""
    if g.user.role_id < 2:
        checkpoints = Checkpoint.get_all()
        return render_template('checkpoints_list.html', checkpoints=checkpoints)
    else:
        return redirect('error_404')


@app.route('/checkpoint/grade/<checkpoint_id>', methods=['GET'])
@security
def checkpoint_grade(checkpoint_id):
    """Returns a webpage with list of checkpoints, allowing mentor or manager to grade"""
    if g.user.role_id < 2:
        students = User.get_all(User.STUDENT_ROLE)
        return render_template('checkpoints_grade.html', students=students, checkpoint_id=checkpoint_id)
    else:
        return redirect('error_404')


@app.route('/checkpoint/grade/<checkpoint_id>', methods=['POST'])
@security
def checkpoint_grade_post(checkpoint_id):
    """Gets checkpoints data from form to update students grades"""
    data = request.form
    data = dict(data)
    for key, value in data.items():
        CheckpointGrades(key, checkpoint_id, value[0]).grade()

    return redirect(url_for('checkpoint'))


@app.route('/checkpoint/add', methods=['GET'])
@security
def checkpoint_add():
    if g.user.role_id < 2:
        return render_template('checkpoint_add.html')
    else:
        return redirect(url_for('error_404'))


@app.route('/checkpoint/add', methods=['POST'])
@security
def checkpoint_add_post():
    description = request.form['description']
    date = request.form['date']
    error = None
    if description == "" or date=="":
        error = "Fields cannot be empty"
        return render_template('checkpoints_list.html', error=error)
    else:
        Checkpoint(description, date).add()
        return redirect(url_for('checkpoint'))


@app.route('/404')
def error_404():
    return render_template('404.html')


@app.errorhandler(404)
def page_not_found(e):
    """Returns our own not existing page template"""
    return redirect(url_for('error_404'))


if __name__ == "__main__":
    # GLOBAL SETTINGS
    DEBUG = False
    if "--debug" in sys.argv:
        DEBUG = True
    if "--init" in sys.argv:
        init_db()
    app.run(debug=DEBUG)
