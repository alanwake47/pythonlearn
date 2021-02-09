class Flight:
    def __init__(self,engine):
        self.engine=engine
    def startengine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("starting airbus engine")

class BGEngine:
    def start(self):
        print("starting BG engine")

ae= AirbusEngine()
f= Flight(ae)
f.startengine()

be= BGEngine()
f1= Flight(be)
f1.startengine()