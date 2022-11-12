from src.pages.base_page import BasePage


class IndexPage(BasePage):

    locators = {
        "sign_in_git_hub": ("xpath", "//a[contains(@class,'btn-github')]"),
        "login_header_title": ("xpath", "//h1[@class='login-head']"),
    }

    def click_sign_in_git_hub(self):
        self.is_login_header_login_displayed()
        self.sign_in_git_hub.click()

    def is_login_header_login_displayed(self):
        retrieved_header = self.login_header_title.text
        assert "To continue you will need to sign in first," in retrieved_header
