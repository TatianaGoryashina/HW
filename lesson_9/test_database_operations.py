from database import Subjects


db_connection_strings = "postgresql://postgres:123@localhost:5432/postgres"
sub = Subjects(db_connection_strings)


def test_add_new():
    body = sub.get_subjects()
    len_before = len(body)

    title = "Autotest"
    sub.create(title)
    result = sub.get_subject(title)

    body = sub.get_subjects()
    len_after = len(body)

    sub.delete(result[0])

    assert len_after - len_before == 1
    assert result[0] == 200
    assert result[1] == title


def test_edit():
    title = "etiquette"
    sub.create(title)
    max_id = sub.get_max_id()

    new_title = "Updated_etiquette"
    sub.update(new_title, max_id)
    result = sub.get_subject(new_title)
    sub.delete(result[0])
    assert result[1] == new_title


def test_delete():
    title = "etiquette"
    sub.create(title)
    max_id = sub.get_max_id()

    sub.delete(max_id)
    max_id = sub.get_max_id()

    assert max_id != 200
