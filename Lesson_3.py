class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return f'model: {self.__model}, year: {self.__year}'

class FuelCar(Car):
    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank

    @property
    def fuel_bane(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.__model} is driving by battery')

    def __str__(self):
        return super().__str__() + f' fuel_bane: {self.__fuel_bank}'

class ElectronicCar(Car):
    def __init__(self):

some_car = Car('Audi', 2000)
print(some_car)
fuel_car = FuelCar('Audi 32', 2001, 21)
print(fuel_car)