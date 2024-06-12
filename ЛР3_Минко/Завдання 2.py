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
import datetime

class Person:
 def modifier(filename):
    """Зчитує дані з файлу, створює об'єкти Person,
    модифікує та зберігає дані в новому файлі.
    """
    persons = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                if len(data) == 3:
                    surname, first_name, birth_date = data
                    person = Person(surname, first_name, birth_date)
                elif len(data) == 4:
                    surname, first_name, birth_date, nickname = data
                    person = Person(surname, first_name, birth_date, nickname)
                else:
                    raise ValueError("Невірний формат даних у файлі.")
                persons.append(person)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return

    # Модифікуємо дані та записуємо їх у новий файл
    modified_filename = filename.replace('.', '_modified.')
    with open(modified_filename, 'w') as f:
        for person in persons:
            f.write(f"{person.surname},{person.first_name},{person.get_fullname()},{person.birth_date},{person.nickname if person.nickname else ''},{person.get_age()}\n")

    print(f"Модифіковані дані збережено у файлі: {modified_filename}")

# Приклад використання:
 modifier("contacts.txt")