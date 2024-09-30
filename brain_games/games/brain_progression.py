import random


GAME_QUESTION = 'What number is missing in the progression?'


def get_game_data():
        length_progression = random.randint(5, 10)
        start = random.randint(0, 10)
        step = random.randint(1, 5)
        progression = [start + step * i for i in range(length_progression)]
        hidden_index = random.randint(0, length_progression - 1)
        answer = progression[hidden_index]
        progression[hidden_index] = '..'
        question = ' '.join(map(str, progression))
        return question, str(answer)


# def main():
#     print('Welcome to the Brain Games!')
#     arithmetic_progression()
#
#
# if __name__ == "__main__":
#     main()
