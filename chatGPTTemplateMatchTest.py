import cv2
import numpy as np

# Load the image you want to detect
template = cv2.imread('openCV_project/assets/doubleDots2.png', cv2.IMREAD_GRAYSCALE)

# Set up the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was not grabbed, break
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Define the two detection regions
    #left = gray[300:50, 600:0]
    #right = gray[980:0, 680:50]
    left = gray[0:200, 0:200]
    right = gray[100:200, 100:0]

    # Detect the image in each region
    result1 = cv2.matchTemplate(left, template, cv2.TM_CCOEFF_NORMED)
    result2 = cv2.matchTemplate(right, template, cv2.TM_CCOEFF_NORMED)

    # Find the maximum value in each region
    _, max_val1, _, _ = cv2.minMaxLoc(result1)
    _, max_val2, _, _ = cv2.minMaxLoc(result2)

    # If the image was detected in region 1, draw a rectangle around it
    if max_val1 > 0.5:
        cv2.rectangle(frame, (0, 0), (200, 200), (0, 255, 0), 2)
    # If the image was detected in region 2, draw a rectangle around it
    if max_val2 > 0.5:
        cv2.rectangle(frame, (1280, 200), (1080, 0), (0, 255, 0), 2)

    # If the image was detected in region 1, return "Region 1"
    if max_val1 > 0.5:
        print("LEFT SIDE WINS")
        #break #This will just shut the screen off.
                ##Consider putting a return that leads to a victory screen on the smart contract DAPP.
    # If the image was detected in region 2, return "Region 2"
    elif max_val2 > 0.5:
        print("RIGHT SIDE WINS")
        break
    # If the image was not detected in either region, return "Not found"
    else:
        print("Not found")
   
    
    # Show the frame
    cv2.imshow('Frame', frame)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27:  # Escape key
        break

# Release the video capture object
cap.release()

# Close all windows
cv2.destroyAllWindows()
