class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color


class Plan(Transport):
    def __init__(self, model, year, color):
        super().__init__(model, year, color)
class Car(Transport):
    # constructor      parameters
    def __init__(self, model, year, color, penalties=0):
        # attributes
        super().__init__(model, year, color)
        self.penalties = penalties

    def driv(self, city):
        print(self.model, city)

    def sicnal(self, num_of_times, sound):
        while num_of_times > 0:
            print(f'Car {self.model} is signalling {sound}')
            num_of_times -= 1

class Truck(Car):
    def __init__(self, model, year, color, penalties=0, load_capasity=0):
        super().__init__(model, year, color, penalties)
        self.load_capasity = load_capasity

    def load_cargo(self, weight, product_type):
        if weight > self.load_capasity:
            print(self.load_capasity)
        else:
            print(product_type, weight)

number = 5
my_car = Car('bmv', 2022, 'black')
print(my_car)
print(my_car.model, my_car.year, my_car.color)
best_car = Car(year=2020, model='mers', color='whate')
print(best_car.model, best_car.year, best_car.color)
best_car.color = 'red'
print(best_car.model, best_car.year, best_car.color, best_car.penalties)
best_car.driv('osh')
best_car.sicnal(3, 'beep')
truc = Truck('volvo', 2013, 'blue', 500, 30000)
print(truc.model, truc.year, truc.color, truc.penalties, truc.load_capasity)
truc.load_cargo(25000, 'apple')