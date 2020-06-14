# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.open_user_registration_page()
    app.register_user(Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                                            nick_name="nickname", title="title", company="company", address="address2", home="phone", mobile="mobile", work="work",
                                            fax="fax", email="email", email2="email2", email3="email3", homepage="", bday="1", bmonth="January",
                                            byear="1994", aday="7", amonth="May", ayear="2020", address2="address2", phone2="phone2", notes="notes"))
    app.logout()