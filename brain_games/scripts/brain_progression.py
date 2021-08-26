#!/usr/bin/env python
from brain_games.scripts.games import welcome_user
from brain_games.scripts.games import check_answ
from random import randint


def make_ques_answ_dict(n):
    ques_answ_dict = {}
    for i in range(n):
        progr_start = randint(1, 100)
        progr_multip = randint(1, 10)
        progr_miss = randint(1, 10)
        progr_list = [progr_start]
        for k in range(1, 10):
            progr_list.append(progr_start + k * progr_multip)
        correct_answer = str(progr_list[progr_miss - 1])
        progr_list[progr_miss - 1] = '..'
        ques = str(progr_list).replace(", ", " ")
        ques = ques.replace("'", "")
        ques = ques.replace("[", "")
        ques = ques.replace("]", "")
        ques_answ_dict[i] = [ques, correct_answer]
    return ques_answ_dict


def main():
    game_count = 3
    name = welcome_user()
    print('What number is missing in the progression?')
    check_answ(make_ques_answ_dict(game_count), name)


if __name__ == '__main__':
    main()
