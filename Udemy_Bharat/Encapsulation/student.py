class Student:
    def setID(self,id):
        self.id = id
    def getID(self):
        return self.id

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    '''def __init__(self):
        self.__id=123
        self.name="Sid"
    def display(self):
        print(self.__id)
        

#non private fields
s=Student()
print(s.name)

#function inside class for private fields
s.display()

#Name mangling
print(s._Student__id)'''

s=Student()
s.setID(123)
s.setName("aman")
print(s.getID())
print(s.getName())