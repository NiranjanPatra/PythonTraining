
from flask import Flask, render_template, request, redirect, url_for # type: ignore

import mysql.connector
import os

from sql_schema import SQLSchema
from database_connection import DatabaseConnectionError
from logger import Logger
from logger import LoggingType
from student import Student
from admin import Admin
from courses import Courses
from feedback import Feedback

log = Logger(__name__)

app = Flask(__name__)

current_student_id = 0

def init_db():
    log.write_log("Init database", LoggingType.info)
    sql_schema = SQLSchema()
    try:
        log.write_log("Database creating", LoggingType.info)
        sql_schema.create_database()
        log.write_log("Database created if no exists", LoggingType.info)
        sql_schema.create_student_table()
        log.write_log("Student table created if no exists", LoggingType.info)
        sql_schema.create_courses_table()
        log.write_log("Course table created if no exists", LoggingType.info)
        sql_schema.create_feedback_table()
        log.write_log("Feedback table created if no exists", LoggingType.info)
        sql_schema.create_admins_table()
        log.write_log("Admin table created if no exists", LoggingType.info)
        sql_schema.close()
        log.write_log("Database schema iniialized", LoggingType.info)

        admin_usr = Admin()
        admin_usr.add_admin()
    except DatabaseConnectionError as e:
        log.write_log(f"Init database exception: {e}", LoggingType.error)
    except mysql.connector.Error as err:
        log.write_log(f"Init database exception: {e}", LoggingType.error)
    except Exception as e:
        log.write_log(f"Init database exception: {e}", LoggingType.error)

    courses = Courses()
    courses.populate_courses()
    courses.close()
 
@app.route('/register',methods=['GET','POST'])
def form_register():
    if request.method == 'POST':
        log.write_log("Registering...", LoggingType.info)
        name = request.form['username']
        email = request.form['email']
        pwd = request.form['password']
        student = Student()
        status = student.register(name, email, pwd)
        if status == 1:
            return redirect(url_for('form_login'))
        elif status == 2:
            return f"Hello {name}, you are already registered !!"
        else:
            log.write_log("Student registration failed", LoggingType.error)
            return f"Hello {name}, registration failed !!"
    return '''
        <form method="POST">
        <label for="username">Username:</label><br>
        <input type="text" name="username"><br>
        <label for="username">Email:</label><br>
        <input type="text" name="email"><br>
        <label for="username">Password:</label><br>
        <input type="text" name="password"><br><br>
        <input type="submit">
        </form>
'''

@app.route('/login',methods=['GET','POST'])
def form_login():
    if request.method == 'POST':
        log.write_log("Verifying login details", LoggingType.info)
        email = request.form['email']
        pwd = request.form['password']
        student = Student()
        global current_student_id
        current_student_id = student.login(email, pwd)
        if current_student_id:
            log.write_log("Login successful", LoggingType.info)
            return redirect(url_for('form_submit_student_feedback'))
        
        log.write_log("Fail to login", LoggingType.error)
        return f"Hello, invalid login credentials or database error !!"
    return '''
        <form method="POST">
        <label for="username">Email:</label><br>
        <input type="text" name="email"><br>
        <label for="username">Password:</label><br>
        <input type="text" name="password"><br><br>
        <input type="submit">
        </form>
'''

@app.route('/submit_feedback',methods=['GET','POST'])
def form_submit_student_feedback():
    if request.method == 'POST':
        log.write_log("Feedback submitting...", LoggingType.info)
        global current_student_id
        student_id = current_student_id
        course_id = request.form.get('course_id')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        feedback = Feedback(student_id, course_id, rating, comments)

        student = Student()
        status = student.submit_feedback(feedback)
        if status == True:
            log.write_log("Feedback submited", LoggingType.info)
            return "Feedback submitted successfully !!"
        
        log.write_log("Feedback submission failed", LoggingType.error)
        return "Feedback submission failed !!"
    
    courses = Courses()
    courses_list = courses.get_courses()
    if len(courses_list) > 0:
        return render_template("submit_feedback.html", courses=courses_list)
    return "Sorry! unable to fetch data from courses database !!!"

@app.route('/admin/login',methods=['GET','POST'])
def form_admin_login():
    if request.method == 'POST':
        log.write_log("Verifying admin login details...", LoggingType.info)
        usr = request.form['username']
        pwd = request.form['password']
        admin_usr = Admin()
        status = admin_usr.login(usr, pwd)
        if status == True:
            return redirect(url_for('form_admin_feedback'))
        else:
            log.write_log("Admin login fail", LoggingType.error)
            return "Invalid login credentials or database error !!"
    return '''
        <form method="POST">
        <label for="username">User Name:</label><br>
        <input type="text" name="username"><br>
        <label for="username">Password:</label><br>
        <input type="text" name="password"><br><br>
        <input type="submit">
        </form>
'''

@app.route('/admin/feedback',methods=['GET','POST'])
def form_admin_feedback():
    if request.method == 'POST':
        return redirect(url_for('form_admin_downloadlog'))
    
    admin = Admin()
    feedback_list = admin.view_feedback()
    print(feedback_list)
    return render_template("view_feedback.html", feedback_list=feedback_list)

@app.route('/admin/downloadlog',methods=['GET','POST'])
def form_admin_downloadlog():
    log_content = log.read_log()
    # cleaned_log = log_content.strip()
    return render_template("view_log.html", log_content=log_content)
 
if __name__ == '__main__':
    log.write_log("==========Service started==========", LoggingType.info)
    print("Starting...")
    init_db()
    app.run(debug=True, use_reloader=False)
 
