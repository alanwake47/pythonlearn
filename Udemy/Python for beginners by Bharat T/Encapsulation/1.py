class Patient:

    def setId(self,Id):

        self.__Id = Id

    def setName(self,Name):

        self.__Name = Name

    def setSSN(self, SSN):

        self.__SSN = SSN

    def getId(self):

        return self.__Id

    def getName(self):

        return self.__Name

    def getSSN(self):

        return self.__SSN


P = Patient()

P.setId(1)

P.setName("John Doe")

P.setSSN(543)


print(f"{P.getName()} has Id: {P.getId()} and SSN: {P.getSSN()}")