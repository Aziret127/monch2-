from datetime import datetime

class Person :
    def __init__(self, name, birth_date, occupation,  higher_education):
             self.name = name
             self.__birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
             self.__occupation = occupation
             self.__higher_education = higher_education

    @property
    def age(self):
        today = datetime.today()
        years = today.year - self.__birth_date.year
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
          years -= 1

        return years

    def get_brith_date(self):
        return self.__birth_date.strftime("%Y-%m-%d")

    def get_occupation(self):
        return self.__occupation

    def set_higher_education(self, value):
         self.__higher_education = value

    def introduce (self):
             print(f"Меня зовут {self.name}. "
              f"Я родился {self.get_brith_date()}. "
              f"Моя профессия {self.__occupation}. "
              f"Высшее образование: {self.__higher_education}. "
              f"Возраст: {self.age}")

class Classmate(Person):
    def __init__(self,name, birth_date, occupation,  higher_education, group_name):
         super().__init__(name, birth_date, occupation, higher_education)
         self.group_name = group_name
    def introduce (self, ):
          super().introduce()
          print(f"мой гуппа {self.group_name}")

class Friend(Person):
     def __init__(self,name, birth_date, occupation, higher_education, hobby):
            super().__init__(name, birth_date, occupation,higher_education,)
            self.hobby = hobby
     def introduce (self):
            super().introduce()
            print(f"хобби друга {self.hobby}")
person = Person("Азамат", "2000-05-12", "Ветеринар", "Да")
person.introduce()
print()

classmate = Classmate("Бекзат", "2001-03-20", "Студент", "Нет", "Geeks 60-1")
classmate.introduce()
print()

friend = Friend("Эрмек", "1999-07-15", "Программист", "Да", "играть в шахматы")
friend.introduce()

fr1 = Friend("Айбек", "2000-02-20", "студент", "нет", "футбол")
fr1.introduce()
print(fr1.age) # 25





