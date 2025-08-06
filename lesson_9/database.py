from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Subjects:
    sql_st = {
        "select": text("SELECT * FROM subject"),
        "delete_by_id": text("DELETE FROM subject "
                             "WHERE subject_id = :id_to_delete"),
        "insert_new": text("INSERT INTO subject(subject_id, subject_title)"
                           " values (200, :title)"),
        "change": text("UPDATE subject SET subject_title = :new_title "
                       "WHERE subject_id = :id"),
        "get_max_id": text("SELECT MAX(subject_id) FROM subject"),
        "get_subject": text("SELECT * FROM subject "
                            "WHERE subject_title = :subject_title")
        }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        return self.__db.execute(self.sql_st["select"]).fetchall()

    def delete(self, subject_id):
        self.__db.execute(self.sql_st["delete_by_id"], id_to_delete=subject_id)

    def create(self, title):
        self.__db.execute(self.sql_st["insert_new"], title=title)

    def update(self, new_title, id):
        self.__db.execute(self.sql_st["change"], new_title=new_title, id=id)

    def get_max_id(self):
        return self.__db.execute(self.sql_st["get_max_id"]).fetchall()[0][0]

    def get_subject(self, title):
        return self.__db.execute(self.sql_st["get_subject"],
                                 subject_title=title).fetchall()[0]
