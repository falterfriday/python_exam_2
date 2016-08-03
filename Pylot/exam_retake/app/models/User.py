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
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
		NAME_REGEX = re.compile(r'^[a-zA-Z ]*$')
		ALIAS_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]*$')
		errors = []
		if not info['name']:			
			errors.append('Name required')
		elif len(info['name']) < 2:
			errors.append('Name too short')
		elif not NAME_REGEX.match(info['name']):
			errors.append('Invalid name!')
		if not info['alias']:
			errors.append('Alias required')
		elif len(info['alias']) < 2:
			errors.append('Alias too short')
		elif not ALIAS_REGEX.match(info['alias']):
			errors.append('Invalid alias!')
		if not info['email']:
			errors.append('Email required')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append('Invalid email!')
		if not info['password']:
			errors.append('Password required')
		elif len(info['password']) < 8:
			errors.append('Password too short')
		elif info['password'] != info['pw_confirmation']:
			errors.append('Passwords must match!')
		if not info['dob']:
			errors.append('Date of Birth required')
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			hashed_pw = self.bcrypt.generate_password_hash(password)
			create_query = "INSERT INTO users (name, alias, email, pw_hash, created_at, updated_at) VALUES (:name, :alias, :email, :pw_hash, NOW(), NOW() )"
			create_data = {'name': info['name'], 'alias': info['alias'], 'email': info['email'], 'pw_hash': hashed_pw}
			self.db.query_db(create_query,create_data)
			get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
			users = self.db.query_db(get_user_query)
			return { "status": True, "user": users[0] }

	def login_user(self, info):
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
		errors = []
		if not info['email']:
			errors.append('Email required')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append('Invalid email!')
		if not info['password']:
			errors.append('Password required')
		elif len(info['password']) < 8:
			errors.append('Password required')
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
			user_data = {'email': info['email']}
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

		
