import math
import random
from brain_games.scripts.cli import welcome_user


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        numb_1 = random.randint(1, 5)
        numb_2 = random.randint(1, 5)
        examples = f'{numb_1} {numb_2}'
        print('Question: ' + examples)
        player_answer = int(input('Your answer: '))
        if player_answer == math.gcd(numb_1, numb_2):
            print('Correct!')
        elif player_answer != math.gcd(numb_1, numb_2):
            print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{math.gcd(numb_1, numb_2)}'\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    gcd()


if __name__ == "__main__":
    main()

