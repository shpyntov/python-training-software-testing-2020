from selenium.webdriver.support.ui import Select


class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()
        self.fill_contact_form(driver, contact)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.goto_homepage()

    def edit_first_contact(self, contact):
        driver = self.app.driver
        first_row = driver.find_elements_by_css_selector("body table tr")[1]
        column = first_row.find_elements_by_css_selector("td")[7]
        column.find_element_by_css_selector('a').click()
        self.fill_contact_form(driver, contact)
        driver.find_element_by_name("update").click()
        self.goto_homepage()

    def fill_contact_form(self, driver, contact):
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.title)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.home_phone)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.work_phone)
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.home_page)
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.birth_year)
        Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.address_2)
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.phone_2)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.note)

    def goto_homepage(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        driver = self.app.driver
        self.goto_homepage()
        driver.find_element_by_css_selector("td[class='center'] > input").click()
        driver.find_element_by_xpath("//input[@value='Delete']").click()
        driver.switch_to_alert().accept()
