from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group_random(app, db):
    if len(db.get_contact_list()) == 0 or len(db.get_contacts_without_group()) == 0:
        app.contact.create(
            Contact(name="name", firstname="firstName", middlename="middleName", lastname="lastName",
                    nickname="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())
    contact_ids = random.choice(db.check_contacts_not_in_group(group.id))
    app.contact.add_contact_to_group_by_id(contact_ids, group.name)
    groups_of_contact = db.check_groups_of_contact(contact_ids)
    assert (int(group.id),) in groups_of_contact
