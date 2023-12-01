import sqlite3 as sql

conn = sql.connect("test_database.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User (
               username TEXT PRIMARY KEY,
               password TEXT)''')

# cursor.execute("INSERT INTO User (username, password) VALUES ('Karthik', 'Karthik23')")
# cursor.execute("INSERT INTO User (username, password) VALUES ('Ade', 'Ade24')")
# cursor.execute("INSERT INTO User (username, password) VALUES ('Ella', 'Ella36')")
# cursor.execute("INSERT INTO User (username, password) VALUES ('Sanjana', 'Sanjana00')")
# cursor.execute("INSERT INTO User (username, password) VALUES ('HrithikRoshan', 'Greatest')")
# cursor.execute("INSERT INTO User (username, password) VALUES ('Hemsworth', 'Handsome')")
# cursor.execute("INSERT INTO User (username, password) VALUES ('Lebron', 'Goated')")

cursor.execute("SELECT * FROM User")
rows = cursor.fetchall()
print(rows)

conn.commit()
conn.close()