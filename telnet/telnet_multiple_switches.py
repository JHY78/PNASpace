import getpass
import telnetlib

hosts = open("cs_ipaddresses.txt") # Open cisco switch ip information file
user = input("Enter your username: ")
password = getpass.getpass()

for host in hosts:
	print("Connect to : " + host)
	HOST = (host.strip()) 
	tn = telnetlib.Telnet(HOST)

	tn.read_until(b"Username: ")
	tn.write(user.encode('ascii') + b"\n")
	
	if password:
		tn.read_until(b"Password: ")
		tn.write(password.encode('ascii') + b"\n")

	tn.write(b"conf t\n")

	for vlan in range(101,105):
		tn.write(b"vlan " + str(vlan).encode('UTF-8') + b"\n")
		tn.write(b"name python_vlan_" + str(vlan).encode('UTF-8') + b"\n")

	if HOST == "192.168.37.20":
		for vlan in range(101,105):
			tn.write(b"int vlan " + str(vlan).encode('UTF-8') + b"\n")
			tn.write(b"ip add 10.10." + str(vlan).encode('UTF-8') + b".20 255.255.255.0" + b"\n")
			tn.write(b"no shut\n")
		
	tn.write(b"end\n")
	tn.write(b"exit\n")

	print(tn.read_all().decode('ascii'))

