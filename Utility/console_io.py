from typing import List


def binary_input(prompt: str = '') -> bool:
    while True:
        inp = input(prompt + ' (y/n)')
        if inp in ['y', 'Y', 'yes', 'Yes']:
            return True
        elif inp in ['n', 'N', 'no', 'No']:
            return False
        elif inp in ['c', 'C', 'close', 'Close']:
            return None
        else:
            print('error: type "y", "n", or "c"')


def numeric_input(prompt: str = '') -> int:
    while True:
        inp = input(prompt + ' (number)')
        if inp.isdecimal():
            return int(inp)
        elif inp in ['c', 'C', 'close', 'Close']:
            return None
        else:
            print('error: type number, or "c"')


def choice_input(list_to_choose: List[str], prompt: str = '') -> str:
    while True:
        inp = input(prompt + ' (choice from: ' + str(list_to_choose) + ')')
        if inp in list_to_choose:
            for index, i in enumerate(list_to_choose):
                if inp == i: return inp

        elif inp in ['\c', '\C', '\close', '\Close']:
            return None
        else:
            print('error: choose form list, or tye "\c"')