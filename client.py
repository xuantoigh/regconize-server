import socket
import time
import cv2
server_address = ('192.168.0.103', 30000)
capture = cv2.VideoCapture(0)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
count = 0
while True:
    ret, frame = capture.read()
    frame = cv2.resize(frame, (640, 480))
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
    cv2.imshow('client', frame)
    data = 'start'
    data += cv2.imencode('.jpg', frame)[1].tostring()
    data += 'stop'
    sock.sendall(data)
    count += 1
    print count
    while True:
        flag = sock.recv(1024)
        if flag == "1":
            print ('flag: ' + str(flag))
            break
        else:
            print ('flag: ' + str(flag))
            continue

