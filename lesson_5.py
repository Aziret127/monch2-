class swimm:
    def move(self):
        return f"Плавает"

class Flyable:
    def move(self):
        return f"Летает"

class Animal :
    def move(self):
        return f"Двигается"

class Duck(Flyable, Animal,swimm ):
    def move(self):
        return "может плавать летать и ходить"

donal_duck = Duck()
print(donal_duck.move())
print(Duck.__mro__)


