import requests
import allure

@allure.feature('GET section')
@allure.story('GET all booking test')
@allure.severity(allure.severity_level.CRITICAL)
def test_get(url):
    with allure.step('Make API test'):
        response = requests.get(f'{url}/booking')
    with allure.step('Check API code'):
        assert response.status_code == 200

@allure.feature('GET section')
@allure.story('GET booking by id test')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_by_id(url):
    with allure.step('Make API test'):
        response = requests.get(f'{url}/booking/52')
    with allure.step('Check API code and data'):
        assert response.status_code == 200
        assert response.json()

@allure.feature('POST section')
@allure.story('POST user test')
@allure.severity(allure.severity_level.CRITICAL)
def test_post_user(url, post_user_data):
    with allure.step('Make API test'):
        response = requests.post(f'{url}/auth', json=post_user_data)
        data = response.json()
    with allure.step('Check API code and data'):
        assert response.status_code == 200
        assert data['token']

@allure.feature('POST section')
@allure.story('POST booking test')
@allure.severity(allure.severity_level.CRITICAL)
def test_post_book(url, post_book_data):
    with allure.step('Make API test'):
        response = requests.post(f'{url}/booking', json=post_book_data)
        data = response.json()
    with allure.step('Check API code and data'):
        assert response.status_code == 200
        assert data['bookingid']
        assert data['booking']['firstname'] == post_book_data['firstname']
        assert data['booking']['lastname'] == post_book_data['lastname']
        assert data['booking']['totalprice'] == post_book_data['totalprice']
        assert data['booking']['depositpaid'] == post_book_data['depositpaid']
        assert data['booking']['bookingdates'] == post_book_data['bookingdates']
        assert data['booking']['additionalneeds'] == post_book_data['additionalneeds']

@allure.feature('PUT section')
@allure.story('PUT booking test')
@allure.severity(allure.severity_level.CRITICAL)
def test_put_book(url, put_book_data, headers):
    with allure.step('Make API test'):
        response = requests.put(f'{url}/booking/52', json=put_book_data, headers=headers)
        data = response.json()
    with allure.step('Check API code and data'):
        assert response.status_code == 200
        assert data['firstname'] == put_book_data['firstname']
        assert data['lastname'] == put_book_data['lastname']
        assert data['totalprice'] == put_book_data['totalprice']
        assert data['depositpaid'] == put_book_data['depositpaid']

@allure.feature('DELETE section')
@allure.story('DELETE booking test')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_book(url, headers):
    with allure.step('Make API test'):
        response = requests.delete(f'{url}/booking/30', headers=headers)
    with allure.step('Check API code'):
        assert response.status_code == 201
