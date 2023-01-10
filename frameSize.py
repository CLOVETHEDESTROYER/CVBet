import cv2

# Set up the video capture object
cap = cv2.VideoCapture(0)

# Get the width and height of the frame
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Print the size of the frame
print(f'Frame size: {width} x {height}')

# Release the video capture object
cap.release()
