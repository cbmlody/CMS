from models.database import Database


class Checkpoint:

    def __init__(self, user_id, card):
        self.user_id = user_id
        self.card = card

    @classmethod
    def update_user_card(cls, card, user_id):
        conn, cur = Database.db_connect()
        try:
            cur.execute("INSERT OR IGNORE INTO `CHECKPOINTS` VALUES (?,?)", (user_id, card))
            cur.execute("UPDATE `CHECKPOINTS` SET card=(?) WHERE user_id = (?)", (card, user_id))
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def get_card(user_id):
        conn, cur = Database.db_connect()
        try:
            card = cur.execute("SELECT card FROM `CHECKPOINTS` WHERE user_ID = (?)", (user_id,)).fetchone()[0]
        except TypeError:
            card = 'none'
        finally:
            conn.close()
        return card
