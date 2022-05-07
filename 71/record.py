class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.maxScore = -1000

    def record(self, score):
        if score > self.maxScore:
            self.maxScore = score

    def __call__(self, score):
        self.record(score)
        return self.maxScore
