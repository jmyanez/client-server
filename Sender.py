import socket
import os

host = socket.gethostname()
port = 50001
address = (host,port)
buffer = 16
file_name = "C:/Users/manue/PycharmProjects/s18-nets-udp-file-transfer-jmyanez/stopWait/client/textfile.txt"
file_info =os.stat("C:/Users/manue/PycharmProjects/s18-nets-udp-file-transfer-jmyanez/stopWait/client/textfile.txt")
print(file_info.st_size ,"Bytes")
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)

data,address = s.recvfrom(buffer)
print("Received: ",data)


