from netmiko import ConnectHandler

cisco_routers = [
        {
    "device_type": "cisco_ios",
    "host": "192.168.37.201",
    "username": "devnet",
    "password": "dn1001",
    },
        {
    "device_type": "cisco_ios",
    "host": "192.168.37.202",
    "username": "devnet",
    "password": "dn1001",
    },
        {
    "device_type": "cisco_ios",
    "host": "192.168.37.203",
    "username": "devnet",
    "password": "dn1001",
    },
]

cisco_switches = [
        {
    "device_type": "cisco_ios",
    "host": "192.168.37.102",
    "username": "devnet",
    "password": "dn1001",
    },
        {
    "device_type": "cisco_ios",
    "host": "192.168.37.112",
    "username": "devnet",
    "password": "dn1001",
    },
]

arista_routers = [
        {
    "device_type": "arista_eos",
    "host": "192.168.37.101",
    "username": "devnet",
    "password": "dn1001",
    },
        {
    "device_type": "arista_eos",
    "host": "192.168.37.111",
    "username": "devnet",
    "password": "dn1001",
    },
        {
    "device_type": "arista_eos",
    "host": "192.168.37.204",
    "username": "devnet",
    "password": "dn1001",
    },
]

# cisco router configuration
for device in cisco_routers:
    net_connect = ConnectHandler(**device)
    print(f"* Configuring NTP server : {device['host']}")
    commands = ['ntp server 192.168.37.129','clock timezone utc -0']
    net_connect.send_config_set(commands)
    output = net_connect.send_command("sh ntp status")
    output += net_connect.send_command("show ntp associations")
    print('-'*100)
    print(output)
    print('-'*100)
    net_connect.disconnect()

# cisco switch configuration
for device in cisco_switches:
    net_connect = ConnectHandler(**device)
    print(f"* Configuring NTP server : {device['host']}")
    commands = ['ntp server 192.168.37.129','clock timezone utc -0']
    net_connect.send_config_set(commands)
    output = net_connect.send_command("sh ntp status")
    output += net_connect.send_command("show ntp associations")
    print('-'*100)
    print(output)
    print('-'*100)
    net_connect.disconnect()

# arista router configuration
for device in arista_routers:
    net_connect = ConnectHandler(**device)
    print(f"* Configuring NTP server : {device['host']}")
    commands = ['no ntp local-NTP','ntp server 192.168.37.129','clock timezone UTC']
    net_connect.enable()
    net_connect.config_mode()
    net_connect.send_config_set(commands,exit_config_mode=False)
    output = net_connect.send_command("show ntp associations")
    output += net_connect.send_command("show clock")
    print('-'*100)
    print(output)
    print('-'*100)
    net_connect.disconnect()