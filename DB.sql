import sqlite3

/*Connect to SQLite */
conn = sqlite3.connect('mydatabase.db') 
cursor = conn.cursor()
