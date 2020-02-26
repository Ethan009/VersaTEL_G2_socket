#coding:utf-8

import socket

ip_port = ('10.203.1.89', 12128)

def conn(commands):
    # s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # client=ssl.wrap_socket(s,ca_certs='key.pem',cert_reqs=ssl.CERT_REQUIRED)
    client=socket.socket()
    client.connect(ip_port)
    data = client.recv(8192).decode()
    print (data)
    client.send(str(commands).encode())
    commandsData = client.recv(8192).decode()
    #print (commandsData)
    client.send(b'exit')
    return commandsData