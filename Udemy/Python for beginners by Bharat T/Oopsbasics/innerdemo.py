class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    class Engine:
        def __init__(self,numebr):
            self.numebr=numebr
        def start(self):
            print("engine started")

c=Car("bmw",2017)

e = c.Engine(123)
e.start()