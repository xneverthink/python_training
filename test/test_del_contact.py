# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                    nick_name="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    sleep(1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
