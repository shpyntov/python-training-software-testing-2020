# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.add_new_group(Group(name="test group", header="test 12345 _", footer="test 12345 +"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.add_new_group(Group(name="", header="", footer=""))
    app.session.logout()
