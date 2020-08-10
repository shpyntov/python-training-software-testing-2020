# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit_first_contact(Contact(firstname='Ivan11111', middlename='Ivanovich1111', lastname='Ivanov', nickname='', title='test', company='test',
                                         address='Test St. 123 456', home_phone="+79999999999", mobile_phone='+79991234567', work_phone='', fax='',
                                         email='test@test.com', email2='test@qwertyu.ru', email3='', home_page='www.ru',
                                         birth_day='2', birth_month='May', birth_year='1987',
                                         anniversary_day='10', anniversary_month='April', anniversary_year='1999',
                                         address_2='', phone_2='', note='test test test'))
    app.session.logout()
