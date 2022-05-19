from netmiko import ConnectHandler

def ConfigInterface():
    Interface = input("Enter Interface:")
    IP = input("Enter IP address and mask:")
    commands = ["interface " + str(Interface), "ip address " + str(IP)]
    resultintconfig = ssh_connect.send_config_set(commands)
    return resultintconfig

def saveconfig():
    resultsave = ssh_connect.send_command("wr")
    return resultsave

f = open("/home/routers.txt")
Routers = f.read().splitlines()
for router in Routers:
    dev = {
            "device_type": "cisco_ios",
            "host": router,
            "username": "moakod",
            "password": "cisco"
            }
    ssh_connect = ConnectHandler(**dev)
    while True:
        config = input("want to config an Interface?(y/n)")
        if config == "n":
            break
        elif config == "y":
            result = ConfigInterface()
            print(result)
        else:
            print("Please enter y or n")
        print(saveconfig())