from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory "database" of students
students = []

# Helper function to find a student by ID
def find_student(student_id):
    return next((student for student in students if student['id'] == student_id), None)

# GET /students - Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET /students/{id} - Retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = find_student(student_id)
    if not student:
        abort(404)
    return jsonify(student), 200

# POST /students - Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json or not 'grade' in request.json or not 'email' in request.json:
        abort(400)
    
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    students.append(new_student)
    return jsonify(new_student), 201

# PUT /students/{id} - Update an existing student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = find_student(student_id)
    if not student:
        abort(404)
    if not request.json:
        abort(400)
    
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    return jsonify(student), 200

# DELETE /students/{id} - Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student['id'] != student_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
