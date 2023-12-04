import threading # two things happening at once
import sqlite3 as sql
import hashlib
import socket # used to establish the connection between client and server
import re



conn = sql.connect("test_database.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User (
               username TEXT PRIMARY KEY,
               password TEXT)''')

cursor.execute("INSERT INTO User (username, password) VALUES ('Karthik', 'Karthik23')")
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


# - - - - - - -  - - - - - - - - - - - - - --------------------------------------------------------------------------------------------------
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()


server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()


def start_connection(c): # taking client as parameter
    #Check if Name is entered correctly
    credentials = []
    correct_credentials = False
    while not correct_credentials:
        msg = "Please enter your name:\n"
        c.send(msg.encode())
        response = c.recv(1024).decode() 
        pattern = re.compile(r'^[a-zA-Z]{3,26}$')

        cursor.execute("SELECT password FROM User WHERE user = ? ", (response,))
        result = cursor.fetchone()

        if result:
            msg =  "Username already exist"
            c.send(msg.encode())
        else:
            #pattern.match(string= str(response)):
            credentials[0] = str(response)
            Name = credentials[0]
            correct_credentials = True


    #Check if password is properly formatted
    correct_credentials = False
    while not correct_credentials:

        msg = "Please enter your Password:\n"
        c.send(msg.encode())
        response = c.recv(1024).decode() 
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$')

        if(pattern.match(str(response))):
            credentials[1] = str(response)
            password = credentials[1]          
        
            #Does not exist in the DB yet, so w e can insert it. Also commiting the changes after and closing the DB 
            cursor.execute("INSERT INTO User (username, password) VALUES (?, ?)", (Name, password))
            conn.commit()
            conn.close()
            correct_credentials = True

        else:
            msg = "Please enter the password correctly"
            c.send(msg.encode())

while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()
    # Close the server socket
    ss.close()
    exit()

