import mysql.connector

from logger import Logger
from logger import LoggingType

logger = Logger(__name__)

class DatabaseConnectionError(Exception):
    pass

class DatabaseConnection:
    # connect() method to connect the database
    def connect():
        try:
            mydb = mysql.connector.connect(
                host="localhost",  # IP
                user="root",
                password="kol@mind1"
                #database="feedback_system"  # database name
            )

            if mydb.is_connected():
                logger.write_log("Database connected successfully", LoggingType.info)

            return mydb
        except mysql.connector.Error as err:
            print("Database connected successfully")
            # Logger.write_log("Database failed to connect, " + err, LoggingType.error)
            raise DatabaseConnectionError("Database connection error")

    def connectDB():
        try:
            mydb = mysql.connector.connect(
                host="localhost",  # IP
                user="root",
                password="kol@mind1",
                database="feedback_system"  # database name
            )

            # if mydb.is_connected():
            #     Logger.write_log("Database connected successfully", LoggingType.info)

            return mydb
        except mysql.connector.Error as err:
            # Logger.write_log("Database failed to connect, " + err, LoggingType.error)
            raise DatabaseConnectionError("Database connection error")
        
    # disconnect() method to disconnect the database
    def disconnect(conn):
        try:
            if conn.is_connected():
                conn.close()
                # Logger.write_log("Database disconnected", level=LoggingType.info)
        except mysql.connector.Error as err:
            # Logger.write_log("Database fail to disconnect, " + err, level=LoggingType.error)
            raise DatabaseConnectionError("Database disconnection error")
