from src.pages.base_page import BasePage
import random
import string


class HomePage(BasePage):
    locators = {
        "sign_out_btn": ("xpath", "//button[.='Sign out']"),
        "todo_list_header_title": ("xpath", "//div[contains(@class,'brownhill')]"),
        "todo_list_txt": ("xpath", "//input[@type='text' and not(@placeholder='Search')]"),
        "add_todo_list_btn": ("xpath", "//button[.='Add List']"),
    }

    def click_sign_out_btn(self):
        self.sign_out_btn.click()

    def is_login_header_login_displayed(self):
        retrieved_header = self.todo_list_header_title.text
        assert "Todo Lists" in retrieved_header

    def input_todo(self, content):
        self.todo_list_txt.send_keys(content)

    def click_add_todo(self):
        self.add_todo_list_btn.click()

    def add_new_random_content_todo(self):
        list_content = self.generate_todo_list(10)
        for input in list_content:
            self.input_todo(input)
            self.click_add_todo()

    def generate_todo_list(self, time):
        list_content = []
        for i in range(time):
            list_content.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15)))
        return list_content

    def get_all_todo_list(self):
        todo_list_element_locator = "//a[contains(@href,'!/list/')]"
        todo_list_element = self.get_list_elements_by_xpath(todo_list_element_locator)
        return todo_list_element

    def delete_todo_list_by_name(self, todo_list_name):
        locator = "//a[contains(.,'{name}')]/../..//button".format(name=todo_list_name)
        print(locator)
        element = self.get_web_element_by_xpath(locator)
        element.click()

    def perform_delete_todo_list(self):
        todo_list_elements = self.get_all_todo_list()
        for i in range(5, len(todo_list_elements)):
            self.delete_todo_list_by_name(todo_list_elements[i].text)
