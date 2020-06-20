# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_first_group_name(app):
    app.group.mod_first_group(Group(name="New Name"))


def test_mod_first_group_header(app):
    app.group.mod_first_group(Group(header="New Header"))


def test_mod_first_group_footer(app):
    app.group.mod_first_group(Group(footer="New Footer"))
