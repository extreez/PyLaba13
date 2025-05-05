#1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

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