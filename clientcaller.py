#!/usr/bin/python
import client,time

sendData = '70344a7648516471334b50656d71536f8d7f660708278e882c0d0c681fe97879bc5ef86a9a3297dc6bd404adfab24b5895f177aeef5d3e29da2225fa405255d2c6e0b89f18f102dbd4a5c0a53519d7b8a8ba1dbf0cd82fbfc39176a3b941af07c0b223d49492c6caef83cad290d069bf69d72da348c0d6f7ad9ad66f15469b6f2f401c0d98f8a8de649748e257688acc6d0d0183e667776cb71379cc1b676b082ef4f00cae59d46b3203c3f0dbbb972a'
resultz = '70344a7648516471334b50656d71536f8d7f660708278e882c0d0c681fe97879bc5ef86a9a3297dc6bd404adfab24b5895f177aeef5d3e29da2225fa405255d2c6e0b89f18f102dbd4a5c0a53519d7b8a8ba1dbf0cd82fbfc39176a3b941af07c0b223d49492c6caef83cad290d069bf69d72da348c0d6f7ad9ad66f15469b6f2f401c0d98f8a8de649748e257688acc6d0d0183e667776cb71379cc1b676b082ef4f00cae59d46b3203c3f0dbbb972a:10:20'

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
    currentData = sendData[0:len(sendData) - 2] + hex2str(dec2hex(i))
    result = client.connect(ipaddr,port,currentData,keyid)

    if result != '' and currentData != sendData:
        i = currentData[len(sendData) - 2:len(sendData)]
        print "Data sent to get valid padding:", currentData
        print "Last byte in hex is: ", int(i) ^ 01, "\nLast byte in decimal is: ", int(i,16)


#thisData = sendData[len(sendData) - 4 : len(sendData)]

#for i in range (0,255):
#    hexOne = int(sendData[len(sendData) - 4 : len(sendData) - 3],16) ^ 2 ^ i 
#    hexTwo = int(sendData[len(sendData) - 2 : len(sendData) - 1],16) ^ 2 ^ 36
#    currentEnd = hex2str(dec2hex(hexOne)) + hex2str(dec2hex(hexTwo))
    
#    currentData = sendData[0:len(sendData) - 4] + currentEnd
#    result = client.connect(ipaddr,port,currentData,keyid)
    
#    if result != '' and currentData != sendData:
#        i = currentData[len(sendData) - 4:len(sendData) - 2]
#        print "Last byte in hex is: ", dec2hex(int(i,16) ^ 02), "\nLast byte in decimal is: ", int(i,16)
