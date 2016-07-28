"""
MODEL File
"""
from system.core.model import Model
import re
import bcrypt

class Travel(Model):
	def __init__(self):
		super(Travel, self).__init__()

	def add_trip(self, info):
		errors = []
		if not info['destination']:
			errors.append('Destination required')
		if not info['description']:
			errors.append('Description required')		
		if not info['depart']:
			errors.append('From Date required')
		if not info['arrive']:
			errors.append('To Date required')
		if errors:
			return {"status": False, "errors": errors}
		else:
			query = "INSERT INTO trips (destination, description, depart, arrive, created_at, updated_at, user_id) VALUES (:destination, :description, :depart, :arrive, NOW(), NOW(), :user_id )"
			data = {
			'destination': info['destination'],
			'description': info['description'],
			'depart': info['depart'],
			'arrive': info['arrive'],
			'user_id': info['user_id']
			}
			print 'data'*80
			print data
			self.db.query_db(query, data)
			return { "status": True }


	def my_trips(self, info):
		query = "SELECT * FROM trips LEFT JOIN buddies ON buddies.trip_id = trips.id WHERE trips.user_id = :id  OR buddies.user_id = :id"
		data = {'id': info['id']}
		return self.db.query_db(query, data)

	def get_destination(self, info):
		query = "SELECT * FROM trips JOIN users ON users.id = trips.user_id WHERE trips.id = :id"
		data = {'id': info['trip_id']}
		return self.db.query_db(query, data)

	def other_trips(self, info):
		query = "SELECT *, trips.id AS trip_id FROM trips JOIN users ON users.id = trips.user_id WHERE user_id != :id"
		data = {'id': info['id']}
		return self.db.query_db(query, data)

	def join(self, info):
		query = "INSERT INTO buddies (user_id, trip_id, created_at, updated_at) VALUES (:user_id, :trip_id, NOW() ,NOW() )"
		data = {
		'user_id': info['user_id'],
		'trip_id': info['trip_id']
		}
		self.db.query_db(query, data)

	def get_buddies(self, info):
		query = "SELECT * FROM users JOIN buddies ON buddies.user_id = users.id WHERE trip_id = :trip_id"
		data = {
		'trip_id' :info['trip_id'],
		}
		return self.db.query_db(query, data)







