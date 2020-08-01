from selenium import webdriver
from selenium.webdriver.support.ui import Select


class Application():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def destroy(self):
        self.driver.quit()

    def login(self, username, password):
        driver = self.driver
        self.open_homepage(driver)
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, driver):
        driver.get("https://localhost/")

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()

    def goto_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def add_new_group(self, group):
        driver = self.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()
        self.goto_groups_page()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def add_new_contact(self, contact):
        driver = self.driver
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
        self.goto_homepage()

    def goto_homepage(self):
        driver = self.driver
        driver.find_element_by_link_text("home").click()
