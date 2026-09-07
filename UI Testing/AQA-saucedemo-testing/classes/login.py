import allure

class LoginPage:
    def __init__(self, url, page, username, password):
        self.page = page
        self.url = url
        self.username = username
        self.password = password
        self.username_input = self.page.locator('#user-name')
        self.password_input = self.page.locator('#password')
        self.submit_input = self.page.locator('input[type="submit"]')

    @allure.step('Авторизуємося')
    def login(self):
        self.page.goto(self.url)
        self.username_input.fill(self.username)
        self.password_input.fill(self.password)
        self.submit_input.click()
