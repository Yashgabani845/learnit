import cv2
import numpy as np

# Load the image
image = cv2.imread('ab.jpg')

# Check if the image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# 1. Averaging (Mean Filtering)
average_blur = cv2.blur(image, (5, 5))  # Kernel size is (5, 5)

# 2. Gaussian Blurring
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)  # Kernel size (5, 5), sigma=0

# 3. Median Blurring
median_blur = cv2.medianBlur(image, 5)  # Kernel size must be odd (e.g., 3, 5, 7)

# 4. Bilateral Filtering
bilateral_blur = cv2.bilateralFilter(image, 9, 75, 75)  # Diameter, sigmaColor, sigmaSpace

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Averaging Blur", average_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Blur", bilateral_blur)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()


# Averaging (Mean Filtering)
# Takes the average of all the pixel intensities under the kernel area.
# Gaussian Blurring
# Uses a Gaussian kernel for weighted averaging. It provides a smoother and more natural blur.
# Median Blurring
# Replaces each pixel's intensity with the median of the intensities in its neighborhood. Effective for removing salt-and-pepper noise.
# Bilateral Filtering
# Preserves edges while blurring the rest of the image.