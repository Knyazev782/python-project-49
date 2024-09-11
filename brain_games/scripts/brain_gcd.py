import math
import random


print('May I have your name? ', end='')
name = input("Enter your name: ")
print(f"Hello, {name}!")


print('Find the greatest common divisor of given numbers.')
def gcd():
    for i in range(3):
        numb_1 = random.randint(1, 5)
        numb_2 = random.randint(1, 5)
        examples = f'{numb_1} {numb_2}'
        print('Question: ' + examples)
        player_answer = int(input('Your answer: '))
        if player_answer == math.gcd(numb_1, numb_2):
            print('Correct!')
        elif player_answer != math.gcd(numb_1, numb_2):
            print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{math.gcd(numb_1, numb_2)}'\nLet's try again, {name}!")
            return
    print(f'Congratulations {name}!')

gcd()