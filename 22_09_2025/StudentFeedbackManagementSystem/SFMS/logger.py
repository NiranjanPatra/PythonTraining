import logging
from logging.handlers import RotatingFileHandler
import os
from enum import Enum

class LoggingType(Enum):
    debug = 1
    info = 2
    warning = 3
    error = 4

# log_created = False

# def initialize():
#     print("Logger init")
#     global log_created
#     if log_created == False:
#             print("Logger config")
#             logging.basicConfig(filename="app.log",
#                 filemode="a",
#                 level=logging.DEBUG,
#                 format='%(asctime)s - %(levelname)s - %(message)s')
#         #  self.logger = logging.getLogger()
#             log_created = True
# class Logger:    
    
#     def write_log(msg, level):
#         initialize()
#         str = msg
#         print(str)
#         # if level == LoggingType.debug:
#         #     logging.debug(msg)
#         # elif level == LoggingType.info:
#         #     logging.error(msg)
#         # elif level == LoggingType.warning:
#         #     logging.warning(msg)
#         # else:
#         #     logging.info(msg)

# logger_manager.py


class Logger:
    _loggers = {}

    def __init__(self, name: str):
        self.logger = self._get_or_create_logger(name)

    def _get_or_create_logger(cls, name):
        if name in cls._loggers:
            return cls._loggers[name]

        
        # logging.basicConfig(filename="app.log",
        #         filemode="a",
        #         level=logging.DEBUG,
        #         format='%(asctime)s - %(levelname)s - %(message)s')
        # logger = logging.getLogger(name)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )
            handler = RotatingFileHandler(
                "app.log",
                maxBytes=5 * 1024 * 1024,
                backupCount=3
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        # logger.setLevel(logging.INFO)

        # if not logger.handlers:
        #     formatter = logging.Formatter(
        #         '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        #     )
        #     handler = RotatingFileHandler(
        #         log_file,
        #         maxBytes=5 * 1024 * 1024,
        #         backupCount=3
        #     )
        #     handler.setFormatter(formatter)
        #     logger.addHandler(handler)

        cls._loggers[name] = logger
        return logger

    def get_logger(self):
        return self.logger

    def write_log(self, msg, level):
        log_content = ""
        try:
            if level == LoggingType.debug:
                self.logger.debug(msg)
            elif level == LoggingType.error:
                self.logger.error(msg)
            elif level == LoggingType.warning:
                self.logger.warning(msg)
            else:
                self.logger.info(msg)
        except FileNotFoundError:
            log_content = "Log file not found."
        except PermissionError:
            log_content = "Permission denied while writing the log file."
        except Exception as e:
            log_content = f"An unexpected error occurred while writing to the log file: {e}"

    def read_log(self):
        self.write_log("Reading log file", LoggingType.info)
        log_file_path = "app.log"
        log_content = ""
        try:
            if os.path.exists(log_file_path):
                with open(log_file_path, 'r') as file:
                    log_content = file.read()
            
        except FileNotFoundError:
            log_content = "Log file not found."
        except PermissionError:
            log_content = "Permission denied while accessing the log file."
        except Exception as e:
            log_content = f"An unexpected error occurred while reading the log file: {e}"

        return log_content
