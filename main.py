from flask import Flask, render_template, request, redirect, url_for
from models import Student, Mentor


app = Flask(__name__)


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


@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/mentor')
def mentor():
    mentors = Mentor.get_all(1)
    return render_template('mentors_view.html', mentors=mentors)

@app.route('/change_password')
def change_password():
    pass

@app.route('<todo>/delete')
def delete(todo):
    pass



if __name__ == "__main__":
    app.run(debug=True)
