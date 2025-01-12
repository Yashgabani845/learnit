import cv2
import numpy as np

# Open video file
cap = cv2.VideoCapture('a.mp4')

# Read the first two frames
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Calculate the absolute difference between the two frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to smooth the image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding to highlight changes
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around detected motion
    for contour in contours:
        if cv2.contourArea(contour) < 1000:  # Ignore small contours to reduce noise
            continue

        # Get the bounding box coordinates for the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Draw a rectangle on the original frame
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Motion Detection", frame1)

    # Update frames for the next iteration
    frame1 = frame2
    ret, frame2 = cap.read()

    # Break the loop if ESC key is pressed or video ends
    if not ret or cv2.waitKey(40) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
