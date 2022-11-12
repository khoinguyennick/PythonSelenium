from selenium import webdriver
from src.pages.index_page import IndexPage
from src.pages.github_login_page import GithubLoginPage
# from src.pages.authorize_to_do_app import AuthorizeToDoApp
from src.pages.homepage import HomePage

import time


def test_todo_list_login_github():
    driver = webdriver.Chrome()
    driver.get("https://todo-list-login.firebaseapp.com/")

    index_page = IndexPage(driver)
    github_page = GithubLoginPage(driver)
    # authorize_git_page = AuthorizeToDoApp(driver)

    # storing the current window handle to get back to dashboard
    main_page = driver.current_window_handle
    homepage = HomePage(driver)

    index_page.click_sign_in_git_hub()
    # changing the handles to access login page
    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle
    # change the control to signin page
    driver.switch_to.window(login_page)
    github_page.login()
    # authorize_git_page.click_authorize_btn() #for first time login on todoList had to authorize // uncomment follow line 16
    time.sleep(3)

    # change control to main page
    driver.switch_to.window(main_page)
    homepage.add_new_random_content_todo()
    homepage.click_sign_out_btn()
    time.sleep(2)
    driver.close()
    #end process 1

    driver = webdriver.Chrome()
    driver.get("https://todo-list-login.firebaseapp.com/")

    index_page_2 = IndexPage(driver)
    github_page_2 = GithubLoginPage(driver)
    homepage_2 = HomePage(driver)
    # storing the current window handle to get back to dashboard
    main_page = driver.current_window_handle

    index_page_2.click_sign_in_git_hub()
    time.sleep(5)
    for handle in driver.window_handles:
        if handle != main_page:
            login_page = handle

    # change the control to signin page
    driver.switch_to.window(login_page)
    github_page_2.login()

    time.sleep(3)
    # change control to main page
    driver.switch_to.window(main_page)

    homepage_2.perform_delete_todo_list()
    homepage_2.click_sign_out_btn()
    time.sleep(5)

    driver.quit()

