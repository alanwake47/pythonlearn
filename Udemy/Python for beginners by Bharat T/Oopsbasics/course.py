class Course:
    def __init__(self,name,ratings):
        self.name= name
        self.ratings= ratings
    
    def average(self):
        numberofrating= len(self.ratings)
        average = sum(self.ratings)/numberofrating
        print("average rating",self.name,"is",average)

c1= Course('Pydev',[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2= Course('Java',[5,5,5,5])
print(c2.name)
print(c2.ratings)
c2.average()
