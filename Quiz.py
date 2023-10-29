### Sophie Hasara, Aakriti Shah, James McIntyre, Alex Hernandez ###
### class for quiz objects, information, declaring quiz questions, quiz form and calculating results ###

import logging
logging.basicConfig(filename='record.log', level=logging.DEBUG)

class Quiz: 
  def __init__(self, formNum, questions):
    self.formNum = formNum
    self.questions = questions 
    self.answers = []
    
    #percents added in calculateScore
    partyPercents = []

    #getters and setters
    def getFormNum(self):
        return self.formNum

    def setFormNum(fNum):
        self.formNum = fNum
        
    def getQuestions(self):
        return self.questions
        
    def setQuestions(arr):
        self.questions = arr
        
    def getAnswers(self):
        return self.answers
        
    def setAnswers(arr):
        self.answers = arr
        
    def calculateScore(self, user, partyPercents, answers):
        for i in self.answers:
            partyPercents[answers[i]] += 1
            
        #num for keeping track of highest score
        num = 0
        for j in self.partyPercents:
            if partyPercents[i] > num:
                num = partyPercents[i]
            user.setParty(num)
        
        
    def printQuiz(self):
       for i in self.questions:
        print(questions[i])