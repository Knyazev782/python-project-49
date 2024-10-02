import random

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    random_number = random.randint(1, 100)
    question = random_number
    if question % 2 == 0:
     answer = 'yes'
    else:
     answer = 'no'
    return question, answer
