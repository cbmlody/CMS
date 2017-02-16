import database


class Assignment:
    """Holds assignments, created by mentors"""

    assignment_list = []


    def __init__(self, ID, title, due_date, max_points, as_team='NULL'):
        self.ID = ID
        self.title = title
        self.due_date = due_date
        self.max_points = max_points
        self.as_team = as_team


    @classmethod
    def import_from_db(cls):
        assign_list = database.Database.cur.execute("SELECT * FROM `ASSIGNMENTS`")
        for assignment in assign_list.fetchall():
            Assignment(*assignment)

class Submission:
    """Holds assignments submitted by students"""


    def __init__(self, title, submission_date, project, max_points):
        self.max_points = max_points
        self.title = title
        self.submission_date = submission_date
        self.project = project


    def __str__(self):
        return "Student submitted {} assignment on {}.\nLink: {}".format(self.title, self.submission_date, self.project)

    def grade(self, points, feedback):
        """Allows mentor to grade an assignment """
        self.points = points
        self.feedback = feedback
        return "{}: {}/{} points".format(self.title, self.points, self.max_points)
