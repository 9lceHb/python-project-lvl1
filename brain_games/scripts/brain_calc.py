#!/usr/bin/env python
from brain_games.scripts.games import welcome_user
from brain_games.scripts.games import check_answ
from brain_games.scripts.games import make_oper
from random import randint


def make_ques_answ_dict(n):
    ques_answ_dict = {}
    for i in range(n):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        oper = make_oper()
        ques = f'{num1} {oper} {num2}'
        if oper == '*':
            correct_answer = str(num1 * num2)
        elif oper == '+':
            correct_answer = str(num1 + num2)
        else:
            correct_answer = str(num1 - num2)
        ques_answ_dict[i] = [ques, correct_answer]
    return ques_answ_dict


def main():
    game_count = 3
    name = welcome_user()
    print('What is the result of the expression?')
    check_answ(make_ques_answ_dict(game_count), name)


if __name__ == '__main__':
    main()
