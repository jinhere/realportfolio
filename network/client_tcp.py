from datetime import datetime
import socket

address=('localhost',6789)
max_size=1000

print('Starting the client at',datetime.now())
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp의 일종인 streaming protocol
client.connect(address) # 스트림을 설정하기 위해 connect()
client.sendall(b'Hey!')
data=client.recv(max_size)
print('At',datetime.now(),'someone replied',data)
client.close()

# tcp서버는 client.sendall을 호출하고 udp는 client.sendto를 호출하여 응답한다.