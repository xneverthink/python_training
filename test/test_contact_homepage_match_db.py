from model.contact import Contact
import re


def test_contact_info(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(
            Contact(name="name", firstname="firstName", middlename="middleName", lastname="lastName",
                    nickname="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for c in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[c].lastname == contacts_from_db[c].lastname
        assert contacts_from_home_page[c].firstname == contacts_from_db[c].firstname
        assert contacts_from_home_page[c].address == contacts_from_db[c].address
        assert contacts_from_home_page[c].all_phones == "\n".join(filter(lambda x: x != "", map(lambda x:
                                                                                                re.sub("[/() -]", "", x),
                                                                                                filter(lambda x: x is not None,
                                                                                                       [contacts_from_db[c].home,
                                                                                                        contacts_from_db[c].mobile,
                                                                                                        contacts_from_db[c].work,
                                                                                                        contacts_from_db[c].phone2]
                                                                                                       ))))
        assert contacts_from_home_page[c].all_emails == "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                                                               [contacts_from_db[c].email,
                                                                                                contacts_from_db[c].email2,
                                                                                                contacts_from_db[c].email3])))
