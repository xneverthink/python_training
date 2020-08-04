import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re


def clean_contact_info_from_db(contact):
    return Contact(id=contact.id, firstname=contact.firstname.strip(),
                   lastname=contact.lastname.strip(), address=contact.address.strip(),
                   all_emails=contact.all_emails, all_phones=contact.all_phones)


def clean_group_info_from_db(group):
    return Group(id=group.id, name=group.name.strip())


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, "
                           "address, home, mobile, work, fax, email, email2, email3, homepage, "
                           "address2, phone2, notes from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile,
                 work, fax, email, email2, email3, homepage, address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, company=company, title=title, address=address,
                                    home=home, mobile=mobile, work=work, fax=fax, email=email, email2=email2,
                                    email3=email3, homepage=homepage, address2=address2, phone2=phone2,
                                    notes=notes, all_emails="\n".join(filter(lambda x: x != "",
                                                                             filter(lambda x: x is not None,
                                                                                    [email, email2, email3]))),
                                    all_phones="\n".join(filter(lambda x: x != "", map(lambda x:
                                                                                       re.sub("[/() -]", "", x),
                                                                                       filter(lambda x: x is not None,
                                                                                              [home, mobile, work,
                                                                                               phone2]))))))
        finally:
            cursor.close()
        return list

    def check_groups_of_contact(self, id):
        group_ids = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where id = %s" % id)
            for row in cursor:
                (group_id) = row
                group_ids.append(group_id)
        finally:
            cursor.close()
        return group_ids

    def check_contacts_in_group(self, group_id):
        contact_ids = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where group_id = %s" % group_id)
            for row in cursor:
                (id) = row
                contact_ids.append(id)
        finally:
            cursor.close()
        return contact_ids

    def destroy(self):
        self.connection.close()
