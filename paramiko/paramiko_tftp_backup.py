import re
import time
import paramiko
from datetime import datetime
from getpass import getpass

save_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
cisco_devices = ["192.168.37.10","192.168.37.20", "192.168.37.21", "192.168.37.22", "192.168.37.23"]
start_time = time.mktime(time.localtime())

def user_info():       
	global username
	global password
	print("Cisco Device Configuration Backup Script")	
	username = input(" * Enter username : ")
	password = getpass(" * Enter user's password : ")
	
	return username, password

user_info()        

for ip in cisco_devices:
	print(f"Save Time : {save_time}")
	print(f"--- Connecting to {ip}") 
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=ip, username=username, password=password)
	print(f"--- Connected to {ip}")
	print(f"--- Running config backup of {ip}")

	rc = ssh_client.invoke_shell()
	time.sleep(3)
	rc.send("copy running-config tftp\n")
	rc.send("192.168.37.129\n")
	rc.send((ip) + ".backup@" + (save_time) + "\n")
	time.sleep(3)

	output = rc.recv(65535)
	print(output.decode('ascii'))

	print(f"--- Completed the backup of {ip}")
	print("-" * 100)
	ssh_client.close
	time.sleep(1)

total_time = time.mktime(time.localtime()) - start_time
print(f" Total time to backup config : {total_time} seconds")

	  
	
	
