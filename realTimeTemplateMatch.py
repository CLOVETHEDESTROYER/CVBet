import cv2
import numpy as np

cap = cv2.VideoCapture(0)
template = cv2.imread('openCV_project/images/drpepper.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]




while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result =cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    #TM_CCORR_NORMED threshold is .96-1.00 **decent results but didnt track perfectly
    #cv2.TM_CCOEFF_NORMED threshold .15-.2  **best motion detection yet, frame wrapped around object
    #cv2.TM_SQDIFF_NORMED threshold .99999-1 * frame is off and it produces many results
    #cv2.TM_CCOEFF threshold .05-1 *produces too many unuseable results

    loc = np.where(result >= .159)

    #these items were just test items for code.  I will replace later
    #frame = cv2.line(frame, (0, 0), (w, h), (255, 0, 0), 10)
    #frame = cv2.line(frame, (0, h), (w, 0), (0, 255, 0), 5)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #frame = cv2.putText(frame, 'CARLOS is Great!', (10, h - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)


    for pt in zip(*loc[::-1]):

        cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 3)

    cv2.imshow("Template Matching", frame)

    if(cv2.waitKey(5) & 0xFF == ord('q')):
        break



cap.release()
cv2.destroyAllWindows()