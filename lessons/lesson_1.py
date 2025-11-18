class Car:
    #git checkout -b branch_nameинициализатор
    def __init__(self, color, model):
            self.color = color
            self.model = model
    def drive(self,location):
        print(f"Car {self.model} is driving in {location}")

    def test(self):
            self.drive("Karakol")

class MySuperBigCar:
    pass
color = "red"
car_honda = Car(color="red", model="Honda")
car_Subaru = Car(color="red", model="Subaru")

car_Subaru.drive("Naryn")
car_Subaru.drive("Bishkek")
print(car_Subaru)
print(car_honda)
print(car_Subaru.color)
print(car_honda.color)
print(car_Subaru.model == car_honda.model)

# class Bus(Car):
#     def draw(self,location):
#         print(f"Bus {self.model} is driving in {location}")
    # def test_bus(self


# stage
#
# production  - V1.0.0.0
#
#
# feat/
# fix/
# update/
# hotfix/
# delete/
#
#
# git commit -m "fix: fixing bug on login page"
# git commit -m "feat: add new feature"
# git commit -m "update: update feature"
# git commit -m "hotfix: fix bug on login page"
#
# git commit -m "hotfix: fix bug on login page"