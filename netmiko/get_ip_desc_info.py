import socket
from netmiko import ConnectHandler

# defined by service vendor and type
ios_router   = ["192.168.37.201", "192.168.37.202","192.168.37.203"]
ios_switch  = ["192.168.37.102","192.168.37.112"]
eos_router  = ["192.168.37.101", "192.168.37.111","192.168.37.204"]

# get interface and desc information 
def get_interface_info_ios(target):
    for ip in target:
        ios = {'device_type':'cisco_ios','ip':ip,'username':'devnet','password':'dn1001',}
        net_connect = ConnectHandler(**ios)
        output = net_connect.send_command('sh ip int brief')
        output += net_connect.send_command('sh int desc')
        print('-' * 100)
        print(f" {ip} : interface information")
        print('-' * 100)
        print(output)
        net_connect.disconnect()

# get interface and desc information 
def get_interface_info_eos(target):
    for ip in target:
        eos = {'device_type':'arista_eos','ip':ip,'username':'devnet','password':'dn1001'}
        net_connect = ConnectHandler(**eos)
        output = net_connect.send_command('sh ip int brief')
        output += net_connect.send_command('sh int desc')
        print('-' * 100)
        print(f" {ip} : interface information")
        print('-' * 100)
        print(output)
        net_connect.disconnect()

print("=" * 100)
print("* Cisco Router Interface Information")
get_interface_info_ios(ios_router)
print("-" * 100)

print("=" * 100)
print("* Cisco Switch Interface Information")
get_interface_info_ios(ios_switch)
print("-" * 100)

print("=" * 100)
print("* Arista Router Interface Information")
get_interface_info_eos(eos_router)
print("-" * 100)