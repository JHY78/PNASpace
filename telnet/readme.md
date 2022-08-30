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
