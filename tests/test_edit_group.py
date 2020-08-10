# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.edit_first_group(Group(name="edited test group", header="edited test 12345 _", footer="edited test 12345 +"))
    app.session.logout()
