import random
import math
import operator
from brain_games.scripts.cli import welcome_user


def operation(numb_1, operations, numb_2):
    if operations == '+':
        return sum([numb_1, numb_2])
    elif operations == '-':
        return operator.sub(numb_1, numb_2)
    elif operations == '*':
       return math.prod([numb_1, numb_2])

def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    for i in range(3):
        numb_1 = random.randint(1, 5)
        numb_2 = random.randint(1, 5)
        operations = random.choice(['+', '-', '*'])
        print('Question: ' f"{numb_1} {operations} {numb_2}")
        player_answer = int(input('Your answer: '))
        correct_answer = operation(numb_1, operations, numb_2)
        if player_answer == correct_answer:
            print('Correct!')
        elif player_answer != correct_answer:
            print(f"'{player_answer}' is a wrong answer ;(. The correct answer was '{correct_answer}'. "
                  f"\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

def main():
    print('Welcome to the Brain Games!')
    calc()

if __name__ == "__main__":
    main()
