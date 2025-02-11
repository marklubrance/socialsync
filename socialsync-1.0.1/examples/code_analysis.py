from socialsync.main_code_checker import CodeChecker

code = """
def example_function():
    x = 10
    y = 20
    z = x + y
    for i in range(10):
        print(i)
"""

checker = CodeChecker(code)
print("Unused variables:", checker.find_unused_variables())
print("Syntax errors:", checker.check_syntax_errors())
print("Suggestions:", checker.suggest_improvements())
print("Long functions:", checker.detect_long_functions())
print("Security issues:", checker.check_security_issues())
print("Optimized code:\n", checker.optimize_code())