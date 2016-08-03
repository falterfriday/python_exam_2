"""
MODEL File
"""
from system.core.model import Model

class Post(Model):
	def __init__(self):
		super(Post, self).__init__()

	def all(self):
		query = "SELECT * FROM posts"
		return self.db.query_db(query)


	def create(self, info):
		query = "INSERT INTO posts (post) VALUES (:post)"
		data = {
		'post':info['post']
		}
		self.db.query_db(query, data)
		posts_query = "SELECT * FROM posts"
		return self.db.query_db(posts_query)
