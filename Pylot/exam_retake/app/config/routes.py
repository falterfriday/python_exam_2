"""
    Routes Configuration File
"""

from system.core.router import routes


routes['default_controller'] = 'Users'
routes['POST']['/register'] = 'Users#add_user'
routes['POST']['/login'] = 'Users#login_user'
routes['/clear'] = 'Users#clear'
routes['/quotes'] = 'Quotes#quotes'
routes['POST']['/add_quote'] = 'Quotes#add_quote'
routes['/users/<user_id>'] = 'Quotes#user'
routes['POST']['/add_to_favorites/<quote_id>'] = 'Quotes#add_to_favorites'
routes['POST']['/remove/<quote_id>'] = 'Quotes#remove_from_favorites_by_id'