#!/usr/bin/env python3

from termcolor import colored
print(colored("*******Domain to Ip convertor*******",'green'))
print(colored("*******create by snoopy sugar*******",'red'))

import socket     #socket is a modules
import pyfiglet  #banner package

banner=colored(pyfiglet.figlet_format("IP Convertor"),'green')   #use for banner
print(banner)

Domain_Name=input("Please, Enter Domain Name:")

ip=socket.gethostbyname(Domain_Name)

print("IP For {} : {} ".format(Domain_Name,ip))

