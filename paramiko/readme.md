# PARAMIKO
* ssh protocol python library
* runs on server or client
* send command via ssh remotely
* https://pypi.org/project/paramiko/
* https://www.paramiko.org/

### installation
    $ pip3 install paramiko
    $ python3
    >>> import paramiko

### "paramiko_ntp_server.py"

``` python
import time
import paramiko

cisco_devices = ["192.168.37.10","192.168.37.20", "192.168.37.21", "192.168.37.22", "192.168.37.23"]

username = "devnet"
password = "dn1001"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for ip in cisco_devices:
	ssh_client.connect(hostname=ip, username=username, password=password)
	print("Connected to " + ip + "\n")
	rc = ssh_client.invoke_shell()

	output1 = rc.recv(3000)
	
	rc.send("configure terminal\n")
	rc.send("clock timezone UTC -0\n")
	rc.send("ntp server 192.168.37.129\n")
	rc.send("exit\n")
	time.sleep(1)
	rc.send("copy running-config startup-config\n")
	rc.send("end\n")
	
	output2 = rc.recv(65535)

	print((output2).decode('ascii'))

	time.sleep(1)
	ssh_client.close()
  
	print("-" * 80)
```

* import paramiko module
* define cisco devices as list
* uses "paramiko.SSHClient()"
* run for statment to access the multiple devices
* run "ntp server command"

### "paramiko_tftp_backup.py"

``` python
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
```

* get the username using "input method"
* get the password using "getpass" python library
* import time to record the time
* define "user_info() function





