#import string
#wrd='hello dar,'
#print(wrd.strip(','))
#print(string.punctuation)

import socket
from datetime import datetime

server_address=('localhost',6789)
max_size=4096

print('Starting the client at',datetime.now())
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(b'Hey!',server_address)
data,sever=client.recvfrom(max_size) # 돌아오는 datagram을 기다림
print('At',datetime.now(),sever,'said',data)
client.close()

#Starting the client at 2022-03-07 14:03:00.571591
#At 2022-03-07 14:03:00.604368 ('127.0.0.1', 6789) said b'Are you talking to me?'