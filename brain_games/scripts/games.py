#!/usr/bin/env python
import prompt
from random import randint


def common_divisor(a, b):
    if a >= b:
        divend = a
        divr = b
    else:
        divend = b
        divr = a
    rest = divend % divr
    while rest != 0:
        divend = divr
        divr = rest
        rest = divend % divr
    nod = divr
    return nod


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def make_oper():
    n = randint(1, 3)
    if n == 1:
        return '*'
    elif n == 2:
        return '+'
    else:
        return '-'


def is_prime(x):
    d = 2
    while x % d != 0 and d * d <= x:
        d += 1
    return x % d != 0


def check_answ(ques_answ_dict, name):
    i = 0
    print(f'Question: {ques_answ_dict[i][0]}')
    user_answer = prompt.string('Your answer:')
    if user_answer == ques_answ_dict[i][1]:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was\
 '{ques_answ_dict[i][1]}'.\nLet's try again, {name}!")
    while user_answer == ques_answ_dict[i][1] and i < len(ques_answ_dict) - 1:
        i += 1
        print(f'Question: {ques_answ_dict[i][0]}')
        user_answer = prompt.string('Your answer:')
        if user_answer == ques_answ_dict[i][1]:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was\
 '{ques_answ_dict[i][1]}'.\nLet's try again, {name}!")
    if i == len(ques_answ_dict) - 1:
        print(f'Congratulations, {name}!')
