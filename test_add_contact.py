# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_new_contact(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver, username="admin", password="secret")
        self.add_new_contact(driver, Contact(firstname='Ivan', middlename='Ivanovich', lastname='Ivanov', nickname='', title='test', company='test',
                                             address='Test St. 123 456', home_phone="+79999999999", mobile_phone='+79991234567', work_phone='', fax='',
                                             email='test@test.com', email2='test@qwertyu.ru', email3='', home_page='www.ru',
                                             birth_day='2', birth_month='May', birth_year='1987',
                                             anniversary_day='10', anniversary_month='April', anniversary_year='1999',
                                             address_2='', phone_2='', note='test test test'))
        self.goto_homepage(driver)
        self.logout(driver)

    def add_new_contact(self, driver, contact):
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").send_keys(contact.home_phone)
        driver.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        driver.find_element_by_name("work").send_keys(contact.work_phone)
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("homepage").send_keys(contact.home_page)
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        driver.find_element_by_name("byear").send_keys(contact.birth_year)
        Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        driver.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        driver.find_element_by_name("address2").send_keys(contact.address_2)
        driver.find_element_by_name("phone2").send_keys(contact.phone_2)
        driver.find_element_by_name("notes").send_keys(contact.note)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def goto_homepage(self, driver):
        driver.find_element_by_link_text("home").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, driver):
        driver.get("https://localhost/")

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
