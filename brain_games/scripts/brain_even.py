import random

print('May I have your name? ', end='')
name = input("Enter your name: ")
print(f"Hello, {name}!")

def conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def task():
    for i in range(3):
        loose_1 = f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!"
        loose_2 = f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"
        question = random.randint(1, 100)
        numb =int(f"{question}")
        print("Question: " + f"{numb}")
        player_answer = input(str('Your answer: '))
        if (numb % 2)== 0 and player_answer == 'yes' or (numb % 2) != 0  and player_answer == 'no':
           print("Correct!")
        elif (numb % 2) == 0 and player_answer == 'no':
            print(loose_1)
            return
        elif (numb % 2) != 0 and player_answer == 'yes':
            print(loose_2)
            return
    print(f"Congratulations, {name}!")
    return

# conditions()
# print(task())


if __name__ == "__main__":
    conditions()


if __name__ == "__main__":
    task()






