import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # translate the hostname to ip

print('-' * 50)
print('scanning target ' +target)
print('Time is :'+str(datetime.now()))
print('-' * 50)

try:

    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print('port {} is open', format(port))
        s.close()
except KeyboardInterrupt:
    print('\ exit program')
    sys.exit()
