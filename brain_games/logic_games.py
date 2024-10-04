import prompt


ROUNDS_TO_WIN = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}"'!')
    return name


def launch_game(game):
    username = welcome_user()
    round_counter = 0
    print(game.GAME_QUESTION)
    while round_counter < ROUNDS_TO_WIN:
        question, answer = game.get_game_data()
        print(f"Question: {question}")
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            round_counter += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{answer}".')
            print(f'Let\'s try again, {username}!')
            return
    print(f'Congratulations, {username}!')
