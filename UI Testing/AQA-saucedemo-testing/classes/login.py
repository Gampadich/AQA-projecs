import allure
from playwright.sync_api import Page, Locator


class LoginPage:
    """Page Object representing the SauceDemo Login Page."""

    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com/"):
        """Initialize Login Page elements and driver.
        
        :param page: Playwright Page instance
        :param base_url: Target application URL
        """
        self.page: Page = page
        self.url: str = base_url

        # UI Locators
        self.username_input: Locator = self.page.locator('#user-name')
        self.password_input: Locator = self.page.locator('#password')
        self.login_button: Locator = self.page.locator('input[type="submit"]')

    @allure.step("Navigate to the login page")
    def navigate(self) -> None:
        """Navigates to the base URL of the login page."""
        self.page.goto(self.url)

    @allure.step("Perform user login with credentials")
    def login(self, username: str, password: str) -> None:
        """Fills in credentials and submits the login form.
        
        :param username: User login string
        :param password: User password string
        """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    @allure.step("Perform full login flow")
    def open_and_login(self, username: str, password: str) -> None:
        """Combined helper method to open the page and authenticate in one call."""
        self.navigate()
        self.login(username, password)
