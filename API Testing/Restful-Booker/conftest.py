import pytest
import allure
import requests


@pytest.fixture(scope="session")
@allure.step('Provide Base API URL')
def url() -> str:
    """Returns the base endpoint URL for Restful Booker API."""
    return 'https://restful-booker.herokuapp.com'


@pytest.fixture(scope="session")
@allure.step('Provide User Authentication Credentials')
def post_user_data() -> dict:
    """Returns credentials payload for user authentication."""
    return {
        "username": "admin",
        "password": "password123"
    }


@pytest.fixture(scope="session")
@allure.step('Provide Initial Booking Payload')
def post_book_data() -> dict:
    """Returns payload structure for creating a new booking entity."""
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
@allure.step('Provide Updated Booking Payload')
def put_book_data() -> dict:
    """Returns payload structure for updating an existing booking entity."""
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
@allure.step('Provide Authorization Headers')
def headers() -> dict:
    """Returns Basic Authorization headers required for PUT/DELETE requests."""
    return {'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='}


@pytest.fixture(scope="function")
@allure.step('Create dynamic booking entity for dependent tests')
def created_booking_id(url: str, post_book_data: dict) -> int:
    """Creates a temporary booking resource and yields its dynamic ID."""
    response = requests.post(f'{url}/booking', json=post_book_data)
    assert response.status_code == 200, "Setup failed: Unable to create test booking"
    booking_id = response.json()['bookingid']
    yield booking_id
