import cv2
import numpy as np

# Initialize the webcam (0 for default webcam)
cap = cv2.VideoCapture(0)

# Define the HSV range for detecting a specific color (example: red color)
# These values can be changed based on the color you want to track
lower_bound = np.array([0, 120, 70])  # Lower bound of HSV range for red
upper_bound = np.array([10, 255, 255])  # Upper bound of HSV range for red

# Or define other ranges if you want to track a different color
# Example for green: lower_bound = np.array([35, 100, 100]), upper_bound = np.array([85, 255, 255])

while True:
    # Capture frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame from BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask based on the defined HSV color range
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # Perform bitwise AND operation to extract the object of interest from the frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, draw a bounding box around the largest contour
    if contours:
        # Sort contours based on area and get the largest one
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the bounding box of the largest contour
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Draw a rectangle around the object
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Optionally, draw the center of the object
        center = (x + w // 2, y + h // 2)
        cv2.circle(frame, center, 5, (0, 0, 255), -1)

    # Show the original frame with the bounding box
    cv2.imshow('Original Frame', frame)

    # Show the result (masked frame showing only the object of interest)
    cv2.imshow('Mask', result)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
