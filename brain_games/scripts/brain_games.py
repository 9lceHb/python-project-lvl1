#!/usr/bin/env python
import brain_games.cli as cli



def main():
    print('Welcome to the Brain Games!')
    name =cli.welcome_user()
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
