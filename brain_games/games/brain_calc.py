import random
import math
import operator

GAME_QUESTION = 'What is the result of the expression?'


def get_correct_answer(numb_1, operators, numb_2):
    if operators == '+':
        return numb_1 + numb_2
    elif operators == '-':
        return numb_1 - numb_2
    elif operators == '*':
        return numb_1 * numb_2


def get_game_data():
    question_numb_1 = random.randint(1, 5)
    question_numb_2 = random.randint(1, 5)
    operators = random.choice(['+', '-', '*'])
    question = f"{question_numb_1} {operators} {question_numb_2}"
    answer = get_correct_answer(question_numb_1, question_numb_2, operators)
    if operators == '+':
        answer = sum([question_numb_1, question_numb_2])
    elif operators == '-':
        answer = operator.sub(question_numb_1, question_numb_2)
    elif operators == '*':
        answer = math.prod([question_numb_1, question_numb_2])
    return question, str(answer)
