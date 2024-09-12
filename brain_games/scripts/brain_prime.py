import random
import math
from brain_games.scripts.cli import welcome_user


def is_prime(numb):
    if numb <= 1:
        return False
    for i in range(2, int(math.sqrt(numb)) + 1):
        if numb % i == 0:
            return False
    return True


def prime_game():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        numb = random.randint(1, 10)
        correct_answer = "yes" if is_prime(numb) else "no"
        print(f"Question: {numb}")
        player_answer = str(input("Your answer: "))
        if player_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

def main():
    print('Welcome to the Brain Games!')
    prime_game()

if __name__ == "__main__":
    main()













