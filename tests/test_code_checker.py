import unittest
from socialsync.main_code_checker import CodeChecker

class TestCodeChecker(unittest.TestCase):
    def test_find_unused_variables(self):
        code = "x = 10\ny = 20"
        checker = CodeChecker(code)
        self.assertEqual(checker.find_unused_variables(), ["x", "y"])

    def test_check_syntax_errors(self):
        code = "print('Hello, world!'"
        checker = CodeChecker(code)
        self.assertTrue(len(checker.check_syntax_errors()) > 0)

    def test_suggest_improvements(self):
        code = "for i in range(10): pass"
        checker = CodeChecker(code)
        self.assertIn("Consider adding a break statement", checker.suggest_improvements())

    def test_detect_long_functions(self):
        code = "def long_function():\n" + "\n".join(["    pass"] * 25)
        checker = CodeChecker(code)
        self.assertTrue(len(checker.detect_long_functions()) > 0)

if __name__ == "__main__":
    unittest.main()