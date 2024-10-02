import math
import random


GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    numb_1 = random.randint(1, 5)
    numb_2 = random.randint(1, 5)
    question = f'{numb_1} {numb_2}'
    answer = math.gcd(numb_1, numb_2)
    return question, str(answer)
