class Driver:

    def __init__(self, name, age, brand):
        self.__name = name
        self.__age = age
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def __eq__(self, other):
        return (self.get_name() == other.get_name()
                and self.get_age() == other.get_age()
                and self.get_brand() == other.get_brand())

    def __str__(self):
        return (f' Driver name: {self.__name}, age: {self.__age}, '
                f'brand: {self.__brand},')

    def __repr__(self):
        return str(self)


