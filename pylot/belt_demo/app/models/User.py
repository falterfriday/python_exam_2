""" 
    Sample Model File
"""
from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    
    def add_user_to_db(self, request):
        name = request.form['name']
        alias = request.form['alias']
        email = request.form['email']
        password = request.form['password']
        password_conf = request.form['password_conf']
        birthday = request.form['birthday']
        data = {
        'name': name,
        'alias':alias,
        'email':email,
        'password':password,
        'birthday':birthday
        }
        query = "INSERT INTO users (name, alias, email, password, birthday, created_at, updated_at) VALUES (:name, :alias, :email, :password, :birthday, NOW(), NOW())"
        self.db.query_db(query, data)

    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = :email"
        data = {
        'email':email
        }
        return self.db.query_db(query, data)

