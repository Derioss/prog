#!/bin/python3

#__ survey_credential.py _______________________________________
# Author: Frederic MAURY
# Date  : 2018/09/01
# Goal  : Survey CMS user credential
#________________________________________________________
import paramiko
import datetime
from datetime import datetime as dt

###_________________VARIABLE_____________________
listIp = ('192.168.1.82','192.168.1.82')
user = "root"
passwd = "010Mouray045="
command ="date +'%m/%d/%Y'&&date +'%m/%d/%Y'&&date +'%m/%d/%Y'"


#_________________FUNCTION_______________________
#SSH connect
def nouvelle_co(ip,user,passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    return client

#use command and return stdout
def inject_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    stdout = stdout.read().splitlines()
    client.close()
    return stdout


#___________________MAIN____________________________
def main ():
    for ip in listIp:
        conNect = nouvelle_co(ip,user,passwd)
        consoleValue = inject_command(conNect,command)
        print(consoleValue)
        for line in consoleValue:
           line = line.decode('UTF-8')
           print(line)
           date2 = dt.strptime(line.split()[0],"%m/%d/%Y")
           date2=date2.date()
           firstday = datetime.date.today()
           seconday = date2
           diff = firstday - seconday
           diff = diff.days
           print(diff)
           if diff <= 30:
            print("j'ai gagné")






main()
