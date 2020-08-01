# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.add_new_group(Group(name="test group", header="test 12345 _", footer="test 12345 +"))
    app.logout()


def test_add_new_empty_group(app):
    app.login(username="admin", password="secret")
    app.add_new_group(Group(name="", header="", footer=""))
    app.logout()
