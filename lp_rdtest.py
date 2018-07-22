
#f = open("hosts_072118.txt", "r")
#for z in f:
	#print(z.strip())

hosts_str = """
192.168.1.100
192.168.1.101
"""
hosts_arr = hosts_str.strip().splitlines()
for z in hosts_arr:
	print z
