from threading import Thread,current_thread

#Even Numbers Thread
def even():
    i=0
    print(current_thread().getName())
    for i in range(1,101):
        if (i%2==0):
            print(i)
        else:
            pass
            

#Odd Numbers Thread
def odd():
    j=0
    print(current_thread().getName())
    for j in range(100):
        if (j%2!=0):
            print(j)
        else:
            pass

print(current_thread().getName())
for k in range(101):
    print(k)

t1=Thread(target=even)
t1.start()

t2=Thread(target=odd)
t2.start()
