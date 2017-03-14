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
