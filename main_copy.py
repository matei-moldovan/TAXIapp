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

    def __str__(self):
        return (f'plate number: {self.__plate_number}, brand: {self.__brand}, '
                f'horse power: {self.__hp}, mileage: {self.__mileage}')

    def __repr__(self):
        return str(self)


def print_menu():
    print("1. Add car")
    print("2. Delete car")
    print("3. Average car mileage")
    print("4. Most common brand")
    print("5. Show car list")
    print("0. Exit menu")


def add_car(car_list):
    plate_number = int(input("Plate number: "))
    brand = str(input("Brand: "))
    hp = int(input("Horse power: "))
    mileage = int(input("Mileage: "))
    car_list.append(Car(plate_number, brand, hp, mileage))


def get_car(car_list, plate_number):
    for car in car_list:
        if car.get_plate_number() == plate_number:
            return car


def remove_car(car_list):
    plate_number = int(input(" Type the plate number of the car you want to delete from the list: "))
    car = get_car(car_list, plate_number)
    if car is not None:
        car_list.remove(car)
        print(" The new car list is:")
        show_car_list(car_list)
    else:
        print(f'{plate_number} is not a valid plate number for any car')


def show_car_list(car_list):
    for car in car_list:
        print(car)


def average_car_mileage(car_list):
    sum_of_mileage = 0
    for car in car_list:
        sum_of_mileage += car.get_mileage()
    average_mileage = sum_of_mileage / len(car_list)
    print(f'The average car mileage in the TAXI company is {average_mileage}')


def compose_distinctive_brand_list(car_list):
    brand_list = []
    for i in range(len(car_list)):
        try:
            brand_list.index(car_list[i].get_brand())
        except:
            brand_list.append(car_list[i].get_brand())

    return brand_list


def myFunc(e):
    return e['count']


def most_common_brand(car_list):
    brand_list = compose_distinctive_brand_list(car_list)
    popularity = []
    for brand in brand_list:
        count = 0
        for a in car_list:
            if brand == a.get_brand():
                count += 1
        popularity.append({'brand': brand, 'count': count})
    print(popularity)
    popularity.sort(reverse=True, key=myFunc)
    print(popularity)
    print(popularity[0]['brand'])

    # most_common = ''
    # brand_list = compose_brand_list(car_list)
    # max_popularity = int(-1)
    #
    # for i in range(len(brand_list)):
    #     popularity = int(0)
    #
    #     for j in range(len(car_list)):
    #
    #         if brand_list[i] == car_list[j].get_brand():
    #             popularity += 1
    #             most_common = brand_list[i]
    #
    #     if popularity > max_popularity:
    #         max_popularity = popularity
    #         most_common = brand_list[i]
    #
    # print(most_common)


def drive(plate_number=None):
    car_list = [Car(2345, 'BMW', 235, 15000),
                Car(1234, 'Toyota', 235, 15000),
                Car(555, 'Toyota', 235, 20000),
                Car(111, 'Jaguar', 235, 10000),
                Car(222, 'Toyota', 235, 40000)]
    while True:
        print_menu()
        try:
            command = int(input(" Chose the command: ").strip())
            if command == 0:
                return
            elif command == 1:
                add_car(car_list)
            elif command == 2:
                remove_car(car_list)
            elif command == 3:
                average_car_mileage(car_list)
            elif command == 4:
                most_common_brand(car_list)
            elif command == 5:
                show_car_list(car_list)
        except:
            print(" Make sure to enter one 'int' type character")


drive()
