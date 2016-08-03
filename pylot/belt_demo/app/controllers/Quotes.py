"""
Controller File
"""
from system.core.controller import *

class Quotes(Controller):
	def __init__(self, action):
		super(Quotes, self).__init__(action)

		self.load_model('User')
		self.db = self._app.db

	def index(self):
		return self.load_view('quotes.html')