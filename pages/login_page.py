class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_test_id("username")
        self.password = page.get_by_test_id("password")
        self.error = page.get_by_test_id("error")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.page.get_by_test_id("login-button").click()
