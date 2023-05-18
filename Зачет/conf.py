from faker import Faker
from random import randint, uniform
import itertools

fake = Faker("ru_RU")

def title():
    filename = "book.txt"
    line_num = randint(0, 10)
    with open(filename) as file:
        lines = itertools.islice(file, line_num - 1, line_num)
        line = next(lines)
    return line

def year():
    return randint(1900, 2023)

def pages():
    return randint(100, 500)

def isbn13():
    return fake.isbn13()

def rating():
    return round(uniform(0, 5),  2)

def price():
    return round(uniform(1, 2000),  2)

def generate_fio(func):
    def wrapper():
        lst = []
        for i in range(randint(1, 3)):
            lst.append(func())
        lst = ', '.join(lst)
        return lst
    return wrapper

@generate_fio
def author():
    first_name = fake.first_name()
    last_name = fake.last_name()
    patronymic = fake.first_name()
    short_fio = f"{last_name} {first_name[0]}. {patronymic[0]}."
    return short_fio
