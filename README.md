# Python Automation Framework - Web and API

## Project Overview
This project is a Python-based Selenium Web Automation framework designed for testing web applications. It integrates API testing and Continuous Integration/Continuous Deployment (CI/CD) using Jenkins. The framework is scalable, maintainable, and designed to handle complex test cases efficiently.

## Features
- **Web Automation:** Automate web applications using Selenium WebDriver.
- **API Testing:** Validate RESTful APIs using Pytest.
- **Reporting:** Generate detailed HTML reports with screenshots for test execution.
- **CI/CD:** Integrate with Jenkins for automated testing and deployment.

## Prerequisites
- **Python 3.7+**: Ensure Python is installed on your machine.
- **Selenium**: Install Selenium using `pip install selenium`.
- **Pytest**: Install Pytest using `pip install pytest`.
- **Jenkins**: Set up Jenkins for CI/CD (optional but recommended).

## Project Structure
![image](https://github.com/SaishWadkar/PythonAutomationFramework-Web-API/assets/60892068/0e35ed64-6759-4fbd-b3c6-e0769e5763a3)

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Running Tests

Running Regression Test Suite for Restful Booker
To run the regression test suite for the Restful Booker application, execute the following command:

```bash
pytest -v -s -m regression --html=reports_screenshots/restful_booker/Automation_Execution_Report_Restful_Booker.html tests/restful_booker
```

 **Author Name - Saish Wadkar**




