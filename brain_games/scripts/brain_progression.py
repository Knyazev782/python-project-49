import random


print('May I have your name? ', end='')
name = input("Enter your name: ")
print(f"Hello, {name}!")


print('What number is missing in the progression?')


def arithmetic_progression():
    for i in range(3):
        length_progression = random.randint(5,10)
        start = random.randint(0,10)
        step = random.randint(1,5)
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
            print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{hidden_value}'\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')




arithmetic_progression()




