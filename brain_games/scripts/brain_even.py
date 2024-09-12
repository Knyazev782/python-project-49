import random
from brain_games.scripts.cli import welcome_user


def task():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        loose_1 = (f"'no' is wrong answer ;(. "
                   f"Correct answer was 'yes'.\nLet's try again, {name}!")
        loose_2 = (f"'yes' is wrong answer ;(. "
                   f"Correct answer was 'no'.\nLet's try again, {name}!")
        question = random.randint(1, 100)
        numb = int(f"{question}")
        print("Question: " + f"{numb}")
        player_answer = input(str('Your answer: '))
        if ((numb % 2) == 0 and player_answer == 'yes' or
        (numb % 2) != 0 and player_answer == 'no'):
            print("Correct!")
        elif (numb % 2) == 0 and player_answer == 'no':
            print(loose_1)
            return
        elif (numb % 2) != 0 and player_answer == 'yes':
            print(loose_2)
            return
    print(f"Congratulations, {name}!")
    return


def main():
    print('Welcome to the Brain Games!')
    task()
