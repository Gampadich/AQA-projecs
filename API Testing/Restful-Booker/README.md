RESTful Booker API Tests

Automated API tests for the RESTful Booker
 REST API using Python, Pytest, Requests, and Allure.

The project covers the main CRUD operations for bookings as well as authentication.

Tech Stack
Python 3
Pytest — test framework
Requests — HTTP client for API requests
Allure — test reporting and test result visualization
RESTful Booker API — system under test
Project Structure
.
├── tests/
│   └── test_booking.py
├── conftest.py
├── requirements.txt
└── README.md


The exact structure may vary depending on the project configuration.

API Under Test

Base URL:

https://restful-booker.herokuapp.com


The tests use the following REST API endpoints:

Method	Endpoint	Purpose
GET	/booking	Get all booking IDs
GET	/booking/{id}	Get a booking by ID
POST	/auth	Create an authentication token
POST	/booking	Create a new booking
PUT	/booking/{id}	Update an existing booking
DELETE	/booking/{id}	Delete a booking
Test Coverage
GET
Get all bookings

The test sends a GET request to:

GET /booking


Assertions:

HTTP status code is 200.
Get booking by ID

The test sends a request to:

GET /booking/52


Assertions:

HTTP status code is 200.
Response contains JSON data.
POST
Create authentication token

The test sends login credentials to:

POST /auth


Request data:

{
  "username": "admin",
  "password": "password123"
}


Assertions:

HTTP status code is 200.
Response contains an authentication token.
Create a booking

The test sends a new booking to:

POST /booking


Example request:

{
  "firstname": "Alex",
  "lastname": "Tester",
  "totalprice": 150,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2026-10-01",
    "checkout": "2026-10-10"
  },
  "additionalneeds": "Breakfast"
}


Assertions:

HTTP status code is 200.
Response contains bookingid.
Returned booking data matches the submitted data.
PUT
Update a booking

The test updates booking 52 using:

PUT /booking/52


Authentication is provided using the Authorization header.

Assertions:

HTTP status code is 200.
Updated firstname matches the request.
Updated lastname matches the request.
Updated totalprice matches the request.
Updated depositpaid matches the request.
DELETE
Delete a booking

The test deletes booking 30 using:

DELETE /booking/30


Authentication is provided using the Authorization header.

Assertion:

HTTP status code is 201.
Installation

Clone the repository:

git clone <repository-url>
cd <project-directory>


Create a virtual environment:

python -m venv venv


Activate the virtual environment.

Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate


Install the dependencies:

pip install -r requirements.txt


If requirements.txt is not available, install the required packages manually:

pip install pytest requests allure-pytest

Running Tests

Run all tests with Pytest:

pytest


Run tests with verbose output:

pytest -v


Run a specific test file:

pytest tests/test_booking.py -v

Allure Reports

The tests use Allure annotations such as:

@allure.feature
@allure.story
@allure.severity
allure.step

These annotations make the test results easier to analyze in an Allure report.

Generate Allure Results

Run the tests with:

pytest --alluredir=allure-results


This creates the allure-results directory containing the test execution data.

Open the Allure Report

If Allure is installed on your system:

allure serve allure-results


Alternatively, generate a static report:

allure generate allure-results -o allure-report --clean


Then open the generated report.

Fixtures

The project uses Pytest fixtures to store reusable test data.

API URL
@pytest.fixture(scope="session")
def url():
    return "https://restful-booker.herokuapp.com"


The API base URL is reused by all tests.

Authentication Data

The authentication fixture contains the default RESTful Booker credentials:

{
    "username": "admin",
    "password": "password123"
}

Booking Data

The project contains separate fixtures for:

Creating a booking.
Updating a booking.
Authentication headers.

This keeps test data separate from test logic and makes the tests easier to maintain.

Authentication

The PUT and DELETE requests require authentication.

The project currently uses a Basic Authorization header:

{
    "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
}


For a production-quality framework, credentials and authorization data should be moved to environment variables or a secure configuration instead of being stored directly in the source code.

Allure Test Organization

Tests are organized using Allure features and stories.

Example:

@allure.feature("POST section")
@allure.story("POST booking test")
@allure.severity(allure.severity_level.CRITICAL)


This allows the generated report to group tests by API operation and business scenario.

Each API request and validation is also represented as an Allure step:

with allure.step("Make API test"):
    ...

with allure.step("Check API code and data"):
    ...

Example Test Result

A successful test run should contain tests covering:

GET section
├── GET all booking test
└── GET booking by id test

POST section
├── POST user test
└── POST booking test

PUT section
└── PUT booking test

DELETE section
└── DELETE booking test

Notes

The project uses fixed booking IDs (52 and 30) for some tests. Because RESTful Booker is a public demo API, the state of these records can change between test runs.

For a more stable automation framework, the tests could be improved by:

Creating test data dynamically before update/delete scenarios.
Saving the booking ID returned by the POST request.
Using the generated ID in subsequent PUT and DELETE requests.
Generating authentication tokens dynamically instead of using a hardcoded header.
Adding negative API tests.
Validating response schemas.
Validating response headers.
Adding parametrization for different test data.
Moving configuration and credentials to environment variables.
Adding CI/CD execution, for example with GitHub Actions.
Purpose

The main purpose of this project is to demonstrate automated REST API testing using Python and Pytest, including:

HTTP request validation.
Response status code verification.
JSON response validation.
CRUD API testing.
Authentication.
Reusable Pytest fixtures.
Allure test reporting.
Basic API test organization.