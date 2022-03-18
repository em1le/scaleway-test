from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class AccountTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        cls.username = "johny"
        cls.email = "john.doe@gmail.com"
        cls.password = "azerty01!"
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/accounts/signup/"))
        username_input = self.selenium.find_element(by="name", value="username")
        username_input.send_keys(self.username)
        email_input = self.selenium.find_element(by="name", value="email")
        email_input.send_keys(self.email)
        password_input = self.selenium.find_element(by="name", value="password1")
        password_input.send_keys(self.password)
        password_input2 = self.selenium.find_element(by="name", value="password2")
        password_input2.send_keys(self.password)
        self.selenium.find_element(by="name", value="submit").click()
