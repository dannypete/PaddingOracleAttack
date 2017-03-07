# Dependencies
import argparse
import socket
import sys

# Length of either response.
# Server response may have spaces in it
# to adhere to message length
MESSAGE_LENGTH = 32
BLOCK_SIZE = 32

def connect(ip, port, block, keyid):

    global MESSAGE_LENGTH, BLOCK_SIZE
    
    flag = False

    cipher_size = len(block)

    if not(cipher_size % BLOCK_SIZE == 0):
      print "Bad block(s) size"
      exit()

    else:
      # Create a TCP/IP socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      # Connect the socket to the port where the server is listening
      server_address = (ip, int(port))
      sock.connect(server_address)

      num_blocks = (cipher_size/BLOCK_SIZE)-1 # num_blocks to be decrypted (IV not counting as ciphertext block)

      message = block + ':' + str(num_blocks) + ':' + keyid

      try:
          # Send data  
          sock.sendall(message)

          # Look for the response
          amount_received = 0
          amount_expected = MESSAGE_LENGTH

          while amount_received < amount_expected:
              data = sock.recv(MESSAGE_LENGTH)
              amount_received += len(data)

              if "successful" in data:
                #print >>sys.stderr, 'Sending: "%s"' % message
                #print >>sys.stderr, 'Received: "%s"' % data
                flag = True

      finally:
          sock.close()
          if flag:
            return message
          else:
            return ''
          
