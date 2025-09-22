import mysql.connector
from feedback import Feedback
from mysql.connector import Error, errorcode

from database_connection import DatabaseConnection
from logger import Logger
from logger import LoggingType

log = Logger(__name__)

class Admin:
    def __init__(self):
        self.conn = DatabaseConnection.connectDB()
        self.cursor = self.conn.cursor(dictionary=True)

    def add_admin(self):
        log.write_log("Add admin credentials", LoggingType.info)
        try:
            username = "root"
            password = "admin"
            query = "SELECT username FROM admins WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            result = self.cursor.fetchone()
            if result:
                log.write_log("Admin credentials exists", LoggingType.info)
            else:
                query = "Insert into admins(username,password) values(%s,%s)"
                self.cursor.execute(query,(username,password))
                self.conn.commit()
        except Error as e:
            log.write_log(f"Admin database error: {e}", LoggingType.error)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

    def login(self,username,password):
        status = False
        try:
            sql = "SELECT username FROM admins WHERE username = %s AND password = %s"
            self.cursor.execute(sql, (username, password))
            result = self.cursor.fetchall()

            if result:
                log.write_log("Admin login successful", LoggingType.info)
                status = True
            else:
                log.write_log("Invalid login credentials", LoggingType.error)
        except Error as e:
            log.write_log(f"Admin database error: {e}", LoggingType.error)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

        return status
    
    def view_feedback(self):
        feedback_list = []
        try:
            sql = """
            SELECT 
                f.feedback_id,
                s.name AS student_name,
                c.course_name,
                f.rating,
                f.comments
            FROM feedback f
            JOIN students s ON f.student_id = s.student_id
            JOIN courses c ON f.course_id = c.course_id
            ORDER BY f.feedback_id
            """
            # sql = "SELECT * FROM feedback"

            self.cursor.execute(sql)
            feedback_list = self.cursor.fetchall()
            log.write_log("Feedback fetched", LoggingType.info)

            return feedback_list

        except Error as e:
            log.write_log(f"Database error: {e}", LoggingType.error)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        return []