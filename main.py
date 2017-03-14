from flask import Flask, render_template, request, redirect, url_for, flash
from models import Student


app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('index.html')


@app.route('/student')
def student():
    students = Student.get_all(3)
    return render_template('students_view.html', students=students)


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


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
