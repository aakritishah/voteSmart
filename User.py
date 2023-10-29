### Sophie Hasara, Aakriti Shah, James McIntyre, Alex Hernandez ###
### class for user objects, information, register form, and location form ###

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

class User: 
    users = []
    id = 0
    
    def __init__(self, name, users):
        self.name = name
        User.id += 1
        self.id = User.id
        self.zip = 0
        self.quizzes = []
        self.party = ""
        users.append(self)
        
    def getName(self):
        return self.name 
        
    def setName(self, n):
        self.name = n
        
    def getID(self):
        return self.id
        
    def setID(self, num):
        self.id = num
        
    def getZip(self):
        return self.zip
        
    def setZip(self, z):
        self.zip = z
        
    def getQuizzes(self):
        return self.quizzes
        
    def setQuizzes(self, arr):
        self.quizzes = arr
        
    def hasParty(self) :
        if self.party == "":
            return False
            
    def getParty(self):
        return self.party
        
    def setParty(self, p):
        self.party = p
        
    def addQuiz(quizzes, q):
        quizzes.append(q)