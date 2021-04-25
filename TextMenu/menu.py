class TextMenu:
	_EXIT_MENU_: str = 'exit_core_menu'

	def help_cmd(self):
		opts = self.options.items()
		funcs = []
		keys = []
		for opt in opts:
			try:
				idx = funcs.index(opt[1])

				keys[idx].append(opt[0])

			except ValueError:
				funcs.append(opt[1])
				keys.append([opt[0]])

		if self.comment_options is not None:
			comments = []
			for func in funcs:
				try:
					comments.append(self.comment_options.get(func))

				except KeyError:
					comments.append(' ')

		max_width = max([str(i).__len__() for i in keys])
		for idx, i in enumerate(keys):
			line = f'-{str(i)[1:-1].ljust(max_width, " ")}'
			if self.comment_options is not None and comments[idx] is not None:
				line += '(' + str(comments[idx]) + ')'
			else:
				pass
			print(line)

	def exit_cmd(self):
		self.finished = True
		return 'exit_core_menu'

	def close_cmd(self):
		self.finished = True

	def _add_common_calls_(self, implemented_calls):
		if not ('help' in implemented_calls):
			implemented_calls['help'] = self.help_cmd
		if not ('h' in implemented_calls):
			implemented_calls['h'] = self.help_cmd

		if not ('close' in implemented_calls):
			implemented_calls['close'] = self.close_cmd
		if not ('c' in implemented_calls):
			implemented_calls['c'] = self.close_cmd

		if not('exit' in implemented_calls):
			implemented_calls['exit'] = self.exit_cmd
		if not ('e' in implemented_calls):
			implemented_calls['e'] = self.exit_cmd

	def __init__(self, prompt: str = None, options: dict = None, comment_options=None, add_common_calls=True):
		# finished is used for internal menu loop
		self.finished: bool = False

		# heading of the menu
		try:
			self.prompt = prompt
		except AttributeError:
			self.prompt = ''

		# {'option1': option1_cmd, 'option2': option2_cmd, 'opt1': option1_cmd}
		# short option names are separate entries with the same value (linked method)
		try:
			self.options = options
		except AttributeError:
			pass

		# {option1_cmd: 'calls option 1 and does x', option2_cmd: 'calls opt 2 and does y'}
		# optional param used in help menu to comment menu options
		self.comment_options = comment_options

		# add calls for help, close and exit methods if needed
		if add_common_calls:
			self._add_common_calls_(options)

	def set_prompt(self, prompt: str):
		self.prompt = prompt

	def add_comment(self, comment: set):
		self.comment_options[comment[0]] = comment[1]

	def add_comments(self, comments: dict):
		for key, val in comments.items():
			self.comment_options[key] = val

	def add_option(self, option: set):
		self.options[option[0]] = option[1]

	def add_options(self, options: dict):
		for key, val in options.items():
			self.options[key] = val

	def _handle_input_(self, choice, params):
		handled = None
		try:
			handled = self.options[choice](params)
		except TypeError:
			handled = self.options[choice]()
		except KeyError as e:
			handled = False

		return handled

	def run(self):
		while not self.finished:
			inp = input(self.prompt).lower().split(' ', 1)
			choice = inp[0]
			try:
				params = inp[1]
			except IndexError:
				params = None

			handled = self._handle_input_(choice, params)

			if handled == self._EXIT_MENU_:
				return handled
			elif isinstance(handled, bool) and not handled:
				print('Unknown command. Type "help" for list of commands')
