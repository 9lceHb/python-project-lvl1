import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    return name


def start_game(name):
    number = randint(1, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {number}')
    answer = prompt.string('Your answer:')
    if answer == correct_answer:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\
                \nLet's try again, {name}!")
    return answer == correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    result = start_game(name)
    while i < 3 and result is True:
        result = start_game(name)
        i += 1
    if i == 3 and result is True:
        print(f'Congratulations, {name}!')
