# -*- coding: utf-8 -*-
from model.group import Group
import random
from fixture.db import clean_group_info_from_db


def test_delete_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        db_list = map(clean_group_info_from_db, new_groups)
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
