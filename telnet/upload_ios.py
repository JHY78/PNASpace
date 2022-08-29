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

tn.write(b"copy tftp://192.168.37.129/c3725-adventerprisek9-mz.124-15.T14.bin flash:c3725-adventerprisek9-mz.124-15.T14.bin\n")

tn.write(b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
