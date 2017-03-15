import sqlite3
from models.database import Database

class Checkpoint:

    def __init__(self, id_, user_id, card):
        self.id_ = id_
        self.user_id = user_id
        self.card = card

    @classmethod
    def get_all(cls):
        checkpoints = []
        conn, cur = Database.db_connect()
        checkpoints_list = cur.execute("SELECT * FROM `CHECKPOINTS`")
        for check in checkpoints_list:
            checkpoints.append(Checkpoint(*check))
        return checkpoints