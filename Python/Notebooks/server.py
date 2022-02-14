import socket
import sys
from _thread import *

host = ''
port  = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))   

s.listen(5)

def threaded_client(conn):
    conn.send(str.encode('Welcome, type your info\n'))
    while True:
        data = conn.recv(2048)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()
print('Waiting for a connection')
while True:
    conn, addr = s.accept()
    print('connected to: ' + addr[0] + ':' + str(addr[1]))
    conn.send(str.encode('Hello\n'))
    data = conn.recv(2048)
    print(data.decode('utf-8'))
    reply = 'Server output: ' + data.decode('utf-8')
    conn.sendall(str.encode(reply))
    thread = threading.Thread(target=threaded_client, args=(conn,))
    thread.start()