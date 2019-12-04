#!/bin/env python

# Importing the modules needed for this script
from socket import *  # This module is the most needed
import sys
import time
from datetime import datetime
import subprocess

# To clear screen
subprocess.call('clear', shell=True)

# Ask for input from user
host = " "
max_port = 5000
min_port = 1

# Takes/ask for input from user; Input IPV4 to scan
# Initiating the Program (Port Scanner)
try:
    host = raw_input("[*] Enter Target Host Address: ")
except KeyboardInterrupt:  # Takes the ctrl + C input to end program
    print("\n\n[*] User Requested An Interrupt.")
    print("[*] Application Shutting Down.")
    sys.exit(1)

# This function simply returns the up numberic vaules
hostip = gethostbyname(host)
print("\n[*] Host: %s IP: %s" % (host, hostip))
print("[*] Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

# The Scannig of the host function


def scan_host(host, port, r_code=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        excute = s.connect_ex((host, port))

        if excute == 0:
            r_code = excute
        s.close()
    except Exception, e:
        pass
    return r_code


# The scanning portion of the code
for port in range(min_port, max_port):  # For each niumber alias port in range do something
    try:
        response = scan_host(host, port)

        if response == 0:
            print("[*] Port %d: Open" % (port))
    except Exception, e:
        pass


stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n[*] Scanning Finished At %s ..." % (time.strftime("%H:%M:%S")))
print("[*] Scanning Duration: %s ..." % (total_time_duration))
print("[*] An Objection is not a rejection; it is simply a request for more information.")


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.settimeout(2)

# port = 1000
# for portx in range(1, 100):
#    try:
#        s.connect(('ad.samclass.info', port))
#        r = s.recv(1024)
#        if 'Congratulation' in r.decode('utf8'):
#            print('[!] HIDDEN SERVICE FOUND:') % s ~ % s' % (portx, r.decode('utf8'))
#            s.close()
#            break
#        else:
#            print('%s ~ %s' % (portx, r.decode('utf8')))
#            s.close()

#    except socket.error as err:
#        print('%s ~ %s' % (portx, err))

#    port += 1000
