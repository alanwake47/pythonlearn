from threading import Thread,Lock

class bookmybus:
    def __init__(self,availableseats):
        self.availableseats = availableseats
        self.l = Lock()

    def buy(self,seatsrequired):
        self.l.acquire()
        print("total seats available: ",self.availableseats)
        if(self.availableseats>=seatsrequired):

            print("Confirm a seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.availableseats-=seatsrequired
        else:
            print("sorry.no seats available")
        self.l.release()

obj = bookmybus(7)
t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(4,))
t3=Thread(target=obj.buy,args=(3,))

t1.start()
t2.start()
t3.start()