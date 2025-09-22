import mysql.connector
from feedback import Feedback
from mysql.connector import Error, errorcode

from database_connection import DatabaseConnection
from logger import Logger
from logger import LoggingType

log = Logger(__name__)

class Courses:
    def __init__(self):
        self.conn = DatabaseConnection.connectDB()
        self.cursor = self.conn.cursor(dictionary=True)
        self.courses_list = []
        self.fetch_courses()

    def populate_courses(self):
        course_data = [
            ("Python", "Mr. Bej"),
            ("C and C++", "Mr. Patra"),
            ("Java", "Dr. Mondol")
        ]
        self.add_multiple_courses(course_data)

    def add_multiple_courses(self, course_data):
        if len(self.courses_list) == 0:
            try:
                query = "INSERT INTO courses (course_name, faculty_name) VALUES (%s, %s)"
                self.cursor.executemany(query, course_data)
                self.conn.commit()
            except Error as e:
                log.write_log(f"Courses database error: {e}", LoggingType.error)

    def get_courses(self):
        return self.courses_list
 
    def fetch_courses(self):
        try:
            query = "SELECT * FROM courses"
            self.cursor.execute(query)
            self.courses_list = self.cursor.fetchall()

        except Error as e:
            log.write_log(f"Courses database error: {e}", LoggingType.error)
    
    def close(self):
        self.cursor.close()
        self.conn.close()