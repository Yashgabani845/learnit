import cv2
import datetime

# Open a video capture object (use 0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Capture and display frames
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Overlay the current time on the video frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, current_time, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the frame with the date and time
    cv2.imshow("Camera Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
