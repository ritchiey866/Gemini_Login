

import sqlite3

conn = sqlite3.connect('C:/2025_Gemini_Cli/flask_ldap_login_app/users.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        email TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')

c.execute("INSERT INTO users (email, password) VALUES (?, ?)", ('admin@local.com', 'password'))

conn.commit()
conn.close()

