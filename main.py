from flask import Flask, render_template, request, redirect, url_for
from models.assignment import Assignment


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
    return render_template(assignments_list.html, assignments = assignments_list)



@app.route('/student')
def student():
    return render_template('students_view.html')


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)
