"""
    Routes Configuration File
"""
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Users#add_user'
routes['POST']['/login'] = 'Users#login_user'
routes['POST']['/quotes'] = 'Quotes#index'