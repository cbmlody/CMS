class Submission:
    """Holds assignments submitted by students"""

    def __init__(self, title, submission_date, project, max_points):
        self.max_points = max_points
        self.title = title
        self.submission_date = submission_date
        self.project = project

    def grade(self, points, feedback):
        """Allows mentor to grade an assignment """
        self.points = points
        self.feedback = feedback
        return [self.title, self.points, self.max_points]
