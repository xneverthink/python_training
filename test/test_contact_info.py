from model.contact import Contact


def test_random_contact_info(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                    nick_name="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    contacts_from_db = db.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(),
                       last_name=contact.last_name.strip(),
                       address=contact.address.strip())
    db_list = map(clean, contacts_from_db)
    assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
