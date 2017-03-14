from flask import Flask, render_template, request, redirect, url_for
from models.assignment import Assignment
from models.submission import Submission


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/assignment')
def assignment():
    assignments_list = Assignment.get_all()
    return render_template('assignment_list.html', assignments = assignments_list)

@app.route('/assignment/<assignment_id>/submit',methods=['GET','POST'])
def submit(assignment_id):
    if request.method == "POST":
        user_id =1
        assignment = Assignment.get_by_id(assignment_id)
        if assignment.as_team:
            team_id =1
        else:
            team_id = 'NULL'
        Submission.save(user_id, request.form['link'],'NULL',assignment,team_id)
        return redirect('/assignment')
    return render_template('submit_ass.html')

@app.route('/student')
def student():
    return render_template('students_view.html')


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
