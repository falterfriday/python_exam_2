"""
Sample Controller File
"""
from system.core.controller import *

class Posts(Controller):
	def __init__(self, action):
		super(Posts, self).__init__(action)

		self.load_model('Post')
		self.db = self._app.db

	def index(self):
		posts = self.models['Post'].all()
		return self.load_view('posts/index.html', posts=posts)

	def index_json(self):
		posts = self.models['Post'].all()
		return jsonify(posts=posts)

	def index_html(self):
		posts = self.models['Post'].all()
		return self.load_view('partials/posts.html', posts=posts)

	def create(self):
		info = {
		'post':request.form['post']
		}
		posts = self.models['Post'].create(info)
		return self.load_view('partials/posts.html', posts=posts)


		

