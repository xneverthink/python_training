from model.contact import Contact
from random import randrange

from test.test_phones import merge_phones_like_on_home_page


def test_random_contact_info(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(name="name", first_name="firstName", middle_name="middleName", last_name="lastName",
                    nick_name="nickname", title="title", company="company", address="address2", home="phone",
                    mobile="mobile", work="work", fax="fax", email="email", email2="email2", email3="email3",
                    homepage="", bday="1", bmonth="January", byear="1994", aday="7", amonth="May", ayear="2020",
                    address2="address2", phone2="phone2", notes="notes"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address2 == contact_from_edit_page.address2
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == "\n".join(filter(lambda x: x != "",
                                                                                filter(lambda x: x is not None,
                                                                                       [contact_from_edit_page.email,
                                                                                        contact_from_edit_page.email2,
                                                                                        contact_from_edit_page.email3])))
