class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money
        
    @property
    def sallary(self):
        return self.__money
    
    @sallary.setter
    def sallary(self, value):
        if value < 0:
            print('you are not abelto add')
        else:
            self.__money += value
        

sumsu = User('ali', 23, 2356)

sumsu.sallary = 400

print(sumsu.sallary)