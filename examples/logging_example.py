from socialsync.logging_handler import LoggingHandler

logger = LoggingHandler()

logger.log_info("This is an info message.")
logger.log_warning("This is a warning message.")
logger.log_error("This is an error message.")
logger.log_critical("This is a critical message.")