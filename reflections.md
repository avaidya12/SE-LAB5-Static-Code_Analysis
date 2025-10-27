Question 1:
•	The easiest issues to fix were stylistic and naming conventions, such as converting function names to snake_case and adding missing newlines at the end of the file. 
•	These were simple, mechanical edits that did not affect the program logic.
The harder issues were the mutable default argument and the use of eval(). 
•	Replacing eval() safely required understanding its intended purpose and switching to ast.literal_eval() or restructuring the logic. 
•	Similarly, fixing the mutable default argument required understanding how default parameters behave in Python and restructuring the function signature to use None as a default and initialize the list inside the function.

Question 2:
•	Yes, one mild false positive appeared when the tool flagged the except KeyError: pass statement as an issue. 
•	While broad except clauses are often risky, in this specific context it was acceptable because it intentionally suppressed missing-key errors during item removal — a controlled, predictable situation. The tool couldn’t differentiate between unsafe and deliberate exception handling.

Question 3:
Static analysis tools can be integrated into the workflow through both local development and CI/CD pipelines:
•	Local development: Tools like flake8, pylint, or bandit can be run automatically in the IDE (e.g., VS Code) or via pre-commit hooks to catch issues before committing changes.
•	Continuous Integration (CI): On platforms like GitHub or GitLab, static analysis checks can be part of the automated pipeline. Each push or pull request triggers linting and code quality checks, ensuring no new warnings or vulnerabilities are introduced into the main branch.

Question 4:
After applying the fixes:
•	Code readability improved significantly — clear docstrings and consistent naming make it easier for others (and future me) to understand what each function does.
•	Robustness increased — removing unsafe constructs like eval() and handling mutable defaults properly prevents subtle runtime bugs and security issues.
•	Maintainability improved — standardized formatting and documentation make extending or debugging the code easier.
•	Overall, the code now aligns better with PEP 8 standards and follows good software engineering practices, making it production-ready and easier to test.
