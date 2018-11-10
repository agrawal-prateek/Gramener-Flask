import os

from flask import *

# Create Flask Object
app = Flask(__name__)


def read_student_data():
    """
    Function to Get Students data from the Database
    :return: A List object contains students data
    """
    with open(os.path.join('Database', 'students.json'), 'r') as studentFile:
        return json.loads(studentFile.read())


def update_student_data(data):
    """
    Function to update data of students in the database
    :param data: A List object contains students data
    :return: None
    """
    with open(os.path.join('Database', 'students.json'), 'w+') as studentFile:
        studentFile.write(json.dumps(data))


@app.route('/')
def homepage():
    """
    Function to Render the Homepage
    """
    return render_template('index.html', title='Gramener Flask App')


@app.route('/add-student', methods=['POST'])
def add_student():
    """
    Function Which takes student data from post method and Appends it to database
    :return: A Response Object with Response code 200
    """

    # Get the Data from Request Object
    name, age, gender = request.get_json()['name'], request.get_json()['age'], request.get_json()['gender']

    # Read Students data from Database
    data = read_student_data()

    # If No data in Database or database is corrupted, Initialize it as empty
    if not data:
        data = []
        update_student_data(data)

    # Append data got by post method
    data.append({'name': name, 'age': age, 'gender': gender})

    # Write Data to Database
    update_student_data(data)

    # Return Response Object
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/get-students')
def get_students():
    """
    Function to Get Students data from the Database
    :return: A Response object contains students data with response code 200
    """
    return json.dumps(read_student_data()), 200, {'ContentType': 'application/json'}


if __name__ == '__main__':
    # Run Application by allowing Remote access
    # Enable Debugging mode
    # Run of port 5656
    app.run(host='0.0.0.0', port=5656, debug=True)
