import prompt
from random import randint


def welcome_user(game_type):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    if game_type == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_type == 'calc':
        print('What is the result of the expression?')
    return name


def make_oper():
    n = randint(1, 3)
    if n == 1:
        return '*'
    elif n == 2:
        return '+'
    else:
        return '-'


def make_ques_answ(game_type):
    if game_type == 'even':
        number = randint(1, 100)
        ques = number
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
    elif game_type == 'calc':
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
    return ques, correct_answer


def start_game(game_type, name):
    result = make_ques_answ(game_type)
    print(f'Question: {result[0]}')
    answer = prompt.string('Your answer:')
    if answer == result[1]:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result[1]}'.\
                \nLet's try again, {name}!")
    return answer == result[1]


def game_count(n, game_type):
    name = welcome_user(game_type)
    i = 1
    is_answer_correc = start_game(game_type, name)
    while i < n and is_answer_correc is True:
        is_answer_correc = start_game(game_type, name)
        i += 1
    if i == n and is_answer_correc is True:
        print(f'Congratulations, {name}!')
