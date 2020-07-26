# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_group(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.add_new_group(driver, Group(name="test group", header="test 12345 _", footer="test 12345 +"))
        self.goto_groups_page(driver)
        self.logout(driver)

    def test_add_empty_group(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.add_new_group(driver, Group(name="", header="", footer=""))
        self.goto_groups_page(driver)
        self.logout(driver)

    def login(self, driver, username, password):
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, driver):
        driver.get("https://localhost/")

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def goto_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def add_new_group(self, driver, group):
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
