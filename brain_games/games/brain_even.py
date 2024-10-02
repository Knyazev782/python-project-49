import random

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
     question = random.randint(1, 100)
     if question % 2 == 0:
        answer = 'yes'
     else:
        answer = 'no'
        return question, answer
