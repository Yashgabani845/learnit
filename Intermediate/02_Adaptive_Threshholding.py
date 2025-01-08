#Adaptive Thresholding is a more advanced form of image thresholding where the threshold value is determined dynamically for smaller regions of the image rather than using a global threshold value. This approach works well for images with varying lighting conditions.

# OpenCV provides two adaptive methods:

# Mean Thresholding: The threshold value is the mean of the neighborhood area minus a constant C.
# Gaussian Thresholding: The threshold value is a weighted sum (Gaussian-weighted) of the neighborhood area minus a constant C.


# simply blocks ma kare threshholding etle better result aape


import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('first.png', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Adaptive Mean Thresholding
adaptive_mean = cv2.adaptiveThreshold(blurred_image, 255, 
                                      cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 11, 2)

# Apply Adaptive Gaussian Thresholding
adaptive_gaussian = cv2.adaptiveThreshold(blurred_image, 255, 
                                          cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Adaptive Mean Thresholding", adaptive_mean)
cv2.imshow("Adaptive Gaussian Thresholding", adaptive_gaussian)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
