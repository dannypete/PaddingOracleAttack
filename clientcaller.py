#!/usr/bin/python
import client,time

sendData = '70344a7648516471334b50656d71536f8d7f660708278e882c0d0c681fe97879bc5ef86a9a3297dc6bd404adfab24b5895f177aeef5d3e29da2225fa405255d2c6e0b89f18f102dbd4a5c0a53519d7b8a8ba1dbf0cd82fbfc39176a3b941af07c0b223d49492c6caef83cad290d069bf69d72da348c0d6f7ad9ad66f15469b6f2f401c0d98f8a8de649748e257688acc6d0d0183e667776cb71379cc1b676b082ef4f00cae59d46b3203c3f0dbbb972a'

ipaddr = '64.106.46.58'
port = '10020'
keyid = '20'

def dec2hex(d):
    return hex(d).split('x')[1]
    
def hex2str(h):
    result = str(h)
    if len(result) == 1:
        return '0' + result
    else:
        return result    

print "Last byte..."
for i in range (0,255):
    client.connect(ipaddr,port,sendData[0:len(sendData) - 2] + hex2str(dec2hex(i)),keyid)

print "Second to last byte..."
for i in range (0,255):
    client.connect(ipaddr,port,sendData[0:len(sendData) - 4] + '35' + hex2str(dec2hex(i)),keyid)
    
print "Third to last byte..."    
for i in range (0,255):
    client.connect(ipaddr,port,sendData[0:len(sendData) -6] + '34' + hex2str(dec2hex(i)) + '34',keyid)
