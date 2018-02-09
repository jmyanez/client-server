import socket
import sys
import time


port = 50000
sDgram = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sTream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server_address = (host,port)
sTream.bind(server_address)
sTream.listen(1)

print("Server is listening... ")
try:
    conn, addr = sTream.accept()
    print("Found connection from " , addr)
    while True:
        data = conn.recv(16)
        print('Server recieved %s' % data)
        if data:
            print("Sending data back to client....")
            time.sleep(5)
            conn.sendall(data)
        else:
            print("No more data ")
            break

finally:
    conn.close()

"""
#s.listen(5)
#
print(' starting up on %s port %s' % server_address)
s.bind(server_address)

while True:
    print("\nwaiting for message...")
    data,server_address = s.recvfrom(1080)
    print ('received %s bytes from %s' % (len(data), server_address))
    print (data)

    if data:

        sent = s.sendto(data,server_address)
        print("sent %s bytes back to %s" % (len(data),server_address))
"""