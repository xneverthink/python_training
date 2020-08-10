# -*- coding: utf-8 -*-
from model.group import Group
import random
from fixture.db import clean_group_info_from_db
import allure


def test_delete_random_group(app, db, check_ui):
    with allure.step("If group list is empty, I add a new group"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="test"))
    with allure.step("Given a random group from group list"):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with allure.step("When I delete given group %s" % group):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old list with removed group "
                     "and it's length is smaller by one"):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
    if check_ui:
        db_list = map(clean_group_info_from_db, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
