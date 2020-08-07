from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group_random(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(name="name", firstname="firstName", middlename="middleName", lastname="lastName",
                    nickname="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    contact = random.choice(db.get_contact_list())
    contacts_in_group = db.check_contacts_in_group(group.id)
    if len(contacts_in_group) == 0:
        app.contact.add_contact_to_group_by_id(contact.id, group.name)
    contact_id = random.choice(contacts_in_group)
    app.contact.delete_contact_from_group_by_id(group.name, contact_id)
    contacts_in_group_after = db.check_contacts_in_group(group.id)
    assert (int(contact.id),) not in contacts_in_group_after
