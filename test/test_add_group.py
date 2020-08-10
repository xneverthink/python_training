# -*- coding: utf-8 -*-
from model.group import Group
from fixture.db import clean_group_info_from_db
import allure


def test_add_group(app, db, json_groups, check_ui):
    group_data = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step("When I add a group %s to the list" % group_data):
        app.group.create(group_data)
    with allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        #assert len(old_groups) + 5 == len(new_groups)
        old_groups.append(group_data)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        db_list = map(clean_group_info_from_db, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
