from src.pages.base_page import BasePage
import time


class GithubLoginPage(BasePage):
    locators = {
        "username_txt": ("xpath", "//input[@name='login']"),
        "password_txt": ("xpath", "//input[@name='password']"),
        "sign_in_btn": ("xpath", "//input[@name='commit']")
    }

    def login(self):
        time.sleep(2)
        self.input_username()
        self.input_password()
        self.click_sign_in()

    def input_username(self):
        self.username_txt.send_keys(self.username)

    def input_password(self):
        self.password_txt.clear_text()
        self.password_txt.send_keys(self.password)

    def click_sign_in(self):
        self.sign_in_btn.click()
