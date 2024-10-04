import random
import math
import operator as minus

GAME_QUESTION = 'What is the result of the expression?'


def get_correct_answer(numb_1, operator, numb_2):
    if operator == '+':
        return numb_1 + numb_2
    elif operator == '-':
        return numb_1 - numb_2
    elif operator == '*':
        return numb_1 * numb_2


def get_game_data():
    question_numb_1 = random.randint(1, 5)
    question_numb_2 = random.randint(1, 5)
    operator = random.choice(['+', '-', '*'])
    question = f"{question_numb_1} {operator} {question_numb_2}"
    answer = get_correct_answer(question_numb_1, question_numb_2, operator)
    if operator == '+':
        answer = sum([question_numb_1, question_numb_2])
    elif operator == '-':
        answer = minus.sub(question_numb_1, question_numb_2)
    elif operator == '*':
        answer = math.prod([question_numb_1, question_numb_2])
    return question, str(answer)
