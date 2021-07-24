"""Basic TextMenu library usage example"""

from TextMenu import TextMenu


# p 'hi', param='hello' -> p({0:'hi', param:'hello'})
def param_cmd(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)


def echo_cmd(echo: str):
    print(echo)


def open_idn_menu(prompt: str):
    idn_menu = TextMenu('\tIndented Menu: ', {'echo': echo_cmd}, tabs=1, default_method=echo_cmd)
    return idn_menu.run()


text = TextMenu(prompt='Core Menu: ',
                options={'echo': echo_cmd, 'indent': open_idn_menu, 'i': open_idn_menu},
                comment_options={echo_cmd: 'echos back the line you give it\nhello',
                                 open_idn_menu: 'opens new indented menu\nhi'})
text.add_option('p', param_cmd)

text.run()
