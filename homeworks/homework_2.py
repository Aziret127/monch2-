


class Person :
    def __init__(self, name, birth_date, occupation,  higher_education):
            self.name = name
            self.birth_date = birth_date
            self.occupation = occupation
            self.higher_education = higher_education

    def introduce (self):
            print(f" Меня зовут  {self.name}. Я родился {self.birth_date}. Мой профессия{self.occupation}.У меня нет высшее образование{self.higher_education}")

class Classmate(Person):
    def __init__(self,name, birth_date, occupation,  higher_education, group_name ):
        super().__init__(name, birth_date, occupation, higher_education )
        self.group_name = group_name
    def introduce (self):
        super().introduce()
        print(f"мой гуппа {self.group_name}")



class Friend(Person):
    def __init__(self,name, birth_date, occupation, higher_education, hobby ):
           super().__init__(name, birth_date, occupation,higher_education)
           self.hobby = hobby
    def introduce (self):
           super().introduce()
           print(f"хобби друга {self.hobby}")
class BestFriend(Friend):
    def __init__(self,name, birth_date, occupation, higher_education, hobby, shared_memory ):
          super().__init__(name,birth_date,occupation,higher_education,hobby, )
          self.shared_memory = shared_memory
    def introduce (self):
           super().introduce()
           print(f"Есть что спомнить {self.shared_memory}")

person = Person("Азамат", "12.05.2000", "Ветеринар", "Да")

classmate = Classmate("Бекзат", "20.03.2001", "Студент", "Нет", "Geeks 60-1")

friend = Friend("Эрмек", "15.07.1999", "Программист", "Да", "играть в шахматы")

bestFriend = BestFriend("Артур" ,"16.06.2000","МЧС","да","футбол", "Лучшие")


# person.introduce ()
# classmate.introduce()
# friend.introduce()
# BestFriend.introduce()

for person in [person, classmate, friend, bestFriend]:
  person.introduce()

