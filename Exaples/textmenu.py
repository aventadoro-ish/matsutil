import TextMenu


def echo_cmd(echo: str):
	print(echo)


def open_idn_menu(prompt: str):
	idn_menu = TextMenu.TextMenu('\tIndented Menu:', {'echo': echo_cmd}, tabs=1)
	return idn_menu.run()


text = TextMenu.TextMenu('Core Menu: ',
						 {'echo': echo_cmd, 'indent': open_idn_menu, 'i': open_idn_menu},
						 {echo_cmd: 'echos back the line you give it', open_idn_menu: 'opens new indented menu'})

text.run()
