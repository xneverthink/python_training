# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                nick_name="nickname", title="title", company="company", address="address2", home="phone",
                mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                address2="address2", phone2="phone2", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
