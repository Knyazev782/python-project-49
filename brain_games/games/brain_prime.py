import random
import math


GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(numb):
    if numb <= 1:
        return False
    for i in range(2, int(math.sqrt(numb)) + 1):
        if numb % i == 0:
            return False
    return True


def get_game_data():
    for i in range(3):
        question = random.randint(1, 10)
        if is_prime(question):
            answer = 'yes'
        else:
            answer = 'no'
        return question, answer


