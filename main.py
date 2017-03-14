from flask import Flask, render_template, request, redirect, url_for
from models import Student, Team


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


if __name__ == "__main__":
    app.run(debug=True)