# class Animal:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     @property
#     def name (self,):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#     @name.setter
#     def name(self,name):
#          self.__name = name
#     @age.setter
#     def age(self,age):
#          self.__age = age
#     def make_sound(self):
#         print("Животное издает звук")
# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)
#
#     def make_sound(self):
#         print("гав гав")
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def make_sound(self):
#         print("мяу мяу")
#
# dog = Dog("бобик", 3)
# cat = Cat("Мурка", 2)
# print(f"Имя собаки: {dog.name}, возраст: {dog.age}")
# print(f"Имя кошки: {cat.name}, возраст: {cat.age}")
# dog.make_sound()
# cat.make_sound()
#
#
# dog.name = "шарик"
# dog.age = 4
# cat.name = "соня"
# cat.age = 5
#
#
# print(f"Новое имя собаки: {dog.name}, новый возраст: {dog.age}")
# print(f"Новое имя кошки: {cat.name}, новый возраст: {cat.age}")
#
#
# dog.make_sound()
# cat.make_sound()
#
