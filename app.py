import os

from flask import *

app = Flask(__name__)


def read_student_data():
    with open(os.path.join('Database', 'students.json'), 'r') as studentFile:
        return json.loads(studentFile.read())


def update_student_data(data):
    with open(os.path.join('Database', 'students.json'), 'w+') as studentFile:
        studentFile.write(json.dumps(data))


@app.route('/')
def homepage():
    return render_template('index.html', title='Gramener Flask App')


@app.route('/add-student', methods=['POST'])
def add_student():
    name, age, gender = request.get_json()['name'], request.get_json()['age'], request.get_json()['gender']
    data = read_student_data()
    if not data:
        data = []
        update_student_data(data)
    data.append({'name': name, 'age': age, 'gender': gender})
    update_student_data(data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/get-students')
def get_students():
    return json.dumps(read_student_data()), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5656, debug=True)
