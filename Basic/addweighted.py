import cv2

# Read two images of the same size
image1 = cv2.imread('ab.jpg')
image2 = cv2.imread('abs.jpg')

# Blend the two images with different weights (alpha for image1, beta for image2)
blended_image = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

# Show the blended image
cv2.imshow('Blended Image', blended_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
