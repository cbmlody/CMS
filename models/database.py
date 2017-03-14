import sqlite3 as sql


class Database:
    """
    Class for database connection handling
    """

    @staticmethod
    def import_sql():
        """
        Method import sql file
        """
        con, cur = Database.db_connect()
        with open('database.sql', 'r') as file:
            cur.executescript(file.read())

    @classmethod
    def db_connect(cls):
        con = sql.connect('database.db')
        cur = con.cursor()
        return con, cur
