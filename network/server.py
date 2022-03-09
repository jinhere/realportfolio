#browser=webdriver.Chrome("C:\\Users\\Notebook\\Downloads\\chromedriver_win32\\chromedriver.exe")
#열다가 꺼지면 드라이버 새버전 다운하삼
from datetime import datetime
import socket

server_address=('localhost',6789)
max_size=4096

print('Starting the server at',datetime.now())
print('Waiting for a client to call.')
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # socket.socket() creates a socket
server.bind(server_address) # bind()는 소켓에 바인딩한다. 해당 ip 주소와 포트에 도달하는 모든 데이터를 청취

data,client=server.recvfrom(max_size) # 돌아오는 datagram을 기다림
# datagram arrives.. server wakes up 
# client variable contains ip address + port data

print('At',datetime.now(),client,'said',data) 
server.sendto(b'Are you talking to me?',client)
server.close()

#Starting the server at 2022-03-07 14:02:46.672285
#Waiting for a client to call.
#At 2022-03-07 14:03:00.604182 ('127.0.0.1', 62990) said b'Hey!'