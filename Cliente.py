import socket
import sys
import time


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Socket using datagram
sTream = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket using TCP protocol

host = socket.gethostname()
port = 50000
server_address = (host,port)

sTream.connect(server_address)  #Connection to the host and port
#sTream.send(b"Hello There!!") #Send a first message signal
"""
with open('received_file','wb') as f:
    print ('file opened')
    while True:
        print("Getting data...")
        data = sTream.recv(16)
        print('data=%s' % (data))
        if not data:
            break
        f.write(data)
f.close()
print('Successfully got the file')
client_socket.close()
print("connection ended ")
"""


#Stream Transfer 
message = "This is just some random text to test the Client and server at a transfer rate of 8bytes or 8bits? IDK IDC.\n"

try:
    #Sending Data
    print("Sending: %s" % message)
    message = message.encode()
    sTream.sendall(message)
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sTream.recv(16)
        amount_received += len(data)
        print('Received %d bytes/%d bytes' %(amount_received, len(message)))
        print('received: %s' % data.decode('ascii'))
        time.sleep(5)
        print("5 seconds have passed !\n")


finally:
    print('Closing Socket...')
    client_socket.close()





