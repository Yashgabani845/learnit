import cv2
import numpy as np

# Load two images
image1 = cv2.imread('ab.jpg')  # Ensure both images are the same size
image2 = cv2.imread('abs.jpg')

# Resize images to the same size for the bitwise operations
image1 = cv2.resize(image1, (600, 400))
image2 = cv2.resize(image2, (600, 400))

# Create a mask (example: a white rectangle in a black image)
mask = np.zeros(image1.shape, dtype=np.uint8)
cv2.rectangle(mask, (150, 100), (450, 300), (255, 255, 255), -1)  # White rectangle mask

# Perform bitwise AND
bitwise_and = cv2.bitwise_and(image1, image2)

# Perform bitwise OR
bitwise_or = cv2.bitwise_or(image1, image2)

# Perform bitwise NOT on image1
bitwise_not = cv2.bitwise_not(image1)

# Perform bitwise XOR
bitwise_xor = cv2.bitwise_xor(image1, image2)

# Show all the results in windows
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise NOT", bitwise_not)
cv2.imshow("Bitwise XOR", bitwise_xor)

# Show the mask for demonstration
cv2.imshow("Mask", mask)

# Wait for key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
