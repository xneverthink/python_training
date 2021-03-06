# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.db import clean_contact_info_from_db
import allure


def test_add_contact(app, db, json_contacts, check_ui):
    contact_data = json_contacts
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("When I add a contact %s to the list" % contact_data):
        app.contact.create(contact_data)
    #assert len(old_contacts) + 1 == app.contact.count()
    with allure.step("Then the new contact list is equal to the old list with the added group"):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact_data)
        #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        db_list = map(clean_contact_info_from_db, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
