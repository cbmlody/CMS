import sys
from flask import Flask, render_template, request, redirect, url_for
from time import strftime as stime
from models import Assignment, Submission, Team, Student, Mentor, Attendance, Checkpoint, Database


# GLOBAL SETTINGS
DEBUG = False
if "--debug" in sys.argv:
    DEBUG = True
elif "--init" in sys.argv:
    Database.import_sql()


app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/assignment')
def assignment():
    assignments_list = Assignment.get_all()
    return render_template('assignment_list.html', assignments=assignments_list)


@app.route('/assignment/<assignment_id>/submit', methods=['GET', 'POST'])
def submit(assignment_id):
    if request.method == "POST":
        user_id = 1
        assignment = Assignment.get_by_id(assignment_id)
        if assignment.as_team:
            team_id = 1
        else:
            team_id = None
        Submission.save(user_id, request.form['link'], assignment.id_, team_id)
        return redirect('/assignment')
    return render_template('submit_ass.html')


@app.route('/assignment/add', methods=['GET', 'POST'])
def add_assignment():
    if request.method == "POST":
        if 'as-team' in request.form:
            as_team = 1
        else:
            as_team = 0
        Assignment.add(request.form['title'], request.form['due-date'], request.form['max-points'], as_team)
        return redirect('/assignment')
    return render_template('assignment_add.html')


@app.route('/submissions')
def submissions():
    submission_list = Submission.get_all()
    submissions = []
    for submission in submission_list:
        submissions.append(Submission.get_table_info(submission))
    return render_template('submissions_list.html', submissions=submissions)


@app.route('/submissions/<submission_id>/grade')
def grade(submission_id):
    return render_template('grade_assignment.html')


@app.route('/student')
def student():
    students = Student.get_all(Student.role)
    cards = {student.id_: Checkpoint.get_card(student.id_) for student in students}
    return render_template('students_view.html', students=students, cards=cards)


@app.route('/student/add', methods=['GET'])
def student_new():
    url = url_for('student_new')
    return render_template('student_mentor_form.html', form_url=url)


@app.route('/student/add', methods=['POST'])
def student_create():
    url = url_for('student_new')
    role = 3
    fullname = request.form['fullname']
    username = request.form['username']
    paswd = request.form['pass']
    rpaswd = request.form['rpass']
    if paswd != rpaswd:
        error = "Passwords does not match"
        return render_template('student_mentor_form.html', form_url=url, error=error)
    else:
        Student(None, username, paswd, fullname, role, None).add()
        return redirect(url_for('student'))


@app.route('/student/<id>/teams', methods=['GET'])
def add_to_team(id):
    teams = Team.get_all()
    return render_template('add_to_team.html', teams=teams)


@app.route('/student/<id>/teams', methods=['POST'])
def assign_to_team(id):
    student = Student.get_by_id(id)
    team_id = request.form['add-to-team']
    student.assign_team(team_id)
    return redirect('student')


@app.route('/student/<id>/delete')
def delete_student(id):
    to_delete = Student.get_by_id(id)
    to_delete.delete()
    return redirect('/student')


@app.route('/student/<id>/grades', methods=['GET'])
def student_grades(id):
    submissions = Submission.get_by_user_id(id)
    assignment_ids = []
    for submission in submissions:
        assignment_ids.append(str(submission.assignment_id))
    assignments = Assignment.get_by_ids(assignment_ids)
    assignments = {assignment.id_: assignment for assignment in assignments}
    return render_template('grades.html', submissions=submissions, assignments=assignments)


@app.route('/student/<id>/attendance')
def student_attendance(id):
    attendances = Attendance.get_by_id(id)
    return render_template('view_attendance.html', attendances=attendances)


@app.route('/mentor')
def mentor():
    mentors = Mentor.get_all(Mentor.role)
    return render_template('mentors_view.html', mentors=mentors)


@app.route('/mentor/add', methods=['GET'])
def mentor_new():
    url = url_for('mentor_new')
    return render_template('student_mentor_form.html', form_url=url)


@app.route('/mentor/add', methods=['POST'])
def mentor_create():
    url = url_for('mentor_new')
    role = 1
    fullname = request.form['fullname']
    username = request.form['username']
    paswd = request.form['pass']
    rpaswd = request.form['rpass']
    if paswd != rpaswd:
        error = "Passwords does not match"
        return render_template('student_mentor_form.html', form_url=url, error=error)
    else:
        Mentor(None, username, paswd, fullname, role, None).add()
        return redirect(url_for('mentor'))


@app.route('/mentor/<id>/delete')
def delete_mentor(id):
    to_delete = Mentor.get_by_id(id)
    to_delete.delete()
    return redirect('/mentor')


@app.route('/change_password', methods=['GET'])
def change_password():
    return render_template('change_password.html')


@app.route('/teams')
def teams():
    teams = Team.get_all()
    return render_template('teams_view.html', teams=teams)


@app.route('/teams/add', methods=['GET'])
def teams_new():
    return render_template('team_add_form.html')


@app.route('/teams/add', methods=['POST'])
def teams_create():
    team_name = request.form['team-name']
    new_team = Team(None, team_name)
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
def attendance_list():
    students = Student.get_all(Student.role)
    return render_template('attendance_view.html', students=students)


@app.route('/attendance', methods=['POST'])
def attendance_listpost():
    date_now = stime("%d-%m-%Y")
    if request.method == 'POST':
        to_parse = request.form
        data = dict(to_parse)
        print(data)
        for key, value in data.items():
            if "present" in value:
                attendance = Attendance(key, date_now, 1)
            else:
                attendance = Attendance(key, date_now, 0)
            attendance.add()
        return redirect(url_for('attendance_list'))


@app.route('/checkpoint', methods=['GET'])
def checkpoint():
    students = Student.get_all(3)
    return render_template('checkpoints_view.html', students=students)


@app.route('/checkpoint/add', methods=['POST'])
def checkpoint_add():
    data = request.form
    data = dict(data)
    for key, value in data.items():
        if 'green' in value:
            Checkpoint.update_user_card('green', key)
        elif 'yellow' in value:
            Checkpoint.update_user_card('yellow', key)
        else:
            Checkpoint.update_user_card('red', key)
    return redirect(url_for('checkpoint'))


if __name__ == "__main__":
    app.run(debug=DEBUG)
