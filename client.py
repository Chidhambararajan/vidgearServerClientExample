from vidgear.gears import NetGear
import cv2
import time

client = NetGear(receive_mode=True)

while True :
    frame = client.recv()

    if frame is None :
        time.sleep(1)
        print("Waiting for video stream")
        client = NetGear(receive_mode=True)
        continue
    print("Connected")
    cv2.imshow("out",frame)
    cv2.waitKey(1)
