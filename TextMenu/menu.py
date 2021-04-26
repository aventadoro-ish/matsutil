class TextMenu:
	"""Class implementation of multi-layer'able console text menu"""

	_EXIT_MENU_: str = 'exit_core_menu'

	def help_cmd(self):
		"""This method lists all possible menu calls and comments for them if available"""
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
			self._print_(line)

	def exit_cmd(self):
		"""This method is called to exit menu stack.
		Passes _EXIT_MENU_ string to next handler"""
		self.finished = True
		return 'exit_core_menu'

	def close_cmd(self):
		"""Closes this menu instance and backs up"""
		self.finished = True

	def _add_common_calls_(self, implemented_calls):
		"""Internal utility method that adds unimplemented menu calls"""
		if not ('help' in implemented_calls):
			implemented_calls['help'] = self.help_cmd
		if not ('h' in implemented_calls):
			implemented_calls['h'] = self.help_cmd

		if not ('close' in implemented_calls):
			implemented_calls['close'] = self.close_cmd
		if not ('c' in implemented_calls):
			implemented_calls['c'] = self.close_cmd

		if not ('exit' in implemented_calls):
			implemented_calls['exit'] = self.exit_cmd
		if not ('e' in implemented_calls):
			implemented_calls['e'] = self.exit_cmd

	def __init__(self, prompt: str = None, options: dict = None, comment_options: dict = None,
				add_common_calls: bool = True, tabs: int = 0):
		"""Initializes menu class
		If used as indented menu should be called return menu.run()

		:param prompt: str
			Menu name
		:param options: dict
			Specifies all menu call options.
			Should be formatted like {'option1': option1_cmd, 'option2': option2_cmd, 'opt1': option1_cmd}
			Short and long calls are specified twice
		:param comment_options: dict
			Hints for users that are displayed in 'help'
			e.g. {option1_cmd: 'this does that', option2_cmd: 'this does different'}
		:param add_common_calls: bool
			Do you want to specify common menu calls like 'help', 'exit' etc
		:param tabs: int
			Number of tabs before any print

		"""
		# finished is used for internal menu loop
		self.finished: bool = False
		self.tabs = tabs

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
		"""Set menu title
		:param prompt: str
			Title

		"""
		self.prompt = prompt

	def add_comment(self, comment: set):
		"""Add comment hint for 'help' option

		:param comment:
			(option1_cmd, 'this does that')
		:return: None
		"""
		self.comment_options[comment[0]] = comment[1]

	def add_comments(self, comments: dict):
		"""Add multiple comments
		:param comments: dict
			Add hints for users that are displayed in 'help'
			e.g. {option1_cmd: 'this does that', option2_cmd: 'this does different'}
		"""
		for key, val in comments.items():
			self.comment_options[key] = val

	def add_option(self, option: set):
		"""Add one menu option
		:param option: set
			Option to add, e.g. ('option': option_cmd)
		"""
		self.options[option[0]] = option[1]

	def add_options(self, options: dict):
		"""Add multiple menu options

		:param options: dict
			Dictionary of options to add
			Formatted like {'option1': option1_cmd, 'option2': option2_cmd, 'opt1': option1_cmd}
			short option names are separate entries with the same value (linked method)
		"""
		for key, val in options.items():
			self.options[key] = val

	def _print_(self, line):
		"""Prints line with tabulation"""
		print('\t'*self.tabs + line)

	def _handle_input_(self, choice, params):
		"""Internal utility method that handles user choice and params (if given)"""
		handled = None
		try:
			handled = self.options[choice](params)
		except TypeError:
			handled = self.options[choice]()
		except KeyError as e:
			handled = False

		return handled

	def run(self):
		"""Launches menu
		If used as indented menu should be called return menu.run()
		"""
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
				self._print_('Unknown command. Type "help" for list of commands')