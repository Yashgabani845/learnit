import cv2
import numpy as np

# Load the image
image = cv2.imread('ab.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# 1. Sobel Gradients
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Gradient in X direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Gradient in Y direction
sobel_combined = cv2.magnitude(sobel_x, sobel_y)  # Combine gradients

# Convert Sobel results to uint8
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
sobel_combined = cv2.convertScaleAbs(sobel_combined)

# 2. Scharr Gradients (better accuracy than Sobel for small details)
scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharr_combined = cv2.magnitude(scharr_x, scharr_y)

# Convert Scharr results to uint8
scharr_x = cv2.convertScaleAbs(scharr_x)
scharr_y = cv2.convertScaleAbs(scharr_y)
scharr_combined = cv2.convertScaleAbs(scharr_combined)

# 3. Laplacian Gradient
laplacian = cv2.Laplacian(image, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

# 4. Canny Edge Detection
edges = cv2.Canny(image, 100, 200)  # Thresholds: 100 (low), 200 (high)

# Display Results
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.imshow("Scharr X", scharr_x)
cv2.imshow("Scharr Y", scharr_y)
cv2.imshow("Scharr Combined", scharr_combined)
cv2.imshow("Laplacian", laplacian)
cv2.imshow("Canny Edges", edges)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
