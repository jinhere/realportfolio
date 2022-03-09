from datetime import datetime
import socket

address=('localhost',6789)
max_size=1000

print('Starting the server at',datetime.now())
print('Waiting for a client to call.')
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(5) # listen() 은 대기중인 커넥션의 최대 수 를 5로 지정

client,addr=server.accept() # 도착한 첫번째 유효한 메세지를 얻는다.
data=client.recv(max_size) # 메세지 최대 허용 길이

print('At',datetime.now(),client,' said',data)
client.sendall(b'Are you talking to me?')
client.close()
server.close()