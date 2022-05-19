from netmiko import ConnectHandler

f = open("/home/moakod/PycharmProjects/ConfigInterfaces/routers.txt")
Routers = f.read().splitlines()

for router in Routers:
    dev = {
            "device_type": "cisco_ios",
            "host": router,
            "username": "moakod",
            "password": "cisco"
            }
    ssh_connect = ConnectHandler(**dev)
    print("Connecting to Router " + str(router))
    while True:
        config = input("want to config an Interface?(y/n)")
        if config == "n":
            break
        elif config == "y":
            Interface = input("Enter Interface:")
            IP = input("Enter IP address and mask:")
            commands = ["interface " + str(Interface), "ip address " + str(IP)]
            result = ssh_connect.send_config_set(commands)
            print(result)
        else:
            print("Please enter y or n")
        saveresult = ssh_connect.send_command("wr")
        print(saveresult)
