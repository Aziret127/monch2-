from abc import ABC, abstractmethod

class Animal(ABC):
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print('Dog')
class Cat(Animal):
    def make_sound(self):
        print('Cat')


puppy = Dog()
puppy.make_sound()
kitter = Cat()
kitter.make_sound()

