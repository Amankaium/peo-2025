from random import randint
from time import sleep


def count_kef(height, weight):
    print(height, weight, height / weight)
    sleep(2)


while True:
    random_height = randint(100, 190)
    random_weight = randint(10, 200)
    count_kef(random_height, random_weight)
