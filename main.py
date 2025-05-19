#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print()

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")


    #3
    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг у ресторна {self.restaurant_name} - {self.rating}")


#14.1
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=None):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors if flavors else []

    def display_flavors(self):
        print("Доступные сорта мороженого: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

#14.2
    def set_location_and_hours(self, location, hours):
        self.location = location
        self.hours = hours

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def has_flavor(self, flavor):
        return flavor in self.flavors

    def display_flavor_types(self):
        print("типы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")



new_restaurant = Restaurant("Italiani", "Итальянская")
print("--Описание ресторана--")
print(f"Название: {new_restaurant.restaurant_name}")
print(f"Тип кухни: {new_restaurant.cuisine_type}")

print("\n\n--Описание методами--")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

for i in range(3):
    print()
#2
restik1 = Restaurant("Sakura", "Японска")
restik2 = Restaurant("La Table", "Французская")
restik3 = Restaurant("Tandoori", "Индийская")

restik1.describe_restaurant()
restik2.describe_restaurant()
restik3.describe_restaurant()

restik1.update_rating(4.5)
restik2.update_rating(4.8)
restik3.update_rating(4.2)

print("\n", "---", "\n")
#add
from random import *
input_restik = Restaurant(input(f"Напишите название вашего ресторна "),input("Какой тип кухни у вашего ресторна "))
input_restik.describe_restaurant()
input_restik.open_restaurant()
input_restik.update_rating(randint(10, 50)/10)


#14.test
stand = IceCreamStand("Мороженка", "Десерты", ["ванильное", "шоколадное"])
stand.describe_restaurant()
stand.display_flavors()

stand.set_location_and_hours("Центр города", "10:00 - 20:00")
print(f"Локация: {stand.location}, Время работы: {stand.hours}")

stand.add_flavor("клубничное")
stand.remove_flavor("ванильное")
print("Есть ли клубничное?", "Да" if stand.has_flavor("клубничное") else "Нет")

stand.display_flavor_types()