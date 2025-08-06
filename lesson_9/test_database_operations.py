from database import Subjects
from sqlalchemy import create_engine
import pytest


db_connection_strings = ""
db = create_engine(db_connection_strings)


def test_add_new(db):
    sub = Subjects(db)
    body = db.sub.get_subjects()
    len_before = len(body)

    title = "Autotest"
    result = sub.create(title)
    new_id = result["subject_id"]

    body = sub.get_subjects()
    len_after = len(body)

    sub.delete(new_id)

    assert len_after - len_before == 1
    for title in body:
            if title["subject_id"] == new_id:
                assert title["subject_title"] == title
                assert title["subject_id"] == new_id

def test_edit():
    title = "etiquette"
    db.create(title)
    max_id = db.get_max_id()

    new_title = "Updated_etiquette"
    update = db.update(max_id, new_title)

    db.delete(max_id)

    assert update["subject_title"] == new_title

def test_delete():
    title = "etiquette"
    db.create(title)
    max_id = db.get_max_id()

    deleted = db.delete(max_id)

    assert deleted["subject_id"] == max_id

    rows = db.get_subject(max_id)
    assert len(rows) == 0
