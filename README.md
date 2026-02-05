# End-to-End Selenium Test Automation Framework
A professional end-to-end test automation framework built using Python, Selenium, and PyTest, following Page Object Model (POM) design principles.
This project demonstrates real-world automation practices.

## Overview
This framework supports:
- Cross-browser testing
- Data-driven testing using JSON
- PyTest fixtures and hooks
- HTML reporting with screenshots on failure
- Clean and scalable project structure

## Tech Stack

- Python 3.11+
- Selenium WebDriver
- PyTest
- webdriver-manager
- pytest-html

## How to Run the Tests

### Create and activate virtual environment

python -m venv .venv  
.venv\Scripts\activate  

### Install dependencies

pip install -r requirements.txt  

### Run tests

pytest -v -s  

### Run tests with HTML report

pytest --browser_name=chrome --html=reports/report.html --self-contained-html  

## Reports

- HTML reports are generated using pytest-html
- Screenshots are automatically captured on test failure
- Reports are generated inside the reports directory
- Reports are excluded from GitHub using .gitignore

## Demo Application

Tests are executed against the following demo application:

https://rahulshettyacademy.com/loginpagePractise/

Note:
This is a public demo site.  
UI behavior or credentials may change.  
The framework focuses on automation design and flow validation.

## Why This Project

This project was created to:

- Apply Selenium automation concepts in a real framework
- Practice industry-level test structure

## Author

Sheetal Kadian  
Aspiring QA / Automation Engineer

## Future Enhancements

- CI/CD integration using GitHub Actions
- Parallel execution
- Logging framework
- Environment-based configuration
