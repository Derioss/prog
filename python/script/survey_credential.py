import os
import paramiko

def nouvelle_co():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.1.82', username='root', password='010Mouray045=')
    return client

def test():
    client = nouvelle_co()
    #stdin, stdout, stderr = client.exec_command("ls")
    command = "ls"
    stdin, stdout, stderr = client.exec_command(command)
    #stdin, stdout, stderr = client.exec_command(command2)
    for line in stdout.read().splitlines():
        print(line)
    client.close()
    return
test()
