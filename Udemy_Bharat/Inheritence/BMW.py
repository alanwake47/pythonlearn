from abc import abstractmethod,ABC
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stop the car")
    #contract for child classes to follow parent classes otherwise error
    @abstractmethod
    def drive(self):
        pass

#inheriting BMW
class ThreeSeries(BMW):
    def __init__(self,cruiseControlEnabled,make,model,year):
        #using Super()
        super().__init__(make,model,year)
        self.cruiseControlEnabled = cruiseControlEnabled
    def display(self):
        print(self.cruiseControlEnabled)
    #Overriding functinality + adding functionality using super()
    def start(self):
        super().start()
        print("Button Start")
    def drive(self):
        print("three series being driven")
    
class FiveSeries(BMW):
    def __init__(self,ParkingAssistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.ParkingAssistEnabled = ParkingAssistEnabled  
    def drive(self):
        print("five series being driven")

threeSeries=ThreeSeries(True,"BMW","328i","2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

#inherited functions from BMW parent class
threeSeries.start()
threeSeries.stop()

threeSeries.display()