from vidgear.gears import NetGear
import cv2

server = NetGear()
CAP = cv2.VideoCapture(0)

while CAP.isOpened():
    _,frame = CAP.read()
    try:
        server.send(frame)
    except RuntimeError :
        print("Client Unavailable")
