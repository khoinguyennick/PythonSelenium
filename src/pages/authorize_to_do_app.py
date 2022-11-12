from src.pages.base_page import BasePage


class AuthorizeToDoApp(BasePage):
    locators = {
        "authorize_header_title": ("xpath", "//h2[contains(@class,'text-center')]"),
        "authorize_in_btn": ("xpath", "//button[contains(.,'Authorize')]")
    }

    def is_login_header_login_displayed(self):
        retrieved_header = self.authorize_header_title.get_text()
        assert "Authorize Todo App" in retrieved_header

    def click_authorize_btn(self):
        self.authorize_in_btn.click()
