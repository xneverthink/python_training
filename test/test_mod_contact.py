# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_first_contact(app):
    app.contact.mod_first_contact(
        Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                nick_name="nickname", title="title", company="company", address="address2", home="phone",
                mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                address2="address2", phone2="phone2", notes="notes"))
