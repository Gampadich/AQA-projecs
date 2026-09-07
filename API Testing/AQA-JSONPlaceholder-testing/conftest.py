import pytest
import allure

@pytest.fixture(scope='session')
@allure.step('Get API URL')
def url():
    return 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='session')
@allure.step('Get json post data')
def post_data():
    return {
        "title": "My Post",
        "body": "Post content",
        "userId": 1
    }

@pytest.fixture(scope='session')
@allure.step('Get json put data')
def put_data():
    return {
        'id': 1,
        'title': 'Updated Title',
        'body': 'Updated Body',
        'userId': 1
    }

@pytest.fixture(scope='session')
@allure.step('Get json patch data')
def patch_data():
    return {
        'title': 'Only Title Changed'
    }

@pytest.fixture(scope='session')
@allure.step('Get schema')
def schema():
    return {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "number"}
        },
        "required": ["id", "title", "body", "userId"]
    }
