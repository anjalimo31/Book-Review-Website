#Use SQLite3 to create a database

import sqlite3
db_locale = 'users.db'

connie = sqlite3.connect(db_locale)
c=connie.cursor() #use this to create commands

#command
c.execute("""
CREATE TABLE comments
(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    title TEXT,
    comment TEXT
)
""")

#commit the changes
connie.commit()
connie.close()
