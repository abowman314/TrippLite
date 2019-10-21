import subprocess
import paramiko

f = open("upsIPs.txt")

for IPs in f:
    print(IPs)






subprocess.run("snmpset -v 2c -c tripplite 10.13.38.5  .1.3.6.1.4.1.850.1.1.1.2.1.8.1 s "" ")