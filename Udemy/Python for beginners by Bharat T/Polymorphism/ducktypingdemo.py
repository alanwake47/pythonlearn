class Duck:
    def talk(self):
        print("Quack Quack")
class Human:
    def talk(self):
        print("Hello")

def moshi(obj):
    obj.talk()

d=Duck()
moshi(d)

h=Human()
moshi(h)

