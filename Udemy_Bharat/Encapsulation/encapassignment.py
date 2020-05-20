class Patient:
    def setID(self,id):
        self.__id = id
    def getID(self):
        return self.__id

    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    
    def setssn(self,ssn):
        self.__ssn=ssn
    def getssn(self):
        return self.__ssn

p=Patient()
p.setID(123)
p.setName("PSY")
p.setssn(77577)

print(p.getID())
print(p.getName())
print(p.getssn())
