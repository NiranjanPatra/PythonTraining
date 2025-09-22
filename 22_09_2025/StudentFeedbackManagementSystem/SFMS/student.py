import mysql.connector
from feedback import Feedback
from mysql.connector import Error, errorcode

from database_connection import DatabaseConnection
from logger import Logger
from logger import LoggingType

logger = Logger(__name__)

class DuplicateFeedbackError(Exception):
    pass

class Student:
    def __init__(self):
        self.conn = DatabaseConnection.connectDB()
        self.cursor = self.conn.cursor(dictionary=True)

    def register(self, name, email, password):
        status = 0
        query = "Insert into students(name,email,password) values(%s,%s,%s)"
        try:
            self.cursor.execute(query,(name,email,password))
            self.conn.commit()

            logger.write_log(f"Student:{name} registered successfully", LoggingType.info)
            status = 1

        except mysql.connector.IntegrityError as e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                status = 2
                logger.write_log(f"IntegrityError: The email '{email}' is already registered.", LoggingType.error)
            else:
                logger.write_log(f"Integrity Error: {e}", LoggingType.error)
        except Error as e:
            logger.write_log(f"Student database Error: {e}", LoggingType.error)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        return status
    
    def login(self, email, password):
        id = None
        try:
            sql = "SELECT student_id FROM students WHERE email = %s AND password = %s"
            self.cursor.execute(sql, (email, password))
            result = self.cursor.fetchone()

            if result:
                logger.write_log("Student login successful", LoggingType.info)
                id = int(result["student_id"])
                print("Student id = ", id)
            else:
                logger.write_log("Invalid login credentials", LoggingType.warning)
        except Error as e:
            logger.write_log(f"Student login database error: {e}", LoggingType.error)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

        return id

    def submit_feedback(self, feedback):
        status = False
        try:
            # Check if feedback already exists
            check_sql = "SELECT feedback_id FROM feedback WHERE student_id = %s AND course_id = %s"
            self.cursor.execute(check_sql, (feedback.student_id, feedback.course_id))
            if self.cursor.fetchone():
                logger.write_log("Integrity Error: Duplicate feedback submission", LoggingType.error)
                return False

            # Insert feedback
            insert_sql = """
            INSERT INTO feedback (student_id, course_id, rating, comments)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(insert_sql, (feedback.student_id, feedback.course_id, feedback.ratings, feedback.comments))
            self.conn.commit()
            logger.write_log("Feedback submitted successfully.", LoggingType.info)
            status = True
        except mysql.connector.IntegrityError as e:
            if e.errno == errorcode.ER_DUP_ENTRY:
                logger.write_log("IntegrityError: Duplicate feedback submission", LoggingType.error)
                raise DuplicateFeedbackError("Duplicate feedback found")
            else:
                logger.write_log("IntegrityError: {e}", LoggingType.error)
        except Error as e:
            logger.write_log("Feedack database Error: {e}", LoggingType.error)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        return status