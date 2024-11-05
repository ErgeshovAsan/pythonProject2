class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def info(self):
        return f'name: {self.__name}, age: {self.__age}, birth year: {2024 - self.__age}'

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def info(self):
        return super().info()

class Dog(Animal):
    def __init__(self, name, age, command):
        super().__init__(name, age)
        self.__command = command

    def info(self):
        return super().info() + f' command: {self.__command}'

    @property
    def commands(self):
        return self.__command
    @commands.setter
    def commands(self, value):
        self.__command = value

# animel = Animal('Arin', 3)
# animel.set_age(4)
# print(animel.info())
cat = Cat("tom", 5)
dog = Dog('boby', 3, 'sit')
dog.commands = 'sit, run'
print(dog.commands)

list = [cat, dog]
for anim in list:
    print(anim.info())