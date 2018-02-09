import socket

host = socket.gethostname()
port = 50000
address = (host,port)
buffer_size = 16
file_name = "C:/Users/manue/PycharmProjects/s18-nets-udp-file-transfer-jmyanez/stopWait/client/textfile.txt"
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)
print("Waiting....")
hi = "o"
hi = hi.encode()
s.sendto(hi,address)
while 1:
    data,address = s.recvfrom(16)
    print("Received message: ", data.decode('ascii'))