# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.add_new_group(Group(name="test group", header="test 12345 _", footer="test 12345 +"))
    app.session.logout()


def test_add_new_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.groups.add_new_group(Group(name="", header="", footer=""))
    app.session.logout()
