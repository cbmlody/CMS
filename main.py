from flask import Flask, render_template, request, redirect, url_for
from models import Student, Team, Mentor


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/student')
def student():
    students = Student.get_all(3)
    return render_template('students_view.html', students=students)


@app.route('/change_password', methods=['GET'])
def change_password():
    return render_template('change_password.html')

@app.route('/mentor')
def mentor():
    mentors = Mentor.get_all(1)
    return render_template('mentors_view.html', mentors=mentors)

@app.route('/teams/')
def teams():
    teams = Team.get_all()
    return render_template('teams_view.html', teams=teams)


@app.route('/teams/add', methods=['GET'])
def teams_new():
    return render_template('team_add_form.html')


@app.route('/teams/add', methods=['POST'])
def teams_create():
    team_name = request.form['team_name']
    team = Team(None, team_name)
    for team_db in Team.get_all():
        if team_db.name == team.name:
            error = "Team exists in database!"
    team.add()
    return redirect(url_for('teams'))


@app.route('/mentor/<id>/delete')
def delete_mentor(id):
    to_delete = Mentor.get_by_id(id)
    to_delete.delete()
    return redirect('/student')

@app.route('/student/<id>/delete')
def delete_student(id):
    to_delete = Student.get_by_id(id)
    to_delete.delete()
    return redirect('/student')

@app.route('/mentor/add')
def add_mentor():
    pass

@app.route('/attendance', methods=['GET','POST'])
def attendance_list():
    students = Student.get_all(3)
    if request.method == 'GET':
        return render_template('attendance_view.html', students = students)
    if request.method == 'POST':
        pass

if __name__ == "__main__":
    app.run(debug=True)