# TELNET

### "backup_config.py"
``` python
import getpass
import telnetlib

HOST = "192.168.37.132"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"copy running-config tftp://192.168.37.129/running-config_from_dn1-ubuntu\n")

tn.write(b"\n")
tn.write(b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
```
* uses telnet 'telnetlib'
* run 'copy running-config tftp command'

### "telnet_loopback.py"
``` python
import getpass
import telnetlib

HOST = "192.168.37.10" # CR1
user = input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"int loopback 10\n")
tn.write(b"ip address 10.10.10.10 255.255.255.255\n")
tn.write(b"int loopback 20\n")
tn.write(b"ip address 20.20.20.20 255.255.255.255\n")
tn.write(b"int loopback 30\n")
tn.write(b"ip address 30.30.30.30 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"copy running-config startup-config\n")
tn.write(b"\n")
tn.write(b"sh ip int brief\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
'''

* access the single device via telnet
* configure loopback interface

### "telnet_multiple_switches.py"
``` python
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
'''
* access multiple switches
* define switch information as "cs_ipaddresses.txt" file.
* read "cs_ipaddresses.txt" file and run commands. 
