class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_homepage(driver)
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user")
