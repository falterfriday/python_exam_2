"""
MODEL File
"""
from system.core.model import Model
import re
import bcrypt

class Quote(Model):
	def __init__(self):
		super(Quote, self).__init__()

	def get_all_quotes(self):
		query = "SELECT *, quotes.id AS quote_id FROM quotes JOIN users ON users.id = quotes.added_by"
		return self.db.query_db(query)

	def get_all_favorites(self, user_id):
		query = "SELECT * FROM user_favorite_quote JOIN quotes ON quotes.id = user_favorite_quote.quote_id JOIN users ON quotes.added_by = users.id WHERE user_id = :user_id"
		data = {'user_id':user_id}
		return self.db.query_db(query, data)

	def remove_from_favorites_by_id(self, quote_id):
		query = "DELETE FROM user_favorite_quote WHERE user_id = :user_id AND quote_id = :quote_id"
		data = { 'quote_id': quote_id['quote_id'], 'user_id': quote_id['user_id'] }
		self.db.query_db(query, data)

	def add_quote_to_db(self, info):
		NAME_REGEX = re.compile(r'^[a-zA-Z ]*$')
		errors = []
		if not info['author']:			
			errors.append("Author's name required")
		elif len(info['author']) < 2:
			errors.append("Author name too short")
		if not NAME_REGEX.match(info['author']):
			errors.append('Invalid name')
		if not info['quote']:			
			errors.append("Quote required")
		elif len(info['quote']) < 2:
			errors.append("Quote too short")
		if errors:
			return {"status": False, "errors": errors}
		else:
			query = "INSERT INTO quotes (author, quote, added_by, created_at, updated_at) VALUES (:author, :quote, :added_by, NOW(), NOW() )"
			data = {'author': info['author'], 'quote': info['quote'], 'added_by': info['added_by']}
			self.db.query_db(query, data)
			return { "status": True}

	def get_user_by_id(self, user_id):
		query = "SELECT * FROM quotes JOIN users ON users.id = quotes.added_by WHERE users.id = :user_id"
		data = {'user_id': user_id}
		return self.db.query_db(query, data)

	def get_quote_count(self, user_id):
		query = "SELECT *, count(*) FROM quotes JOIN users ON users.id = quotes.added_by WHERE users.id = :user_id"
		data = {'user_id': user_id}
		return self.db.query_db(query, data)

	def add_to_favorites(self, info):
		query = "INSERT INTO user_favorite_quote (user_id, quote_id) VALUES (:user_id, :quote_id) ON DUPLICATE KEY UPDATE quote_id = quote_id"
		data = {
		'user_id': info['user_id'],
		'quote_id':info['quote_id']
		}

		return self.db.query_db(query, data)


