from database_connection import DatabaseConnection

from logger import Logger
from logger import LoggingType

class SQLSchema:
    def __init__(self):
        self.conn = DatabaseConnection.connect()
        self.cursor = self.conn.cursor()

    def create_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS feedback_system")
        self.close()

        self.conn = DatabaseConnection.connectDB()
        self.cursor = self.conn.cursor()

    def connect_db(self):
        self.conn = DatabaseConnection.connectDB()
        self.cursor = self.conn.cursor()

    def create_student_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100) UNIQUE,
                password VARCHAR(100)
            )
            """
        self.cursor.execute(query)

    def create_courses_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS courses (
                course_id INT AUTO_INCREMENT PRIMARY KEY,
                course_name VARCHAR(100),
                faculty_name VARCHAR(100)
            )
            """
        self.cursor.execute(query)

    def create_feedback_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS feedback (
                feedback_id INT AUTO_INCREMENT PRIMARY KEY,
                student_id VARCHAR(100),
                course_id VARCHAR(100),
                rating VARCHAR(100),
                comments VARCHAR(100)
            )
            """
        self.cursor.execute(query)
    
    def create_admins_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS admins (
                admin_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100),
                password VARCHAR(100)
            )
            """
        self.cursor.execute(query)
        # self.cursor.close()

        # self.cursor = self.conn.cursor()
        # name = "root"
        # password = "admin"
        # query = "Insert into admins(username,password) values(%s,%s)"
        # self.cursor.execute(query,(name,password))

    def close(self):
        self.cursor.close()
        DatabaseConnection.disconnect(self.conn)