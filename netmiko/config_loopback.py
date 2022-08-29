from netmiko import ConnectHandler

# defined by service type
blue = ["192.168.37.101", "192.168.37.102"]
red  = ["192.168.37.111","192.168.37.112"]
as1299  = "192.168.37.201"
as7922  = "192.168.37.202"
as16509 = "192.168.37.203"
as3356  = "192.168.37.204"
jr1 = "192.168.37.10"

# deviced by vendor & role
cisco_routers   = ["192.168.37.201", "192.168.37.202","192.168.37.203"]
cisco_switches  = ["192.168.37.102","192.168.37.112"]
arista_routers  = ["192.168.37.101", "192.168.37.111","192.168.37.204"]
juniper_routers = ["192.168.37.10"]

# as1299 config
as1299 = {
	'device_type':'cisco_ios', 
	'ip':'192.168.37.201',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** as1299 : Cisco Interface Configuration ***")
commands = [
    'int lo0','desc as1299.lo0','ip add 12.12.12.12 255.255.255.255','no shut',
    'int g0/0','desc to_server','no shut',
    'int g0/1','desc to_as3356.e2','ip add 1.12.33.1 255.255.255.252','no shut',
    'int g0/2','desc to_as16509.g0/3','ip add 1.12.16.1 255.255.255.252','no shut',
    'int g0/3','desc to_blue_r1.e1','ip add 1.12.200.1 255.255.255.252','no shut',
    ]
net_connect = ConnectHandler(**as1299)
net_connect.send_config_set(commands)
output = net_connect.send_command("show ip int brief")
print(output)
print()
net_connect.disconnect()

# as7922 config
as7922 = {
	'device_type':'cisco_ios', 
	'ip':'192.168.37.202',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** as7922 : Cisco Interface Configuration ***")
commands = [
    'int lo0','desc as7922.lo0','ip add 79.79.79.79 255.255.255.255','no shut',
    'int g0/0','desc to_server','no shut',
    'int g0/1','desc to_as3356.e1','ip add 1.33.79.2 255.255.255.252','no shut',
    'int g0/2','desc to_as16509.g0/2','ip add 1.16.79.2 255.255.255.252','no shut',
    'int g0/3','desc to_red_r1.e1','ip add 1.79.100.1 255.255.255.252','no shut',
    ]
net_connect = ConnectHandler(**as7922)
net_connect.send_config_set(commands)
output = net_connect.send_command("show ip int brief")
print(output)
print()
net_connect.disconnect()

# as16509 config
as16509 = {
	'device_type':'cisco_ios', 
	'ip':'192.168.37.203',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** as16509 : Cisco Interface Configuration ***")
commands = [
    'int lo0','desc as16509.lo0','ip add 16.16.16.16 255.255.255.255','no shut',
    'int g0/0','desc to_server','no shut',
    'int g0/1','desc to_none','shut',
    'int g0/2','desc to_as7922.g0/2','ip add 1.16.79.1 255.255.255.252','no shut',
    'int g0/3','desc to_as1299.g0/2','ip add 1.12.16.2 255.255.255.252','no shut',
    ]
net_connect = ConnectHandler(**as16509)
net_connect.send_config_set(commands)
output = net_connect.send_command("show ip int brief")
print(output)
print()
net_connect.disconnect()


# as3356 Configuration 

as3356 = {
	'device_type':'arista_eos', 
	'ip':'192.168.37.204',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** as3356 Interface Configuration ***")
net_connect = ConnectHandler(**as3356)
commands = ['int lo0','desc as3356.lo0','ip add 33.33.33.33/32',
			'int et1','desc to_as7922.g0/1','no switchport','ip add 1.33.79.1/30',
            'int et2','desc to_as1299.g0/1','no switchport','ip add 1.12.33.2/30',
			'int et11','desc to_blue_r1.e2','no switchport','ip add 1.33.200.1/30',
            'int et12','desc to_red_r1.e2','no switchport','ip add 1.33.100.1/30'
			]
net_connect.enable()
net_connect.config_mode()
net_connect.send_config_set(commands,exit_config_mode=False)
output = net_connect.send_command('show ip int brief')
print(output)
print()
net_connect.disconnect()

# red_r1 Configuration 

red_r1 = {
	'device_type':'arista_eos', 
	'ip':'192.168.37.111',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** red_r1 Interface Configuration ***")
net_connect = ConnectHandler(**red_r1)
commands = ['int lo0','desc red_r1.lo0','ip add 100.100.100.100/32',
			'int et1','desc to_as7922.g0/3','no switchport','ip add 1.79.100.2/30',
            'int et2','desc to_as3356.e12','no switchport','ip add 1.33.100.2/30',
			'int et12','desc to_red-s1.g0/1','no switchport','ip add 192.168.100.1/24',
			]
net_connect.enable()
net_connect.config_mode()
net_connect.send_config_set(commands,exit_config_mode=False)
output = net_connect.send_command('show ip int brief')
print(output)
print()
net_connect.disconnect()

# blue_r1 Configuration 
blue_r1 = {
	'device_type':'arista_eos', 
	'ip':'192.168.37.101',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** blue_r1 Interface Configuration ***")
net_connect = ConnectHandler(**blue_r1)
commands = ['int lo0','desc blue_r1.lo0','ip add 200.200.200.200/32',
			'int et1','desc to_as1299.g0/3','no switchport','ip add 1.12.200.2/30',
            'int et2','desc to_as3356.e11','no switchport','ip add 1.33.200.2/30',
			'int et12','desc to_blue-s1.g0/1','no switchport','ip add 192.168.200.1/24',
			]
net_connect.enable()
net_connect.config_mode()
net_connect.send_config_set(commands,exit_config_mode=False)
output = net_connect.send_command('show ip int brief')
print(output)
print()
net_connect.disconnect()

# red_s1 config
red_s1 = {
	'device_type':'cisco_ios', 
	'ip':'192.168.37.112',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** red_s1 : Cisco Interface Configuration ***")
commands = [
    'int lo0','desc red_s1.lo0',
    'int g0/0','desc to_server','no shut',
    'vlan 100','name mgmt-network','int vlan 100','ip add 192.168.100.2 255.255.255.0','no shut',
    'int g0/1','switch mode acc','sw acc vlan 100','no shut'
    ]
net_connect = ConnectHandler(**red_s1)
net_connect.send_config_set(commands)
output = net_connect.send_command("show ip int brief")
print(output)
print()
net_connect.disconnect()

# blue_s1 config
blue_s1 = {
	'device_type':'cisco_ios', 
	'ip':'192.168.37.102',
	'username':'devnet',
	'password':'dn1001',
}

print(" *** blue_s1 : Cisco Interface Configuration ***")
commands = [
    'int lo0','desc blue_s1.lo0',
    'int g0/0','desc to_server','no shut',
    'vlan 100','name mgmt-network','int vlan 200','ip add 192.168.200.2 255.255.255.0','no shut',
    'int g0/1','switch mode acc','sw acc vlan 200','no shut'
    ]
net_connect = ConnectHandler(**blue_s1)
net_connect.send_config_set(commands)
output = net_connect.send_command("show ip int brief")
print(output)
print()
net_connect.disconnect()