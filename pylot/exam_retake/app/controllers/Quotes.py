"""
CONTROLLER File
"""
from system.core.controller import *

class Quotes(Controller):
	def __init__(self, action):
		super(Quotes, self).__init__(action)

		self.load_model('Quote')
		self.load_model('User')
		self.db = self._app.db




	def quotes(self):
		user_id = session['id']
		quotes = self.models['Quote'].get_all_quotes()
		favorites = self.models['Quote'].get_all_favorites(user_id)
		alias = session['alias']
		return self.load_view('quotes.html', alias=alias, quotes=quotes, favorites=favorites)

	def add_quote(self):
		info = {
		'author':request.form['author'],
		'quote':request.form['quote'],
		'added_by':session['id']
		}
		quote_status = self.models['Quote'].add_quote_to_db(info)
		if quote_status['status'] == True:
			return redirect('/quotes')
		else:
			for message in quote_status['errors']:
				flash( message, 'quote_errors')
			return redirect('/quotes')

	def user(self, user_id):
		info = {
		'user_id': user_id
		}
		user = self.models['Quote'].get_user_by_id(user_id)
		count = self.models['Quote'].get_quote_count(user_id)
		return self.load_view('user.html', user=user, count=count)


	def add_to_favorites(self, quote_id):
		info = {
		'quote_id':quote_id,
		'user_id':session['id']
		}

		favorites = self.models['Quote'].add_to_favorites(info)
		return redirect('/quotes')

	def remove_from_favorites_by_id(self, quote_id):
		user_id = session['id']
		info = {
		'quote_id': quote_id,
		'user_id': user_id
		}
		self.models['Quote'].remove_from_favorites_by_id(info)
		return redirect('/quotes')

