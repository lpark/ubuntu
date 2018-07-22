#!/usr/bin/env python

import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

#hosts_str = "192.168.1.100, 192.168.1.101"
hosts_str = """
192.168.1.100
192.168.1.101
"""
hosts_arr = hosts_str.strip().splitlines()
#hosts_arr = ['192.168.1.100', '192.168.1.101']
for z in hosts_arr:

#f = open("hosts_072118.txt", "r")
#for z in f:
#for n in range(100,102):
	HOST = str(z.strip())

	tn = telnetlib.Telnet(HOST)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
    	  tn.read_until("Password: ")
    	  tn.write(password + "\n")

	tn.write("conf t\n")

	for n in range (11,12):
	  x = str(n)
          tn.write("int loop " + x + "\n")
          tn.write("ip add " + x + "." + x + "." + x + "." + x + " 255.255.255.255\n")

	tn.write("end\n")
	tn.write("wr\n")
	tn.write("exit\n")

	print tn.read_all()
