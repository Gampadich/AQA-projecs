import requests
import allure


@allure.feature('Authentication')
class TestAuthentication:
    """Test suite covering user authentication endpoints."""

    @allure.story('Authenticate user and generate access token')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_user(self, url: str, post_user_data: dict):
        """Verify successful user authentication yields a valid access token."""
        with allure.step('Send POST request to /auth with user credentials'):
            response = requests.post(f'{url}/auth', json=post_user_data)
            data = response.json()

        with allure.step('Validate HTTP status code 200 and token presence'):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert 'token' in data and data['token'], "Response body does not contain a valid token"


@allure.feature('Booking Management - GET')
class TestGetBookings:
    """Test suite covering booking data retrieval endpoints."""

    @allure.story('Retrieve list of all booking IDs')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_bookings(self, url: str):
        """Verify fetching the full list of existing booking IDs."""
        with allure.step('Send GET request to /booking'):
            response = requests.get(f'{url}/booking')

        with allure.step('Validate HTTP status code 200 and list type'):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert isinstance(response.json(), list), "Response payload should be a list"

    @allure.story('Retrieve specific booking details by ID')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_booking_by_id(self, url: str, created_booking_id: int):
        """Verify fetching detailed booking information by dynamic entity ID."""
        with allure.step(f'Send GET request to /booking/{created_booking_id}'):
            response = requests.get(f'{url}/booking/{created_booking_id}')

        with allure.step('Validate HTTP status code 200 and non-empty payload'):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert response.json(), "Response payload is empty"


@allure.feature('Booking Management - POST')
class TestCreateBooking:
    """Test suite covering new booking entity creation."""

    @allure.story('Create new booking record')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_book(self, url: str, post_book_data: dict):
        """Verify booking creation returns HTTP 200 and accurately matches input fields."""
        with allure.step('Send POST request to /booking with payload'):
            response = requests.post(f'{url}/booking', json=post_book_data)
            data = response.json()

        with allure.step('Validate HTTP status code 200 and created record attributes'):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert 'bookingid' in data, "Response does not include generated bookingid"
            
            # Assert field mapping integrity
            booking = data['booking']
            assert booking['firstname'] == post_book_data['firstname']
            assert booking['lastname'] == post_book_data['lastname']
            assert booking['totalprice'] == post_book_data['totalprice']
            assert booking['depositpaid'] == post_book_data['depositpaid']
            assert booking['bookingdates'] == post_book_data['bookingdates']
            assert booking['additionalneeds'] == post_book_data['additionalneeds']


@allure.feature('Booking Management - PUT')
class TestUpdateBooking:
    """Test suite covering full entity updates."""

    @allure.story('Update existing booking record via PUT')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_put_book(self, url: str, created_booking_id: int, put_book_data: dict, headers: dict):
        """Verify full entity modification using PUT method and Basic Auth."""
        with allure.step(f'Send PUT request to /booking/{created_booking_id} with updated payload'):
            response = requests.put(
                f'{url}/booking/{created_booking_id}', 
                json=put_book_data, 
                headers=headers
            )
            data = response.json()

        with allure.step('Validate HTTP status code 200 and modified fields'):
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert data['firstname'] == put_book_data['firstname']
            assert data['lastname'] == put_book_data['lastname']
            assert data['totalprice'] == put_book_data['totalprice']
            assert data['depositpaid'] == put_book_data['depositpaid']


@allure.feature('Booking Management - DELETE')
class TestDeleteBooking:
    """Test suite covering resource deletion."""

    @allure.story('Delete existing booking record')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_book(self, url: str, created_booking_id: int, headers: dict):
        """Verify deleting a booking record returns HTTP status code 201 Created."""
        with allure.step(f'Send DELETE request to /booking/{created_booking_id}'):
            response = requests.delete(f'{url}/booking/{created_booking_id}', headers=headers)

        with allure.step('Validate HTTP status code 201 (Restful Booker standard for successful deletion)'):
            assert response.status_code == 201, f"Expected 201, got {response.status_code}"
