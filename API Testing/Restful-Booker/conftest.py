import pytest
import allure

@pytest.fixture(scope="session")
@allure.step('Get API URL')
def url():
    return 'https://restful-booker.herokuapp.com'

@pytest.fixture(scope="session")
@allure.step('Make POST user data')
def post_user_data():
    return {"username": "admin", "password": "password123"}

@pytest.fixture(scope="session")
@allure.step('Make POST book data')
def post_book_data():
    return {
        "firstname": "Alex",
        "lastname": "Tester",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-10"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture(scope="session")
@allure.step('Make PUT book data')
def put_book_data():
    return {
        "firstname": "Adam",
        "lastname": "Admin",
        "totalprice": 120,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-10"
        },
        "additionalneeds": "Breakfast"
    }

@pytest.fixture(scope="session")
@allure.step('Get headers')
def headers():
    return {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}
