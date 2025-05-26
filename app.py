from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/browse-courses', methods=['POST'])
def browse_courses():
    course_id = request.form.get('courseId')
    print(f"Browsing course: {course_id}")
    return f"Browsing course: {course_id}"

@app.route('/enroll-course', methods=['POST'])
def enroll_course():
    user_name = request.form.get('userName')
    course_name = request.form.get('courseName')
    print(f"{user_name} enrolled in {course_name}")
    return f"Successfully enrolled {user_name} in {course_name}"

@app.route('/lessons', methods=['GET'])
def get_lessons():
    course_name = request.args.get('courseName')
    print(f"Fetching lessons for course: {course_name}")
    lessons = [
        "Lesson 1: Introduction",
        "Lesson 2: Greetings",
        "Lesson 3: Grammar",
        "Lesson 4: Numbers",
        "Lesson 5: Practice Quiz"
    ]
    return jsonify(course=course_name, lessons=lessons)

@app.route('/start-lesson', methods=['POST'])
def start_lesson():
    lesson_id = request.form.get('lessonId')
    print(f"Starting lesson: {lesson_id}")
    return f"Lesson {lesson_id} started"

@app.route('/complete-lesson', methods=['POST'])
def complete_lesson():
    lesson_id = request.form.get('completedLessonId')
    print(f"Marking lesson complete: {lesson_id}")
    return f"Lesson {lesson_id} marked as complete"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
