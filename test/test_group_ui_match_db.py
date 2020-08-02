from model.group import Group
from fixture.db import clean_group_info_from_db


def test_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    ui_list = app.group.get_group_list()
    db_list = map(clean_group_info_from_db, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
