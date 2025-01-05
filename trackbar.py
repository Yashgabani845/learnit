import cv2

# Callback function that does nothing
def nothing(x):
    pass

# Read the image
image = cv2.imread('abs.jpg')

# Create a window
cv2.namedWindow("Image")

# Create two trackbars: one for brightness, one for contrast
cv2.createTrackbar("Brightness", "Image", 50, 100, nothing)
cv2.createTrackbar("Contrast", "Image", 50, 100, nothing)

while True:
    # Get the current position of the trackbars
    brightness = cv2.getTrackbarPos("Brightness", "Image")
    contrast = cv2.getTrackbarPos("Contrast", "Image")

    # Adjust the brightness and contrast
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast/50, beta=brightness-50)

    # Display the adjusted image
    cv2.imshow("Image", adjusted_image)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press 'q' to quit
        break

# Close all windows
cv2.destroyAllWindows()
