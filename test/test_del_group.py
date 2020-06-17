import time


def test_delete_first_group(app):
    time.sleep(1)
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()