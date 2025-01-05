import cv2

# Initialize global variables to store mouse event details
mouse_event = None
mouse_position = (0, 0)

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global mouse_event, mouse_position

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_event = "Left Button Down"
        mouse_position = (x, y)
        print(f"Left button pressed at ({x}, {y})")

    elif event == cv2.EVENT_RBUTTONDOWN:
        mouse_event = "Right Button Down"
        mouse_position = (x, y)
        print(f"Right button pressed at ({x}, {y})")

    elif event == cv2.EVENT_MBUTTONDOWN:
        mouse_event = "Middle Button Down"
        mouse_position = (x, y)
        print(f"Middle button pressed at ({x}, {y})")

    elif event == cv2.EVENT_MOUSEMOVE:
        mouse_event = "Mouse Move"
        mouse_position = (x, y)
        print(f"Mouse moved to ({x}, {y})")

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_event = "Left Button Up"
        print(f"Left button released at ({x}, {y})")

    elif event == cv2.EVENT_RBUTTONUP:
        mouse_event = "Right Button Up"
        print(f"Right button released at ({x}, {y})")

    elif event == cv2.EVENT_MBUTTONUP:
        mouse_event = "Middle Button Up"
        print(f"Middle button released at ({x}, {y})")

# Create a black image window
image = cv2.imread('hire.png')  # Or use np.zeros() for a blank image

# Set the mouse callback to the window
cv2.namedWindow("Mouse Event Window")
cv2.setMouseCallback("Mouse Event Window", mouse_callback)

while True:
    # Display the image with the mouse event information
    display_image = image.copy()

    # Display the current mouse event and position
    cv2.putText(display_image, f"Event: {mouse_event}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
    cv2.putText(display_image, f"Position: {mouse_position}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    # Show the image in a window
    cv2.imshow("Mouse Event Window", display_image)

    # Exit on pressing the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
