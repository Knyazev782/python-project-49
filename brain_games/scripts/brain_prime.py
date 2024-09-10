import random
import math

print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(numb):
    if numb <= 1:
        return False
    for i in range(2, int(math.sqrt(numb)) + 1):
        if numb % i == 0:
            return False
    return True

def prime_game():
    for i in range(3):
        numb = random.randint(1, 10)
        correct_answer = "yes" if is_prime(numb) else "no"
        print(f"Question: {numb}")
        player_answer = str(input("Your answer: "))
        if player_answer == correct_answer:
            print("Correct!")
        else:
            print(f'"{player_answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
            return
    print('Congratulations!')
prime_game()













