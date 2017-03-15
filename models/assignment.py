from .database import Database



class Assignment:
    """Holds assignments, created by mentors"""

    assignment_list = []

    def __init__(self, id_, title, due_date, max_points, as_team='NULL'):
        self.id_ = id_
        self.title = title
        self.due_date = due_date
        self.max_points = max_points
        self.as_team = as_team

    @classmethod
    def get_all(cls):
        assignments = []
        conn, cur = Database.db_connect()
        assignments_list = cur.execute("SELECT * FROM `ASSIGNMENTS`").fetchall()
        for assign in assignments_list:
            assignments.append(Assignment(*assign))
        return assignments

    @staticmethod
    def add(title, due_date, max_points, as_team):
        conn, cur = Database.db_connect()
        try:
            cur.execute("INSERT INTO `ASSIGNMENTS` (title, due_date, max_points, as_team) VALUES (?,?,?,?)",
                        (title, due_date, max_points, as_team,))
            conn.commit()
        except Exception:
            return "Record already exists"
        finally:
            conn.close()

    @staticmethod
    def get_by_id(id):
        """ Retrieves assignment with given id from database.
        Args:
            id(int): item id
        Returns:
            Assignment: Assignment object with a given id
        """
        con,cur = Database.db_connect()
        assignment = cur.execute("SELECT * FROM `ASSIGNMENTS`WHERE ID = ?", (id,)).fetchone()
        return Assignment(*assignment)