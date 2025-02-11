import unittest
import os
from socialsync.logging_handler import LoggingHandler

class TestLoggingHandler(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_log.log"
        self.logger = LoggingHandler(self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_info(self):
        self.logger.log_info("Test info message")
        with open(self.log_file, "r") as f:
            logs = f.read()
        self.assertIn("INFO - Test info message", logs)

    def test_log_error(self):
        self.logger.log_error("Test error message")
        with open(self.log_file, "r") as f:
            logs = f.read()
        self.assertIn("ERROR - Test error message", logs)

if __name__ == "__main__":
    unittest.main()