"""
MODEL File
"""
from system.core.model import Model
import re
import bcrypt

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def add_user_to_db(self, info):
		NAME_REGEX = re.compile(r'^[a-zA-Z ]*$')
		USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]*$')
		errors = []
		if not info['name']:			
			errors.append('Name required')
		elif len(info['name']) < 3:
			errors.append('Name too short')
		elif not NAME_REGEX.match(info['name']):
			errors.append('Invalid name!')
		if not info['username']:
			errors.append('Username required')
		elif len(info['username']) < 3:
			errors.append('username too short')
		elif not USERNAME_REGEX.match(info['username']):
			errors.append('Invalid username!')
		if not info['password']:
			errors.append('Password required')
		elif len(info['password']) < 8:
			errors.append('Password too short')
		elif info['password'] != info['pw_confirmation']:
			errors.append('Passwords must match!')
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			hashed_pw = self.bcrypt.generate_password_hash(password)
			create_query = "INSERT INTO users (name, username, pw_hash, created_at, updated_at) VALUES (:name, :username, :pw_hash, NOW(), NOW() )"
			create_data = {'name': info['name'], 'username': info['username'], 'pw_hash': hashed_pw}
			self.db.query_db(create_query,create_data)
			get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
			users = self.db.query_db(get_user_query)
			return { "status": True, "user": users[0] }


	def login_user(self, info):
		errors = []
		USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]*$')
		if not info['username']:
			errors.append('Username required')
		elif not USERNAME_REGEX.match(info['username']):
			errors.append('Invalid username!')
		if not info['password']:
			errors.append('Password required')
		elif len(info['password']) < 8:
			errors.append('Password required')
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			user_query = "SELECT * FROM users WHERE username = :username LIMIT 1"
			user_data = {'username': info['username']}
			user = self.db.query_db(user_query, user_data)
			if user:
				print user[0]['pw_hash']
				if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
					return {"status": True, "user": user[0]}
				else:
					errors.append('Invalid login credentials!')
			else:
				errors.append('Invalid login credentials!')
			return {"status": False, "errors": errors}

