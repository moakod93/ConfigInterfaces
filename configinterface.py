from netmiko import ConnectHandler

devip = input("Enter the device IP to configure:")
interface = input("Enter Interface:")
intip = input("Enter IP address and mask:")
device = {
    "device_type": "cisco_ios",
    "host": devip,
    "username": "moakod",
    "password": "cisco"
}
ssh_connect = ConnectHandler(**device)
commands = ["interface " + str(interface), "ip address " + str(intip)]
result = ssh_connect.send_config_set(commands)
print(result)