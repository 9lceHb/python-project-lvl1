#!/usr/bin/env python
from brain_games.scripts.games import welcome_user
from brain_games.scripts.games import check_answ
from brain_games.scripts.games import common_divisor
from random import randint


def make_ques_answ_dict(n):
    ques_answ_dict = {}
    for i in range(n):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        ques = f'{num1} {num2}'
        correct_answer = str(common_divisor(num1, num2))
        ques_answ_dict[i] = [ques, correct_answer]
    return ques_answ_dict


def main():
    game_count = 3
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    check_answ(make_ques_answ_dict(game_count), name)


if __name__ == "__main__":
    main()
