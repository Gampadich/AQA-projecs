import allure
import requests
from jsonschema import validate


@allure.feature('GET Endpoints')
class TestGetPosts:
    """Test suite covering REST API GET requests for posts."""

    @allure.story('Retrieve all posts')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all(self, url: str):
        """Verify fetching the full list of posts."""
        with allure.step('Send GET request to /posts'):
            result = requests.get(f'{url}/posts')

        with allure.step('Validate HTTP status code, data structure, and non-empty list'):
            assert result.status_code == 200, f"Expected 200, got {result.status_code}"
            assert isinstance(result.json(), list), "Response body is not a list"
            assert len(result.json()) > 0, "Response posts list is empty"

    @allure.story('Retrieve single post by ID')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_one(self, url: str):
        """Verify fetching a specific post by its ID."""
        with allure.step('Send GET request to /posts/1'):
            result = requests.get(f'{url}/posts/1')

        with allure.step('Validate HTTP status code and response object type'):
            assert result.status_code == 200, f"Expected 200, got {result.status_code}"
            assert isinstance(result.json(), dict), "Response body is not a JSON object"
            assert len(result.json()) > 0, "Response object is empty"

    @allure.story('Handle non-existent post request')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_non_existent_post(self, url: str):
        """Verify 404 response when querying a non-existent post resource."""
        with allure.step('Send GET request to an invalid endpoint'):
            result = requests.get(f'{url}/poasts/14885267')
            data = result.json()

        with allure.step('Validate 404 Status Code and empty JSON payload'):
            assert result.status_code == 404, f"Expected 404, got {result.status_code}"
            assert data == {}, "Response body should be an empty dictionary"


@allure.feature('POST Endpoints')
class TestCreatePost:
    """Test suite covering post creation functionality."""

    @allure.story('Create new post resource')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_post(self, url: str, post_data: dict, schema: dict):
        """Verify creating a post yields 201 status and matches target JSON Schema."""
        with allure.step('Send POST request with payload'):
            result = requests.post(f'{url}/posts', json=post_data)
            json_data = result.json()

        with allure.step('Validate 201 Created status code and JSON Schema compliance'):
            assert result.status_code == 201, f"Expected 201, got {result.status_code}"
            validate(instance=json_data, schema=schema)


@allure.feature('PUT & PATCH Endpoints')
class TestUpdatePost:
    """Test suite covering full and partial post update operations."""

    @allure.story('Full update of post via PUT')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_put(self, url: str, put_data: dict, schema: dict):
        """Verify full entity update using PUT method."""
        with allure.step('Send PUT request with full payload'):
            result = requests.put(f'{url}/posts/1', json=put_data)
            json_data = result.json()

        with allure.step('Validate 200 status code and updated JSON Schema'):
            assert result.status_code == 200, f"Expected 200, got {result.status_code}"
            validate(instance=json_data, schema=schema)

    @allure.story('Partial update of post via PATCH')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_patch(self, url: str, patch_data: dict, schema: dict):
        """Verify partial attribute update using PATCH method."""
        with allure.step('Send PATCH request with partial payload'):
            result = requests.patch(f'{url}/posts/1', json=patch_data)
            json_data = result.json()

        with allure.step('Validate 200 status code and payload structure'):
            assert result.status_code == 200, f"Expected 200, got {result.status_code}"
            validate(instance=json_data, schema=schema)


@allure.feature('DELETE Endpoints')
class TestDeletePost:
    """Test suite covering resource deletion."""

    @allure.story('Delete post by ID')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete(self, url: str):
        """Verify post deletion request returns 200 status code."""
        with allure.step('Send DELETE request to /posts/1'):
            result = requests.delete(f'{url}/posts/1')

        with allure.step('Validate HTTP status code 200'):
            assert result.status_code == 200, f"Expected 200, got {result.status_code}"
