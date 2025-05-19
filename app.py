from flask import Flask, render_template, request, redirect
from database import create_table, insert_student, fetch_students

app = Flask(__name__)
create_table()

@app.route('/')
def index():
    students = fetch_students()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    marks = request.form['marks']
    grade = request.form['grade']
    insert_student(name, email, phone, marks, grade)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
