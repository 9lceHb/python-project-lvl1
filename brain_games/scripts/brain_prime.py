#!/usr/bin/env python
from brain_games.scripts.games import welcome_user
from brain_games.scripts.games import check_answ
from random import randint
from brain_games.scripts.games import is_prime


def make_ques_answ_dict(n):
    ques_answ_dict = {}
    for i in range(n):
        ques = randint(1, 3600)
        if is_prime(ques) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        ques_answ_dict[i] = [ques, correct_answer]
    return ques_answ_dict


def main():
    game_count = 3
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    check_answ(make_ques_answ_dict(game_count), name)


if __name__ == '__main__':
    main()
