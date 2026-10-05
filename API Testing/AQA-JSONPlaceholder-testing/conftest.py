import pytest
import allure

@pytest.fixture(scope='session')
@allure.step('Provide base API URL')
def url() -> str:
    """Returns the base endpoint URL for JSONPlaceholder API."""
    return 'https://jsonplaceholder.typicode.com'


@pytest.fixture(scope='session')
@allure.step('Provide payload for POST request')
def post_data() -> dict:
    """Returns test payload for creating a new post entry."""
    return {
        "title": "My Post",
        "body": "Post content",
        "userId": 1
    }


@pytest.fixture(scope='session')
@allure.step('Provide payload for PUT request')
def put_data() -> dict:
    """Returns test payload for full post entity update."""
    return {
        'id': 1,
        'title': 'Updated Title',
        'body': 'Updated Body',
        'userId': 1
    }


@pytest.fixture(scope='session')
@allure.step('Provide payload for PATCH request')
def patch_data() -> dict:
    """Returns test payload for partial post title update."""
    return {
        'title': 'Only Title Changed'
    }


@pytest.fixture(scope='session')
@allure.step('Provide JSON Schema for Post entity validation')
def schema() -> dict:
    """Returns the expected JSON Schema structure for Post resources."""
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
