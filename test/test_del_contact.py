# -*- coding: utf-8 -*-
from model.contact import Contact
import random
from fixture.db import clean_contact_info_from_db
import allure


def test_delete_random_contact(app, db, check_ui):
    with allure.step("If contact list is empty, I add a new contact"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(
                Contact(name="name", firstname="firstName", middlename="middleName", lastname="lastName",
                        nickname="nickname", title="title", company="company", address="address2", home="phone",
                        mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                        homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                        address2="address2", phone2="phone2", notes="notes"))
    with allure.step("Given a random contact from contact list"):
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
    with allure.step("When I delete given contact %s" % contact):
        app.contact.delete_contact_by_id(contact.id)
    with allure.step("Then the new contact list is equal to the old list with the removed contact "
                     "and it's length is smaller by one"):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
    if check_ui:
        db_list = map(clean_contact_info_from_db, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
