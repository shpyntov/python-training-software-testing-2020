from selenium import webdriver
from fixture.session import SessionHelper
from fixture.groups import GroupsHelper
from fixture.contacts import ContactsHelper


class Application():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.groups = GroupsHelper(self)
        self.contacts = ContactsHelper(self)

    def destroy(self):
        self.driver.quit()

    def open_homepage(self, driver):
        driver.get("https://localhost/")
