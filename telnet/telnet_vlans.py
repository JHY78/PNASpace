import getpass
import telnetlib

HOST = "192.168.37.20" # assigned CS1's IP address
user = input("Enter your username: ") # username
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ") # changed the output
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Get into config mode
tn.write(b"config terminal\n")

# Create vlans (11 - 14)
tn.write(b"vlan 11\n")
tn.write(b"name Management_network\n")
tn.write(b"vlan 12\n")
tn.write(b"name Private_network\n")
tn.write(b"vlan 13\n")
tn.write(b"name Public_network\n")
tn.write(b"vlan 14\n")
tn.write(b"name Backup_network\n")
tn.write(b"exit\n")

# Assigne VLAN to switch port
tn.write(b"int g3/0\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 11\n")
tn.write(b"int g3/1\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 12\n")
tn.write(b"int g3/2\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 13\n")
tn.write(b"int g3/3\n")
tn.write(b"switchport mode access\n")
tn.write(b"switchport access vlan 14\n")
tn.write(b"end\n")

tn.write(b"exit\n")
# output all info
print(tn.read_all().decode('ascii'))
