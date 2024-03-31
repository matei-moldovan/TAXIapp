class Car:
    def __init__(self, plate_number, brand, hp, mileage):
        self.__plate_number = plate_number
        self.__brand = brand
        self.__hp = hp
        self.__mileage = mileage

    def get_plate_number(self):
        return self.__plate_number

    def get_brand(self):
        return self.__brand

    def get_hp(self):
        return self.__hp

    def get_mileage(self):
        return self.__mileage

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

    def set_hp(self, hp):
        self.__hp = hp

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def __eq__(self, other):
        return self.get_plate_number() == other.get_plate_number()

    def __str__(self):
        return (f'plate number: {self.__plate_number}, brand: {self.__brand}, '
                f'horse power: {self.__hp}, mileage: {self.__mileage}')

    def __repr__(self):
        return str(self)
