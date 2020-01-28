import sqlite3
conn = sqlite3.connect('Rideshare.db')
c = conn.cursor()

c.execute("INSERT INTO users(username,password) VALUES(nihal,shdfiushgfiuysgfy)")

conn.commit()
conn.close()