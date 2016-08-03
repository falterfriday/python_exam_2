"""
Controller File
"""
from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)

		self.load_model('User')
		self.db = self._app.db


	def index(self):
		print self.db.query_db("SELECT * FROM users")

		return self.load_view('index.html')

	def add_user(self):
		self.models['User'].add_user_to_db(request)
		flash('You are registered!')
		return redirect('/')

	def login_user(self):
		email = request.form['email']
		password = request.form['password']
		user = self.models['User'].get_user_by_email(email)
		if len(user) == 0:
			flash('email invalid')
			return redirect('/')
		elif user[0].password == password:
			session['current_user_id'] = user[0].id
			return redirect('/quotes')
		else:
			flash('invalid password')
			return redirect('/')