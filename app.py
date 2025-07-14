
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from ldap3 import Server, Connection, ALL, NTLM
import os
import sqlite3

# App config
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User store is now in users.db

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes
@app.route('/')
@login_required
def index():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form['identifier']
        password = request.form['password']
        auth_method = request.form['auth_method']

        if auth_method == 'email':
            conn = sqlite3.connect('C:/2025_Gemini_Cli/flask_ldap_login_app/users.db')
            c = conn.cursor()
            c.execute("SELECT password FROM users WHERE email = ?", (identifier,))
            user_record = c.fetchone()
            conn.close()
            
            if user_record and user_record[0] == password:
                user_obj = User(id=identifier)
                login_user(user_obj)
                return redirect(url_for('index'))
            else:
                flash('Invalid credentials')
        
        elif auth_method == 'ldap':
            try:
                server = Server('your_ldap_server.com', get_info=ALL)
                conn = Connection(server, user=identifier, password=password, auto_bind=True)
                if conn.bound:
                    user_obj = User(id=identifier)
                    login_user(user_obj)
                    return redirect(url_for('index'))
                else:
                    flash('Invalid credentials')
            except Exception as e:
                flash(f'LDAP Authentication Error: {e}')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5008)
