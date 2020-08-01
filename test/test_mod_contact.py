# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_mod_random_contact(app, db, json_contacts, check_ui):
    contact_data = json_contacts
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                    nick_name="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.mod_contact_by_index(index, contact_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    # old_contacts[index] = contact_data
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, first_name=contact.first_name.strip(),
                           last_name=contact.last_name.strip(),
                           address=contact.address.strip())
        db_list = map(clean, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
