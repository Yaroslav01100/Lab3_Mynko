import datetime
class Person:
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        year, month, day = map(int, birth_date.split('-'))
        self.birth_date = datetime.date(year, month, day)
    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (
                today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return str(age)
    def get_fullname(self):
        return f"{self.surname} {self.first_name}"
person1 = Person("Петренко", "Іван", "1974-10-25", "Ваня")
person2 = Person("Сосюра", "Ольга", "1989-10-25", "Оля")
print(f"{person1.get_fullname()} ({person1.nickname}), вік: {person1.get_age()}")
print(f"{person2.get_fullname()} ({person2.nickname}), вік: {person2.get_age()}")