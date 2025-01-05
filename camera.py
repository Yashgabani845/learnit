import cv2

# Open a video capture object (use 0 for the default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Set camera parameters (you can set the following parameters using cv2.CAP_PROP_)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the width of the frames
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the height of the frames
cap.set(cv2.CAP_PROP_BRIGHTNESS, 150)  # Set brightness (0 to 255)
cap.set(cv2.CAP_PROP_CONTRAST, 50)  # Set contrast (0 to 100)
cap.set(cv2.CAP_PROP_SATURATION, 60)  # Set saturation (0 to 100)
cap.set(cv2.CAP_PROP_GAIN, 0)  # Set gain (0 to 100)
cap.set(cv2.CAP_PROP_FPS, 30)  # Set frames per second (FPS)

# Capture and display frames
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame")
        break

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
