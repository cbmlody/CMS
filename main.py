from flask import Flask, render_template, request, redirect, url_for
from models import Student


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


if __name__ == "__main__":
    app.run(debug=True)
