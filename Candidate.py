### Sophie Hasara, Aakriti Shah, James McIntyre, Alex Hernandez ###
### class for candidate objects, information, and candidate form ###

class Candidate: 
    def __init__(self, name, party, gender, facts, agenda):
        self.name = name
        self.party = party
        self.gender = gender 
        self.facts = facts 
        self.agenda = agenda
    
    def getName(self):
        return self.name
        
    def setName(self, n):
        self.name = n
        
    def getParty(self):
        return self.party
        
    def setParty(self, p):
        self.party = p
        
    def getGender(self):
        return self.gender
        
    def setGender(self, g):
        self.gender = g
        
    def getFacts(self):
        return self.facts
    
    def setFacts(self, f):
        self.facts = f
        
    def getAgenda(self):
        return self.agenda
        
    def setAgenda(self, a):
        self.agenda
        
    def modifyFacts(self, i, f):
        self.facts[i] = f
        
    def modifyAgenda(self, i, a):
        self.agenda[i] = a
        
    def addFact(self, f):
        self.facts.append(f)
        
    def addTooAgenda(self, a):
        self.agenda.append(a)