import socket
import cv2
import numpy as np
import time

##HOST = ''
##PORT = 30000
server_address = ('', 30000)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind(server_address)
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
print('Socket now accept')
count = 0
while True:
    data = conn.recv(1024*100)
    start = data[:data.find("start") + 5]
    stop = data[data.find("stop"):]
    if (start == "start" and stop == "stop"):
        data = data[data.find("start") + 5 : data.find("stop")]
        nparr = np.fromstring(data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow('server', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        count += 1
        print ('frame' + str(count))
        conn.sendall("1")
    else:
        conn.sendall("0")
        continue
    
