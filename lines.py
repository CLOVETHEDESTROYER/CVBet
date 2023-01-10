import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (300, 50), (600, 0), (0, 0, 255), 5)
    img = cv2.rectangle(img, (980, 0), (680, 50), (0, 0, 255), 5)
    img = cv2.rectangle(img, (0, 0), (200, 200), (0, 0, 255), 5)
    img = cv2.rectangle(img, (1280, 200), (1080, 0), (0, 0, 255), 5)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Carlos is Great!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()