#coding:utf-8

import socket

# ip_port = ('192.168.36.61', 12129)
ip_port = ('10.203.1.89', 12129)
judge_len = 8192

command=b'CLIcommands'
def conn():
    commandsData = ''
    client=socket.socket()
    client.connect(ip_port)
    data = client.recv(8192).decode()
    print (data)
    client.send(command)
    data_len = int(client.recv(8192).decode())+judge_len
    print ('data_len:',data_len)
    client.send(b'ok')
    while data_len>= judge_len:
        commandsData_part = client.recv(judge_len).decode('utf-8')
        data_len = data_len - judge_len
        commandsData += commandsData_part
    client.send(b'exit')
    return commandsData