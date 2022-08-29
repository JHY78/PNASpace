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

# tn.write(b"ls\n")
# tn.write(b"exit\n")

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
