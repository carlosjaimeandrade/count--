
class Number:
    def add(self, numberLabel):
        new = str(int(self.getRegister()) + 1)
        self.__setRegister(new)
        self.__update(numberLabel)

    def remove(self, numberLabel):
        new = str(int(self.getRegister()) - 1)
        self.__setRegister(new)
        self.__update(numberLabel)

    def returnDefault(self, numberLabel):
        default = "0"
        self.__setRegister(default)
        self.__update(numberLabel)

    def getRegister(self):
        register = open("register.txt","r")
        for linha in register:
            return linha
        register.close()

    def __setRegister(self, number):
        register = open('register.txt', 'w')
        register.write(number)

    def __update(self, numberLabel):
        numberLabel.config(text=self.getRegister())
