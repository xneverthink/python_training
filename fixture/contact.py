from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_user_registration_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact_data):
        wd = self.app.wd
        self.open_user_registration_page()
        self.fill_contact_form(contact_data)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def mod_first_contact(self):
        self.mod_contact_by_index(0)

    def mod_contact_by_index(self, index, contact_data):
        wd = self.app.wd
        self.open_home_page()
        #wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact_data):
        wd = self.app.wd
        self.change_field_value("firstname", contact_data.firstname)
        self.change_field_value("middlename", contact_data.middlename)
        self.change_field_value("lastname", contact_data.lastname)
        self.change_field_value("nickname", contact_data.nickname)
        self.change_field_value("title", contact_data.title)
        self.change_field_value("company", contact_data.company)
        self.change_field_value("address", contact_data.address)
        self.change_field_value("home", contact_data.home)
        self.change_field_value("mobile", contact_data.mobile)
        self.change_field_value("work", contact_data.work)
        self.change_field_value("fax", contact_data.fax)
        self.change_field_value("email", contact_data.email)
        self.change_field_value("email2", contact_data.email2)
        self.change_field_value("email3", contact_data.email3)
        self.change_field_value("homepage", contact_data.homepage)
        #Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        #wd.find_element_by_xpath("//option[@value='3']").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        #wd.find_element_by_xpath("//option[@value='May']").click()
        self.change_field_value("byear", contact_data.byear)
        #Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        #wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        #wd.find_element_by_xpath("(//option[@value='April'])[2]").click()
        self.change_field_value("ayear", contact_data.ayear)
        self.change_field_value("address2", contact_data.address2)
        self.change_field_value("phone2", contact_data.phone2)
        self.change_field_value("notes", contact_data.notes)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  all_phones=all_phones, address=address,
                                                  all_emails=all_emails))
        return list(self.contact_cache)

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_detail_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address2 = wd.find_element_by_name("address2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=first_name, lastname=last_name, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       address2=address2, email=email, email2=email2, email3=email3)

    def get_contact_from_detail_page(self, index):
        wd = self.app.wd
        self. open_contact_detail_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def add_contact_to_group_by_id(self, id, group_name):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_name)
        wd.find_element_by_name("add").click()

    def select_group_by_name(self, group_name):
        wd = self.app.wd
        Select(wd.find_element_by_name("group")).select_by_visible_text(group_name)

    def delete_contact_from_group_by_id(self, group_name, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_group_by_name(group_name)
        wd.find_element_by_name("remove")
        self.select_contact_by_id(id)
        wd.find_element_by_name("remove").click()
