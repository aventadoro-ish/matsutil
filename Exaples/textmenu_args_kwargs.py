""" An example of using functions with arguments in text menu"""
from TextMenu.menu import TextMenu


def arg_cmd(*args):
    print('args:', args)


def kwarg_cmd(**kwargs):
    print('kwargs:', kwargs)


def comb_cmd(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


def none_cmd():
    print('function without any arguments')


menu = TextMenu('Argument Text Menu: ')
menu.add_option('arg', arg_cmd)
menu.add_option('kwarg', kwarg_cmd)
menu.add_option('comb', comb_cmd)
menu.add_option('none', none_cmd)

menu.run()
