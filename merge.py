import cv2

# Read the image
image = cv2.imread('ab.jpg')

# Split the image into 3 channels (BGR)
blue_channel, green_channel, red_channel = cv2.split(image)

# Modify the channels (example: make the red channel all zeros)
red_channel[:] = 0

# Merge the channels back into a single image
modified_image = cv2.merge([blue_channel, green_channel, red_channel])

# Show the modified image
cv2.imshow('Modified Image', modified_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
