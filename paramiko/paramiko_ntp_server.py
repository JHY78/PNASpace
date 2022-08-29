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

	

	
 
