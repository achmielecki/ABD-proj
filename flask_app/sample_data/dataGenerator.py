from random import randrange
from random import randint
import random
import os
from typing import Callable
from faker import Faker
from time import time
from datetime import date
from calendar import monthrange
from shutil import copyfile

Faker.seed(time())
fake = Faker('pl_PL')
csv_separator = ","

shifts = ["rano", "popoludnie", "noc", ]


def get_random_salary(min, max):
    return randint(min, max)


def get_random_shift():
    return random.choice(shifts)


def get_random_magazine_id(magazines_count):
    return str(randint(1, magazines_count))


def get_worker_mail(i):
    return "workermail" + str(i) + "@gmail.com"


def generate_worker(i: int, magazines_count):
    return str(i) + csv_separator \
           + fake.first_name() + csv_separator \
           + fake.first_name() + csv_separator \
           + get_worker_mail(i) + csv_separator \
           + str(get_random_salary(2500, 5000)) + csv_separator \
           + get_random_shift() + csv_separator \
           + get_random_magazine_id(magazines_count)


def random_postal_code():
    return str(randint(11, 99)) + "-" + str(randint(100, 999))


def country():
    if randint(1, 10) > 4:
        return "Polska"
    else:
        return fake.country()


def generate_magazine(i: int):
    return str(i) + csv_separator \
           + fake.city() + csv_separator \
           + fake.street_name() + csv_separator \
           + random_postal_code() + csv_separator \
           + country()


def gen_magazines(start: int, count: int):
    path = os.path.dirname(__file__)
    f = open(os.path.join(path, "magazines.csv"), "a", encoding='utf-16')
    f.write("id,city,street,postal_code,country\n")
    for i in range(start, count + start):
        f.write(generate_magazine(i) + '\n')
    f.close()


def gen_workers(start: int, count: int):
    path = os.path.dirname(__file__)
    f = open(os.path.join(path, "workers.csv"), "a", encoding='utf-16')
    f.write("id,name,surname,email,salary,shift,magazine_id\n")
    for i in range(start-1, count + start):
        f.write(generate_worker(i, start) + '\n')
    f.close()


def generate_director(i: int, magazines_count):
    return str(i) + csv_separator \
           + fake.first_name() + csv_separator \
           + fake.first_name() + csv_separator \
           + fake.company_email() + csv_separator \
           + str(get_random_salary(12500, 50000)) + csv_separator \
           + str(i)


def gen_directors(start: int, count: int):
    path = os.path.dirname(__file__)
    f = open(os.path.join(path, "directors.csv"), "a", encoding='utf-16')
    f.write("id,name,surname,email,salary,magazine_id\n")
    for i in range(start, count + start):
        f.write(generate_director(i, magazines_count) + '\n')
    f.close()


if __name__ == "__main__":
    magazines_count = 100
    workers_count = 300000

    gen_magazines(1, magazines_count)
    gen_directors(1, magazines_count)
    gen_workers(magazines_count, workers_count)
