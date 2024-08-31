import random


def conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def task():
    for i in range(3):
        winner = "Congratulations, Name!"
        loose_1 = "'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, name!"
        loose_2 = "'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, name!"
        question = random.randint(1, 100)
        numb =int(f"{question}")
        print("Question: " + f"{numb}")
        player_answer = input(str('Your answer: '))
        if (numb % 2)== 0 and player_answer == 'yes' or (numb % 2) != 0  and player_answer == 'no':
           print("Correct!")
        elif (numb % 2) == 0 and player_answer == 'no':
            return loose_1
        elif (numb % 2) != 0 and player_answer == 'yes':
            return loose_2
    return winner

conditions()
print(task())







