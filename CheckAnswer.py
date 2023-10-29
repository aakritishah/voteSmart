# class that checks user input
class CheckAnswer(object):
    #pScore = printScore()
    def __init__(self, answer):
        self.answer = answer

    def __call__(self, answer):
        self.answer = answer