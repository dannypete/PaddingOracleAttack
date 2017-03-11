#!/usr/bin/python
import client,time

sendData = '70344a7648516471334b50656d71536f8d7f660708278e882c0d0c681fe97879bc5ef86a9a3297dc6bd404adfab24b5895f177aeef5d3e29da2225fa405255d2c6e0b89f18f102dbd4a5c0a53519d7b8a8ba1dbf0cd82fbfc39176a3b941af07c0b223d49492c6caef83cad290d069bf69d72da348c0d6f7ad9ad66f15469b6f2f401c0d98f8a8de649748e257688acc6d0d0183e667776cb71379cc1b676b082ef4f00cae59d46b3203c3f0dbbb972a'

ipaddr = '64.106.46.58'
port = '10020'
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

totalResult = ''
for blockNumber in range(0,1):

    currentBlocksRaw = sendData[len(sendData)-64:len(sendData)]
    blockOne = currentBlocksRaw[0:32]
    blockTwo = currentBlocksRaw[32:64]

    encryptedBytes = [blockOne[h:h+2] for h in range(0, len(blockOne), 2)] 
    unencryptedBytes = []
    
    for p in range (0,16):
        unencryptedBytes.append(int(encryptedBytes[p],16))
        
    print unencryptedBytes
    
    #####################################################################################
        ## Byte 16
    for i in range (0,255):
        byteGuess = dec2hexStr(int(blockOne[30:32],16) ^ i ^ 1)
        currentData = blockOne[0:30] + byteGuess + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[15] = i
            break
     #####################################################################################       
        ## Byte 15        
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ 2)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[28:30],16) ^ i ^ 2)
        currentData = blockOne[0:28] + byteGuess + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[14] = i
            break    
     #####################################################################################       
        ## Byte 14        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ 3)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ 3)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[26:28],16) ^ i ^ 3)
        currentData = blockOne[0:26] + byteGuess + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[13] = i
            break
    #####################################################################################
        ## Byte 13      
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ 4)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ 4)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ 4)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[24:26],16) ^ i ^ 4)
        currentData = blockOne[0:24] + byteGuess + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[12] = i
            break
    #####################################################################################  
        ## Byte 12
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ 5)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ 5)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ 5)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ 5)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[22:24],16) ^ i ^ 5)
        currentData = blockOne[0:22] + byteGuess + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[11] = i
            break
    #####################################################################################     
         ## Byte 11
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ 6)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ 6)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ 6)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ 6)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ 6)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[20:22],16) ^ i ^ 6)
        currentData = blockOne[0:20] + byteGuess + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[10] = i
            break
    #####################################################################################        
         ## Byte 10
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ 7)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ 7)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ 7)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ 7)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ 7)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ 7)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[18:20],16) ^ i ^ 7)
        currentData = blockOne[0:18] + byteGuess + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[9] = i
            break
    #####################################################################################        
         ## Byte 9
    m = 8
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[8] = i
            break
    #####################################################################################        
                 ## Byte 8
    m = 9
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[7] = i
            break
    #####################################################################################
        ## Byte 7        
    m = 10
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[6] = i
            break
    #####################################################################################
        ## Byte 6        
    m = 11
    byteSeven = dec2hexStr(int(blockOne[12:14],16) ^ unencryptedBytes[6] ^ m)
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteSeven + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[5] = i
            break
    #####################################################################################
        ## Byte 5
    m = 12
    byteSix = dec2hexStr(int(blockOne[10:12],16) ^ unencryptedBytes[5] ^ m)
    byteSeven = dec2hexStr(int(blockOne[12:14],16) ^ unencryptedBytes[6] ^ m)
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteSix + byteSeven + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)
    # here
        if result != '':
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[4] = i
            break
    #####################################################################################
        ## Byte 4
    m = 13
    byteFive = dec2hexStr(int(blockOne[8:10],16) ^ unencryptedBytes[4] ^ m)
    byteSix = dec2hexStr(int(blockOne[10:12],16) ^ unencryptedBytes[5] ^ m)
    byteSeven = dec2hexStr(int(blockOne[12:14],16) ^ unencryptedBytes[6] ^ m)
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteFive + byteSix + byteSeven + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[3] = i
            break
    #####################################################################################
        ## Byte 3        
    m = 14
    byteFour = dec2hexStr(int(blockOne[6:8],16) ^ unencryptedBytes[3] ^ m)
    byteFive = dec2hexStr(int(blockOne[8:10],16) ^ unencryptedBytes[4] ^ m)
    byteSix = dec2hexStr(int(blockOne[10:12],16) ^ unencryptedBytes[5] ^ m)
    byteSeven = dec2hexStr(int(blockOne[12:14],16) ^ unencryptedBytes[6] ^ m)
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteFour + byteFive + byteSix + byteSeven + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[2] = i
            break
    #####################################################################################
        ## Byte 2        
    m = 15
    byteThree = dec2hexStr(int(blockOne[4:6],16) ^ unencryptedBytes[2] ^ m)
    byteFour = dec2hexStr(int(blockOne[6:8],16) ^ unencryptedBytes[3] ^ m)
    byteFive = dec2hexStr(int(blockOne[8:10],16) ^ unencryptedBytes[4] ^ m)
    byteSix = dec2hexStr(int(blockOne[10:12],16) ^ unencryptedBytes[5] ^ m)
    byteSeven = dec2hexStr(int(blockOne[12:14],16) ^ unencryptedBytes[6] ^ m)
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = blockOne[0:32 - 2 * m] + byteGuess + byteThree + byteFour + byteFive + byteSix + byteSeven + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[1] = i
            break
    #####################################################################################
        ## Byte 1        
    m = 16
    byteTwo = dec2hexStr(int(blockOne[2:4],16) ^ unencryptedBytes[1] ^ m)
    byteThree = dec2hexStr(int(blockOne[4:6],16) ^ unencryptedBytes[2] ^ m)
    byteFour = dec2hexStr(int(blockOne[6:8],16) ^ unencryptedBytes[3] ^ m)
    byteFive = dec2hexStr(int(blockOne[8:10],16) ^ unencryptedBytes[4] ^ m)
    byteSix = dec2hexStr(int(blockOne[10:12],16) ^ unencryptedBytes[5] ^ m)
    byteSeven = dec2hexStr(int(blockOne[12:14],16) ^ unencryptedBytes[6] ^ m)
    byteEight = dec2hexStr(int(blockOne[14:16],16) ^ unencryptedBytes[7] ^ m)
    byteNine = dec2hexStr(int(blockOne[16:18],16) ^ unencryptedBytes[8] ^ m)
    byteTen = dec2hexStr(int(blockOne[18:20],16) ^ unencryptedBytes[9] ^ m)
    byteEleven = dec2hexStr(int(blockOne[20:22],16) ^ unencryptedBytes[10] ^ m)
    byteTwelve = dec2hexStr(int(blockOne[22:24],16) ^ unencryptedBytes[11] ^ m)    
    byteThirteen = dec2hexStr(int(blockOne[24:26],16) ^ unencryptedBytes[12] ^ m)       
    byteFourteen = dec2hexStr(int(blockOne[26:28],16) ^ unencryptedBytes[13] ^ m)        
    byteFifteen = dec2hexStr(int(blockOne[28:30],16) ^ unencryptedBytes[14] ^ m)
    byteSixteen = dec2hexStr(int(blockOne[30:32],16) ^ unencryptedBytes[15] ^ m)
    for i in range (0, 255):
        byteGuess = dec2hexStr(int(blockOne[32 - 2 * m:32 - 2 * (m - 1)],16) ^ i ^ m)
        currentData = byteGuess + byteTwo + byteThree + byteFour + byteFive + byteSix + byteSeven + byteEight + byteNine + byteTen + byteEleven + byteTwelve + byteThirteen + byteFourteen + byteFifteen + byteSixteen + blockTwo
        result = client.connect(ipaddr,port,currentData,keyid)

        if result != '' and currentData != currentBlocksRaw:
            print "Altered byte sent to get valid padding:", hex2str(dec2hex(i)), "\n"
            unencryptedBytes[0] = i
            break


    print unencryptedBytes

    result = ''
    for elem in unencryptedBytes:
        result += str(unichr(elem))
        
    print result
    totalResult += result



#print totalResult





















