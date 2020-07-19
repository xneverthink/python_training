# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from test.test_add_group import random_string

testdata = [Contact(name="", first_name="", middle_name="", last_name="",
                    nick_name="", title="", company="", address="", home="",
                    mobile="", work="", fax="", email="", email2="", email3="",
                    homepage="", byear="", ayear="", address2="", phone2="",
                    notes="")] + [
               Contact(name=random_string("name", 10), first_name=random_string("first_name", 10),
                       middle_name=random_string("middle_name", 10), last_name=random_string("last_name", 10),
                       nick_name=random_string("nick_name", 10), title=random_string("title", 10),
                       company=random_string("company", 10), address=random_string("address", 10),
                       home=random_string("home", 10), mobile=random_string("mobile", 10),
                       work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 10),
                       email2=random_string("email2", 10), email3=random_string("email3", 10),
                       homepage=random_string("homepage", 10), byear=random_string("byear", 10),
                       ayear=random_string("ayear", 10), address2=random_string("address2", 10),
                       phone2=random_string("phone2", 10), notes=random_string("notes", 10))
               for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
