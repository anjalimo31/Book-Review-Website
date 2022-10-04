#populating the database

import sqlite3
db_locale = 'users.db'

connie = sqlite3.connect(db_locale)
c=connie.cursor() #use this to create commands

#command
c.execute("""

INSERT INTO comments (title,name,comment) VALUES
('Realm Breaker', 'John Doe', 'It was an AMAZING book! I loved all the characters. They were all uniquely different, each with their own struggles. I especially enjoyed the characters Taristan and Erida. They were fascinating! I am curious to see where this book goes from here!'),
('Six of Crows', 'Suzy Rogers', 'I tried reading this three times and I am pleased to report that on the third try, I latched on! I adored reading this book. THE CHARACTERS!!! KAZ! I love love LOVE a good heist book, and this was absolutely PERFECT!!')
""")

#commit the changes
connie.commit()
connie.close()
