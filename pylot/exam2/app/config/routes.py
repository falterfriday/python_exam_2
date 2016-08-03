"""
    Routes File
"""
from system.core.router import routes


routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Users#add_user'
routes['POST']['/login'] = 'Users#login_user'
routes['/clear'] = 'Users#clear'
routes['/travels'] = 'Travels#index'
routes['/travels/add'] = 'Travels#new_trip_page'
routes['POST']['/add_trip'] = 'Travels#add_trip'
routes['/travels/destination/<trip_id>'] = 'Travels#destination'
routes['/join/<trip_id>'] = 'Travels#join'
