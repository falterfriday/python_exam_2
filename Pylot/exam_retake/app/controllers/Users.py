"""
CONTROLLER File
"""
from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)

		self.load_model('User')
		self.load_model('Quote')
		self.db = self._app.db

	def index(self):
		print session
		return self.load_view('index.html')

	def add_user(self):
		info = {
			'name':request.form['name'],
			'alias':request.form['alias'],
			'email':request.form['email'],
			'password':request.form['password'],
			'pw_confirmation':request.form['pw_confirmation'],
			'dob':request.form['dob']
		}
		create_status = self.models['User'].add_user_to_db(info)
		if create_status['status'] == True:
			session['id'] = create_status['user']['id']
			session['alias'] = create_status['user']['alias']
			return redirect('/quotes')
		else:
			for message in create_status['errors']:
				flash( message, 'regis_errors')
			return redirect('/')

	def login_user(self):
		info = {
		'email':request.form['email'],
		'password':request.form['password']
		}
		login_status = self.models['User'].login_user(info)

		if login_status['status'] == True:
			session['alias'] = login_status['user']['alias']
			session['id'] = login_status['user']['id']
			print "%"*100
			print session
			print "%"*100
			return redirect('/quotes')
		

		else:
			for message in login_status['errors']:
				flash( message, 'login_errors')
			return redirect('/')

	def clear(self):
		session.clear()
		return redirect('/')

