import sqlite3
conn = sqlite3.connect('Rideshare.db')
c = conn.cursor()

#c.execute("INSERT INTO users(username,password) VALUES(nihal,shdfiushgfiuysgfy)")
c. execute("SELECT * from users")
rows = c.fetchall()
print(rows)
conn.commit()
conn.close()