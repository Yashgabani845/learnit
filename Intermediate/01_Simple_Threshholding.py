#Image thresholding is a technique used to segment an image by converting it into a binary image (black and white) based on a threshold value. OpenCV provides the cv2.threshold function for simple image thresholding.
# black and white image banavvani technique

import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('ab.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# Apply different types of thresholding
# 1. Binary Thresholding
_, binary_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 2. Binary Inverse Thresholding
_, binary_inv_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# 3. Truncate Thresholding
_, trunc_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)

# 4. To Zero Thresholding
_, tozero_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO)

# 5. To Zero Inverse Thresholding
_, tozero_inv_thresh = cv2.threshold(image, 127, 255, cv2.THRESH_TOZERO_INV)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Binary Thresholding", binary_thresh)
cv2.imshow("Binary Inverse Thresholding", binary_inv_thresh)
cv2.imshow("Truncate Thresholding", trunc_thresh)
cv2.imshow("To Zero Thresholding", tozero_thresh)
cv2.imshow("To Zero Inverse Thresholding", tozero_inv_thresh)

# Wait until a key is pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
