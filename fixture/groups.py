class GroupsHelper:

    def __init__(self, app):
        self.app = app

    def add_new_group(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("new").click()
        self.fill_group_form(driver, group)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element_by_name("selected[]").click()
        driver.find_element_by_name("edit").click()
        self.fill_group_form(driver, group)
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_group_form(self, driver, group):
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
