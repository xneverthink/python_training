from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", first_name="", middle_name="", last_name="",
                    nick_name="", title="", company="", address="", home="",
                    mobile="", work="", fax="", email="", email2="", email3="",
                    homepage="", byear="", ayear="", address2="", phone2="",
                    notes="")] + [
               Contact(name=random_string("name", 10), first_name=random_string("first_name", 10),
                       middle_name=random_string("middle_name", 10), last_name=random_string("last_name", 10),
                       nick_name=random_string("nick_name", 10), title=random_string("title", 10),
                       company=random_string("company", 10), address=random_string("address", 10),
                       home=random_string("home", 10), mobile=random_string("mobile", 10),
                       work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 10),
                       email2=random_string("email2", 10), email3=random_string("email3", 10),
                       homepage=random_string("homepage", 10), byear=random_string("byear", 10),
                       ayear=random_string("ayear", 10), address2=random_string("address2", 10),
                       phone2=random_string("phone2", 10), notes=random_string("notes", 10))
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
