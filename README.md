# TrippLite
TrippLite PANMS 

File must be named:
paconfig.ini

Data File: upsIPs.txt
- must be a text file with IP address, 1 per line

Import by:
1. CLOSE PowerAlert GUI
2. STOP service "PowerAlert Agent"
3. DELETE all files in: C:\Program Files (x86)\TrippLite\PowerAlert\data
4. COPY new paconfig.ini file to C:\Program Files (x86)\TrippLite\PowerAlert
5. START service "PowerAlert Agent"
6. OPEN PowerAlert GUI
7. Wait for new devices to populate ~1-10 minutes

Export by:
Settings -> System -> Write Config File



~ Andrew Bowman - Service King - 10/3/2019
