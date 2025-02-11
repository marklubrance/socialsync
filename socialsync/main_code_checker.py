import ast
import subprocess
from typing import List, Dict, Any

class CodeChecker:
    def __init__(self, code: str):
        self.code = code
        self.tree = ast.parse(code)

    def find_unused_variables(self) -> List[str]:
        unused = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        if not any(isinstance(n, ast.Name) and n.id == var_name for n in ast.walk(self.tree)):
                            unused.append(var_name)
        return unused

    def check_syntax_errors(self) -> List[str]:
        try:
            compile(self.code, "<string>", "exec")
            return []
        except SyntaxError as e:
            return [str(e)]

    def suggest_improvements(self) -> List[str]:
        suggestions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.For) and not any(isinstance(child, ast.Break) for child in ast.iter_child_nodes(node)):
                suggestions.append("Consider adding a break statement in the loop if applicable.")
            if isinstance(node, ast.FunctionDef) and not any(isinstance(child, ast.Return) for child in ast.iter_child_nodes(node)):
                suggestions.append(f"Function '{node.name}' does not have a return statement.")
        return suggestions

    def detect_long_functions(self, max_lines: int = 20) -> List[str]:
        long_functions = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                lines = node.end_lineno - node.lineno
                if lines > max_lines:
                    long_functions.append(f"Function '{node.name}' is too long ({lines} lines).")
        return long_functions

    def detect_inefficient_loops(self) -> List[str]:
        inefficient_loops = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.For) and any(isinstance(child, ast.Call) for child in ast.iter_child_nodes(node)):
                inefficient_loops.append(f"Loop in line {node.lineno} may be inefficient due to function calls inside.")
        return inefficient_loops

    def check_security_issues(self) -> List[str]:
        security_issues = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == "eval" or node.func.attr == "exec":
                    security_issues.append(f"Potential security risk: use of '{node.func.attr}' in line {node.lineno}.")
        return security_issues

    def run_flake8_analysis(self) -> List[str]:
        with open("temp_code.py", "w") as f:
            f.write(self.code)
        result = subprocess.run(["flake8", "temp_code.py"], capture_output=True, text=True)
        return result.stdout.splitlines()

    def optimize_code(self) -> str:
        optimized_code = self.code
        for suggestion in self.suggest_improvements():
            optimized_code += f"\n# Suggestion: {suggestion}"
        return optimized_code

    def generate_report(self) -> Dict[str, Any]:
        report = {
            "unused_variables": self.find_unused_variables(),
            "syntax_errors": self.check_syntax_errors(),
            "suggestions": self.suggest_improvements(),
            "long_functions": self.detect_long_functions(),
            "inefficient_loops": self.detect_inefficient_loops(),
            "security_issues": self.check_security_issues(),
            "flake8_issues": self.run_flake8_analysis()
        }
        return report