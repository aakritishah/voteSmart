### Sophie Hasara, Aakriti Shah, James McIntyre, Alex Hernandez ###
### class for poll location objects, information, location form, and printing location ###

class PollLocation:
  def __init__(self,streetNum,streetName,city,state,zip,hours):
    self.hours = hours
    self.streetNum = streetNum
    self.streetName = streetName
    self.city = city 
    self.state = state
    self.zip = zip 

    #getters & setters
    def getStreetNum(self):
        return self.streetNum
        
    def setStreetNum(num):
        self.streetNum = num
        
    def getStreetN(self):
        return self.streetName
        
    def setStreetName(num):
        self.streetName = num
        
    def setCity(c):
        self.city = c
        
    def getCity(self):
        return self.city
        
    def getState(self):
        return self.state
        
    def setState(s):
        self.state = s
        
    def getZip(self):
        return self.zip
        
    def setZip(z):
        self.zip = z
        
    def getHours(self):
        return hours
        
    def setHours(h):
        self.hours = h
    
    def setHour(i, j, h):
        self.hours[i][j] = h
  
    def printHours(self):
        for row in self.hours:
            for val in row:
                print('{:4}'.format(val), print())