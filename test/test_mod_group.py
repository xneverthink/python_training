# -*- coding: utf-8 -*-
from model.group import Group
import random
from fixture.db import clean_group_info_from_db


def test_mod_group(app, db, json_groups, check_ui):
    group_data = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.mod_group_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        db_list = map(clean_group_info_from_db, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
