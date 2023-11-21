import threading # two things happening at once
import sqlite3
import hashlib
import socket # used to establish the connection between client and server

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
    msg = "Welcome to Blueprint squad!"
    c.send(msg.encode())
    """ reponse = "THANK YOU!"
                    "no." "im sleepy"
                    variable. --> we need something to pull the client's response.
    """

    response = c.recv(1024).decode() # 1024 bytes tells us the size / buffer of the content we are recieving so that the socket knows how much to expect
    print("[S]: Data received from client: " + response)    

    
    # DO IN GROUPS INDEPENDENTLY
    
    msg = "How are you?" # make own riddle / joke & respond with answer
    c.send(msg.encode())

    response = c.recv(1024).decode()
    print("[S]: Data received from client: " + response)    

    
    count = 0
    while(count < 5): # use loop to send 1, 2, 3, 4, 5 to client
        c.send(str(count).encode())
        response = c.recv(1024).decode()
        print("[S]: Data received from client: " + response)
        count+-1

    print("Done")


while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()

    # Close the server socket
    ss.close()
    exit()