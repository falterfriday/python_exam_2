"""
Sample Controller File

"""
from system.core.controller import *

class Travels(Controller):
	def __init__(self, action):
		super(Travels, self).__init__(action)

		self.load_model('User')
		self.load_model('Travel')
		self.db = self._app.db

	def index(self):
		print '%'*80
		print session
		print '%'*80
		name = session['name']
		info = {'id' :session['id']}
		trips = self.models['Travel'].my_trips(info)
		other_trips = self.models['Travel'].other_trips(info)
		print '%'*80
		print other_trips
		return self.load_view('travels.html', name=name, trips=trips, other_trips=other_trips)

	def new_trip_page(self):
		return self.load_view('add_trip.html')

	def add_trip(self):
		info = {
		'destination': request.form['destination'],
		'description': request.form['description'],
		'depart': request.form['depart'],
		'arrive': request.form['arrive'],
		'user_id': session['id']
		}
		print '%'*80
		print request.form
		create_status = self.models['Travel'].add_trip(info)
		if create_status['status'] == True:
			return redirect('/travels')
		else:
			for message in create_status['errors']:
				flash( message, 'travel_errors')
			return redirect('/travels/add')

	def destination(self, trip_id):
		info = {'trip_id':trip_id}
		info2 = {'trip_id':trip_id, 'user_id': session['id']}
		destinations = self.models['Travel'].get_destination(info)
		buddies = self.models['Travel'].get_buddies(info2)
		print "%"*80
		print buddies
		return self.load_view('destination.html', destinations=destinations, buddies=buddies)

	def join(self, trip_id):

		info = {
		'trip_id': trip_id,
		'user_id': session['id']
		}
		print "^"*80
		print info
		self.models['Travel'].join(info)
		return redirect('/travels')



