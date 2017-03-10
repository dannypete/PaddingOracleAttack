#!/usr/bin/python
import client,time

sendData = '70344a7648516471334b50656d71536f8d7f660708278e882c0d0c681fe97879bc5ef86a9a3297dc6bd404adfab24b5895f177aeef5d3e29da2225fa405255d2c6e0b89f18f102dbd4a5c0a53519d7b8a8ba1dbf0cd82fbfc39176a3b941af07c0b223d49492c6caef83cad290d069bf69d72da348c0d6f7ad9ad66f15469b6f2f401c0d98f8a8de649748e257688acc6d0d0183e667776cb71379cc1b676b082ef4f00cae59d46b3203c3f0dbbb972a'

ipaddr = '64.106.46.58'
port = '10000'
keyid = '20'

def dec2hexStr(d):
    return hex2str(dec2hex(d))

def dec2hex(d):
    return hex(d).split('x')[1]
    
def hex2str(h):
    result = str(h)
    if len(result) == 1:
        return '0' + result
    else:
        return result    

      
currentBlocksRaw = sendData[len(sendData)-64:len(sendData)]       
blockOne = currentBlocksRaw[0:32]
blockTwo = currentBlocksRaw[32:64]

# Byte 16
for i in range (0,255):
    byteGuess = dec2hexStr(int(blockOne[30:32],16) ^ i ^ 1)
    currentData = blockOne[0:30] + byteGuess + blockTwo
    result = client.connect(ipaddr,port,currentData,keyid)

    if result != '' and currentData != currentBlocksRaw:
        print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
        break
# Byte 15        
byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ 12 ^ 2)
for i in range (0, 255):
    byteGuess = dec2hexStr(int(blockOne[28:30],16) ^ i ^ 2)
    currentData = blockOne[0:28] + byteGuess + byteSixteen + blockTwo
    result = client.connect(ipaddr,port,currentData,keyid)

    if result != '' and currentData != currentBlocksRaw:
        print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n" 
        break    
        
# Byte 14        
byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ 12 ^ 3)
byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ 12 ^ 3)
for i in range (0, 255):
    byteGuess = dec2hexStr(int(blockOne[26:28],16) ^ i ^ 3)
    currentData = blockOne[0:26] + byteGuess + byteFifteen + byteSixteen + blockTwo
    result = client.connect(ipaddr,port,currentData,keyid)

    if result != '' and currentData != currentBlocksRaw:
        print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
        break

