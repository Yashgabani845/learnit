import cv2

# Load the image
image = cv2.imread('ab.jpg')

# Check if the image is loaded
if image is None:
    print("Error: Could not load the image.")
    exit()

# 1. Gaussian Pyramid (Downsampling)
gaussian_down1 = cv2.pyrDown(image)  # First level downsampling
gaussian_down2 = cv2.pyrDown(gaussian_down1)  # Second level downsampling

# 2. Gaussian Pyramid (Upsampling)
gaussian_up = cv2.pyrUp(gaussian_down2)  # Upsampling

# 3. Laplacian Pyramid
# Laplacian = Original Image - Upsampled Gaussian
laplacian = cv2.subtract(gaussian_down1, cv2.pyrUp(gaussian_down2))

# Display Images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Down Level 1", gaussian_down1)
cv2.imshow("Gaussian Down Level 2", gaussian_down2)
cv2.imshow("Gaussian Up", gaussian_up)
cv2.imshow("Laplacian", laplacian)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
