# End-to-End Test Automation Framework

## Overview
This project is an end-to-end Selenium test automation framework built using "Python", "PyTest", and the "Page Object Model (POM)" design pattern.

The framework is designed to automate real user flows on a web application and demonstrate best practices used in industry-level test automation projects.

## Key Features
- Page Object Model (POM) for maintainable test design
- PyTest fixtures for browser and test setup
- Data-driven testing using JSON
- Cross-browser execution (Chrome, Firefox)
- HTML test reports with screenshots on failure
- Clean and scalable folder structure
- Easy to extend for new test cases

## Tech Stack
- Python
- Selenium WebDriver
- PyTest
- webdriver-manager
- pytest-html

## Project Structure
EndToEnd_Test_Automation_Framework/
│
├── pageObjects/ # Page Object classes
│ ├── login.py
│ ├── ShopePage.py
│ └── checkout_confirmation.py
│
├── tests/ # Test cases
│ └── test_e2e.py
│
├── utils/ # Utility classes
│ └── BrowserUtils.py
│
├── data/ # Test data (JSON)
│ └── test_e2e.json
│
├── reports/ # HTML reports (ignored in Git)
│
├── conftest.py # PyTest fixtures & hooks
├── pytest.ini # PyTest configuration
├── requirements.txt # Project dependencies
├── README.md
└── ARCHITECTURE.md

## Framework Architecture
- **Tests** contain only test logic
- **Page Objects** handle element locators and page actions
- **Fixtures** manage browser setup and teardown
- **Utilities** provide reusable helper methods
- **JSON** files store test data separately from test logic

## How to Run the Tests

1. Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
2️. Install dependencies
pip install -r requirements.txt
3️. Run tests
pytest -v -s
4️. Run tests with HTML report
pytest --browser_name=chrome --html=reports/report.html --self-contained-html

📃Reports
HTML reports are generated using pytest-html

Screenshots are automatically captured on test failure

Reports are excluded from GitHub using .gitignore

## Demo Application
Tests are executed against the following demo site:

https://rahulshettyacademy.com/loginpagePractise/
Note: This is a demo site; credentials and behavior may be unstable.
The framework focuses on automation design and flow validation.

## Why This Project?
This project was created to:

Apply Selenium automation concepts in a real framework

Practice industry-level test structure

## Author
Seetal Kadian
Aspiring QA / Automation Engineer

## Future Enhancements
CI/CD integration (GitHub Actions)

Parallel execution

Logging framework

Environment-based configuration

