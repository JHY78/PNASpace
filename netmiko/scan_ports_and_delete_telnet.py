import socket
from netmiko import ConnectHandler

# defined by service vendor and type
ios_router   = ["192.168.37.201", "192.168.37.202","192.168.37.203"]
ios_switch  = ["192.168.37.102","192.168.37.112"]
eos_router  = ["192.168.37.101", "192.168.37.111","192.168.37.204"]

def port_scan_delete_telnet_ios(target):
    for ip in target:
        for port in range(22,24):
            destination = (ip, port)
            try: 
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(3)
                    connection = sock.connect(destination)
                    print(f" Target : {ip} / Open  port : {port}")
                    port_number = f"{port}"
                    if port_number == "23":
                        iso = {'device_type':'cisco_ios','ip':ip,'username':'devnet','password':'dn1001',}
                        net_connect = ConnectHandler(**iso)
                        commands = ['line vty 0 15','transport input ssh','no transport input all','no transport input telnet']
                        net_connect.send_config_set(commands)
                        print(f" * Removed telnet access service : {ip} ")
                        net_connect.disconnect()
            except:
                print(f" Target : {ip} / Close  port : {port}")  

def port_scan_delete_telnet_eos(target):
    for ip in target:
        for port in range(22,24):
            destination = (ip, port)
            try: 
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(3)
                    connection = sock.connect(destination)
                    print(f" Target : {ip} / Open  port : {port}")
                    port_number = f"{port}"
                    if port_number == "23":
                        eos = {'device_type':'arista_eos','ip':ip,'username':'devnet','password':'dn1001'}
                        net_connect = ConnectHandler(**eos)
                        commands = ['no management telnet']
                        net_connect.enable()
                        net_connect.config_mode()
                        net_connect.send_config_set(commands,exit_config_mode=False)
                        print(f" * Removed telnet access service : {ip} ")
                        net_connect.disconnect()
            except:
                print(f" Target : {ip} / Close  port : {port}")  

print("=" * 100)
print("* Cisco Router Enterprise Network Port Scan")
port_scan_delete_telnet_ios(ios_router)
print("-" * 100)

print("* Cisco Switch Enterprise Network Port Scan")
port_scan_delete_telnet_ios(ios_switch)
print("-" * 100)

print("* Arista Enterprise Network Port Scan")
port_scan_delete_telnet_eos(eos_router)
print("-" * 100)
