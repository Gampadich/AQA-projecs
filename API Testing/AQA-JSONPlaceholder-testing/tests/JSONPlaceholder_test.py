import allure
import requests
from jsonschema import validate

@allure.feature('Get section')
@allure.story('Get /posts test')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_all(url):
    with allure.step('Make API request'):
        result = requests.get(f'{url}/posts')
    with allure.step('Testing status code, type and count of elements'):
        assert result.status_code == 200
        assert isinstance(result.json(), list)
        assert len(result.json()) > 0

@allure.story('Get /posts/{id} test')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_one(url):
    with allure.step('Make API request'):
        result = requests.get(f'{url}/posts/1')
    with allure.step('Testing status code, type and count of elements'):
        assert result.status_code == 200
        assert isinstance(result.json(), dict)
        assert len(result.json()) > 0

@allure.story('GET non-existent post')
def test_get_non_existent_post(url):
    with allure.step('Make API request'):
        result = requests.get(f'{url}/poasts/14885267')
        data = result.json()
    with allure.step('Testing status code and data'):
        assert result.status_code == 404
        assert data == {}

@allure.feature('Post section')
@allure.story('Post /posts test')
@allure.severity(allure.severity_level.CRITICAL)
def test_post(url, post_data, schema):
    with allure.step('Make API request'):
        result = requests.post(f'{url}/posts', json=post_data)
        json_data = result.json()
    with allure.step('Testing status code and data'):
        assert result.status_code == 201
        validate(instance=json_data, schema=schema)

@allure.feature('Put section')
@allure.story('Put /posts/1 test')
@allure.severity(allure.severity_level.CRITICAL)
def test_put(url, put_data, schema):
    with allure.step('Make API request'):
        result = requests.put(f'{url}/posts/1', json=put_data)
        json_data = result.json()
    with allure.step('Testing status code and data'):
        assert result.status_code == 200
        validate(instance=json_data, schema=schema)

@allure.feature('Patch section')
@allure.story('Patch /posts/1 test')
@allure.severity(allure.severity_level.CRITICAL)
def test_patch(url, patch_data, schema):
    with allure.step('Make API request'):
        result = requests.patch(f'{url}/posts/1', json=patch_data)
        json_data = result.json()
    with allure.step('Testing status code and title in data'):
        assert result.status_code == 200
        validate(instance=json_data, schema=schema)

@allure.feature('Delete section')
@allure.story('Delete /posts/1 test')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete(url):
    with allure.step('Make API request'):
        result = requests.delete(f'{url}/posts/1')
    with allure.step('Testing status code'):
        assert result.status_code == 200
