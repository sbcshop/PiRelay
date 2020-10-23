#! /usr/bin/env python3

import socket
import PiRelay

r1 = PiRelay.Relay("RELAY1")
r2 = PiRelay.Relay("RELAY2")
r3 = PiRelay.Relay("RELAY3")
r4 = PiRelay.Relay("RELAY4")

host = "192.168.0.123"  # Enter Raspberry pi ip here

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serv.bind((socket.gethostname(), 1000))
serv.bind((host, 1000))
serv.listen(5)

while True:
    print("Server started ")
    print(host)
    conn, addr = serv.accept()
    from_client = ''
    
    while True:
        data = conn.recv(500).decode('utf-8')
        if not data: break
        from_client = data
        print (from_client)
        if (from_client == 'A'):
           r1.on()
        elif (from_client == 'B'):
           r1.off()

        elif (from_client == 'C'):
           r2.on()

        elif (from_client == 'D'):
           r2.off()

        elif (from_client == 'E'):
           r3.on()

        elif (from_client == 'F'):
           r3.off()

        elif (from_client == 'G'):
           r4.on()

        elif (from_client == 'H'):
           r4.off()
        #conn.send("I am SERVER<br>")
    conn.close()
    print ('client disconnected')


