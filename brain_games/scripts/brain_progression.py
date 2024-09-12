import random
from brain_games.scripts.cli import welcome_user


def arithmetic_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    for i in range(3):
        length_progression = random.randint(5, 10)
        start = random.randint(0, 10)
        step = random.randint(1, 5)
        progression = [start + step * i for i in range(length_progression)]
        hidden_index = random.randint(0, length_progression - 1)
        hidden_value = progression[hidden_index]
        progression[hidden_index] = '..'
        progression_str = ' '.join(map(str, progression))
        print('Question: ' + progression_str)
        player_answer = int(input('Your answer: '))
        if player_answer == hidden_value:
            print('Correct!')
        else:
            print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{hidden_value}'\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    print('Welcome to the Brain Games!')
    arithmetic_progression()


if __name__ == "__main__":
    main()
