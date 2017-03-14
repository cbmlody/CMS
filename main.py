from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/student')
def student():
    return render_template('students_view.html')

if __name__ == "__main__":
    app.run(debug=True)
