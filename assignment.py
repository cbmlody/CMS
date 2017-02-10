class Assignment:
    """Holds assignments, created by mentors"""


    def __init__(self, title, description, due_date, max_points):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.max_points = max_points


    def __str__(self):
        return "{}\n{}\nTask is due to {}. Student can aquire maximum {} points.\n".format(self.title, self.description,
                                                                                           self.due_date,
                                                                                           self.max_points)


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
