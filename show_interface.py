#! /usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

CISCO_CSR_XE_HOST = 'sandbox-iosxe-latest-1.cisco.com'
USERNAME='developer'
PASSWORD=getpass('\nEnder password for {}@{}: '.format(USERNAME, CISCO_CSR_XE_HOST))

device = {
    'device_type' : 'cisco_ios',
    'ip' : CISCO_CSR_XE_HOST,
    'username' : USERNAME,
    'password' : PASSWORD
}

device = ConnectHandler(**device)
output = device.send_command("show ip interface brief")
print()
print (output)
print()
device.disconnect()