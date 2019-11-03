from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling")
    def click(self):
        pass
  

class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Scrolling")
    def click(self):
        pass

    
class HPNotebook(HP):
    def scroll(self):
        super().scroll()
        print("scrolling is better in HP")
    def click(self):
        print("HP click click")

class DELLNotebook(Dell):
    def scroll(self):
        super().scroll()
        print("scrolling is worse in Dell")
    def click(self):
        print("Dell clackity clack")

hp1= HPNotebook()
hp1.click()
hp1.scroll()

dell1= DELLNotebook()
dell1.click()
dell1.scroll()

hp2=HP()
hp2.scroll()


