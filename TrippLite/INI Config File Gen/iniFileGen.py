# Andrew Bowman
# Service King
# Created - 10/2/2019

# Note: Edit value "RemoteMaxNodes=", on "Line 31" to adjust how many units PANMS can monitor - tested up to 750 by Tripplite

x = 1
#Create a new file if it does not exsist
f = open("paconfig.ini","w")

# Open upsIPs.txt file containing list of TrippLite UPS devices 
upsIPs = open("upsIPs.txt")

# Default configuragtion section
f.write("[Contacts]\n\n[Syslogs]\nEnabled=False\n\n\n")


# Add list of devices from upsIPs.txt file
for ipAddress in upsIPs:
    if x == 1:
        f.write("[PA_Remote]\n")
        f.write("Server={0}\n".format(ipAddress))
        f.write("SNMPMacAddress=\nSNMPVersion=2\nSNMPCommunity=tripplite\nSNMPPort=161\nSNMPTrapPort=162\n\n")
    else:
        f.write("[PA_Remote_{0}]\n".format(x))
        f.write("Server={0}\n".format(ipAddress))
        f.write("SNMPMacAddress=\nSNMPVersion=2\nSNMPCommunity=tripplite\nSNMPPort=161\nSNMPTrapPort=162\n\n")
    x+=1

# Add list of default variables from TrippLite support's example .ini file
f.write("[Variables]\n[PA_Engine]\nDataLogAppend=0\nDataLogDuration=7\nDataLogInterval=300\nDataLogTextFile=0\nEnableAutoDiscovery=0\nDisableAutoDiscoveryAtStartup=1\nEnableBroadcast=0\nEnableHibernation=1\nEnableLocalBroadcast=1\nEnableNetworkBroadcast=0\nEnableShutdownTimer=0\nEventLogAppend=0\nEventLogTextFile=0\nAutoUpdateTrapMinutes=0\nRemoteLoopbackDelay=2\nRemoteMaxNodes=500\nRemoteThreadCount=25\nRemoteTrapPort=162\nRemoteSnmpRetries=3\nRemoteSnmpTimeout=15\nRemoteOfflinePollCycles=10\nShutdownRequired=One\nSMTPAuthenticationRequired=0\nSMTPPort=25\nWriteExtendedValues=0\n\n[IPAddresses]\n\n\n\n")
f.close()