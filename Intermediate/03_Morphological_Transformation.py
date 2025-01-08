
# Morphological transformations are image processing techniques based on the shape or structure of an image. They are typically applied to binary images and are useful for tasks like removing noise, filling gaps, extracting features, and enhancing object structures.

# OpenCV provides the following basic morphological operations:

# Erosion
# Dilation
# Opening (Erosion followed by Dilation)
# Closing (Dilation followed by Erosion)
# Morphological Gradient
# Top Hat
# Black Hat
#used to remove noise

import cv2
import numpy as np

# Load the image
image = cv2.imread('abs.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# Apply binary thresholding to create a binary image
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Perform Morphological Operations
erosion = cv2.erode(binary_image, kernel, iterations=1)  # Erosion - noise remove kari image chuti padi de(shrinking)
dilation = cv2.dilate(binary_image, kernel, iterations=1)  # Dilation - empty pixcels bhari de(growing)
opening = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)  # Opening pela erosion pachi dialation 
closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)  # Closing pela dialation pachi erosion
gradient = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)  # Morphological Gradient Difference between Dilation and Erosion.
tophat = cv2.morphologyEx(binary_image, cv2.MORPH_TOPHAT, kernel)  # Top Hat Difference between the original image and its opening.
blackhat = cv2.morphologyEx(binary_image, cv2.MORPH_BLACKHAT, kernel)  # Black Hat  Difference between the closing of the image and the original image.

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary_image)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Morphological Gradient", gradient)
cv2.imshow("Top Hat", tophat)
cv2.imshow("Black Hat", blackhat)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
