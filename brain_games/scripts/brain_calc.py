import random
import math
import operator

print('May I have your name? ', end='')
name = input("Enter your name: ")
print(f"Hello, {name}!")

def calc():
    for i in range(3):
        numb_1 = random.randint(1, 5)
        numb_2 = random.randint(1, 5)
        operation = random.choice(['+', '-', '*'])
        examples = f"{numb_1} {operation} {numb_2}"
        print('Question: ' + examples)
        player_answer = int(input('Your answer: '))
        correct_answer = None
        if operation == '+':
            correct_answer = sum([numb_1, numb_2])
        elif operation == '-':
            correct_answer = operator.sub(numb_1, numb_2)
        elif operation == '*':
            correct_answer = math.prod([numb_1, numb_2])
        if player_answer == correct_answer:
            print('Correct!')
        elif player_answer != correct_answer:
            print(f"'{player_answer}' is a wrong answer ;(. The correct answer was '{correct_answer}'. \nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')



calc()