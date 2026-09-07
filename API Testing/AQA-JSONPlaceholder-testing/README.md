🚀 AQA JSONPlaceholder Testing Suite

Automated API test suite for testing the JSONPlaceholder
 REST API using Python, Pytest, Requests, and Allure Reports.

The project also includes a GitHub Actions CI/CD pipeline that automatically runs the tests and publishes the Allure test report to GitHub Pages.

🛠️ Tech Stack & Tools
Language: Python 3.11+
Test Framework: pytest
HTTP Client: requests
Reporting: allure-pytest
Schema Validation: jsonschema
CI/CD: GitHub Actions
Report Hosting: GitHub Pages
📊 Live Test Report

Every push or pull request automatically triggers the GitHub Actions pipeline.

The pipeline:

Installs project dependencies.
Runs the automated API test suite.
Generates Allure test results.
Publishes the Allure Report to GitHub Pages.

🔗 View Live Allure Report

🧪 Test Coverage

The test suite covers the main CRUD operations for the /posts resource:

Method	Endpoint	Expected Status	Validation
GET	/posts	200	Response type and non-empty list
GET	/posts/1	200	Response type and non-empty object
GET	/poasts/14885267	404	Empty response object
POST	/posts	201	JSON Schema validation
PUT	/posts/1	200	JSON Schema validation
PATCH	/posts/1	200	JSON Schema validation
DELETE	/posts/1	200	Status code validation
GET All Posts

Verifies that:

the API returns HTTP 200;
the response body is a list;
the list contains at least one element.
GET Single Post

Verifies that:

the API returns HTTP 200;
the response body is a dictionary/object;
the response is not empty.
GET Non-Existent Post

Verifies that:

the API returns HTTP 404;
the response body is an empty object {}.
POST Create Post

Verifies that:

the API returns HTTP 201;
the response matches the expected JSON Schema.
PUT Update Post

Verifies that:

the API returns HTTP 200;
the response matches the expected JSON Schema.
PATCH Update Post

Verifies that:

the API returns HTTP 200;
the response matches the expected JSON Schema.
DELETE Post

Verifies that:

the API returns HTTP 200.
🔍 JSON Schema Validation

The project uses the jsonschema library to validate API responses for POST, PUT, and PATCH requests.

The expected response contains the following fields:

{
  "id": 1,
  "title": "Post title",
  "body": "Post content",
  "userId": 1
}


The schema validates that:

id is a number;
title is a string;
body is a string;
userId is a number;
all four fields are required.
📁 Project Structure
AQA-JSONPlaceholder-testing/
│
├── .github/
│   └── workflows/
│       └── ...
│
├── test.py
├── conftest.py
├── requirements.txt
└── README.md

test.py

Contains the automated API tests for the /posts resource.

Allure annotations are used to organize tests by:

Epic
Feature
Story
Severity

Allure steps are also used to provide detailed information about API requests and assertions.

conftest.py

Contains reusable Pytest fixtures, including:

API base URL;
POST request data;
PUT request data;
PATCH request data;
JSON Schema.
requirements.txt

Contains the Python dependencies required to install and run the test suite.

🏃 How to Run Locally
1. Clone the repository
git clone https://github.com/Gampadich/AQA-JSONPlaceholder-testing.git
cd AQA-JSONPlaceholder-testing

2. Create a virtual environment
python -m venv venv

3. Activate the virtual environment

Linux / macOS:

source venv/bin/activate


Windows:

venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run the tests
pytest

6. Run tests with Allure results
pytest --alluredir=allure-results

7. Serve the Allure Report locally

Make sure Allure is installed and available in your system PATH.

Then run:

allure serve allure-results


The generated report will open automatically in your browser.

⚙️ CI/CD

The project uses GitHub Actions to automate test execution.

The CI/CD pipeline is triggered automatically on:

Push events
Pull requests

The workflow runs the test suite and generates an Allure Report that is published to GitHub Pages.

This provides a continuously updated test report without requiring local test execution.

📈 Allure Reporting

Allure provides detailed information about the test execution, including:

Passed and failed tests;
Test duration;
Test steps;
Test severity;
Epic / Feature / Story hierarchy;
Test execution history.

The test suite uses Allure decorators such as:

@allure.epic("API test")
@allure.feature("Get section")
@allure.story("Get /posts test")
@allure.severity(allure.severity_level.CRITICAL)


This makes the test results easier to analyze and navigate.

🌐 API Under Test

The project uses JSONPlaceholder, a free fake REST API designed for testing and prototyping.

Base URL:

https://jsonplaceholder.typicode.com


The main resource covered by this project is:

/posts

🎯 Project Goals

The main goals of this project are to demonstrate:

API test automation with Python;
Pytest test organization;
HTTP request handling with Requests;
CRUD API testing;
JSON Schema validation;
Reusable Pytest fixtures;
Allure reporting;
Test categorization with Allure;
CI/CD test execution with GitHub Actions;
Automatic test report publishing with GitHub Pages.
👨‍💻 Author

Gampadich

🔗 GitHub Repository