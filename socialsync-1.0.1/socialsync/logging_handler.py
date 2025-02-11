import logging
from datetime import datetime

class LoggingHandler:
    def __init__(self, log_file: str = "socialsync.log"):
        self.logger = logging.getLogger("SocialSyncLogger")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_info(self, message: str):
        self.logger.info(message)

    def log_warning(self, message: str):
        self.logger.warning(message)

    def log_error(self, message: str):
        self.logger.error(message)

    def log_critical(self, message: str):
        self.logger.critical(message)

    def log_exception(self, message: str):
        self.logger.exception(message)