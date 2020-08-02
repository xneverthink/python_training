from model.contact import Contact
from fixture.db import clean_contact_info_from_db


def test_contact_list(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(name="name", firstname="firstName", middlename="middleName", lastname="lastName",
                    nickname="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    contacts_from_db = db.get_contact_list()
    db_list = map(clean_contact_info_from_db, contacts_from_db)
    assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
