# End-to-End Test Automation Framework

''' Overview
This framework automates critical user flows of a demo web application and demonstrates:

Real-world automation structure

Page Object Model (POM) design pattern

Data-driven testing using JSON

PyTest fixtures, markers, and reporting

Screenshot capture on test failure

⚠️ The goal of this project is automation design & framework understanding, not just running tests.  '''

🔹 Tech Stack

Language: Python 3.x

Automation Tool: Selenium WebDriver

Test Framework: PyTest

Design Pattern: Page Object Model (POM)

Reporting: pytest-html

Driver Management: webdriver-manager

🔹 Key Features

✅ Page Object Model (POM)
✅ Data-driven testing using JSON
✅ HTML test reports
✅ Screenshot capture on failure
✅ PyTest fixtures & markers
✅ Interview-friendly architecture

🔹 Demo Application

Tests are executed against the following public demo site:

🔗 https://rahulshettyacademy.com/loginpagePractise/

Note:
This is a public demo application.
Credentials, UI behavior, or flows may change without notice.

🔹 How to Run the Tests
1️⃣ Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run tests normally
pytest -v -s

4️⃣ Run tests with HTML report
pytest --browser_name=chrome --html=reports/report.html --self-contained-html

🔹 Reports

HTML reports are generated using pytest-html

Screenshots are automatically captured on test failure

Reports are generated inside the reports/ directory

Reports are excluded from GitHub using .gitignore

🔹 Why This Project?

This project was created to:

Apply Selenium automation concepts in a real framework

Practice industry-level test architecture

Build a project that can be clearly explained in interviews

Avoid copy-paste automation and focus on conceptual understanding

🔹 Author

Sheetal Kadian
Aspiring QA / Automation Engineer

🔹 Future Enhancements

CI/CD integration (GitHub Actions)

Parallel execution

Logging framework

Environment-based configuration

Browser grid support

⭐ If you find this project useful, feel free to star the repository!

