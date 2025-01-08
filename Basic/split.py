import cv2

# Read the image
image = cv2.imread('ab.jpg')

# Split the image into 3 channels (BGR)
blue_channel, green_channel, red_channel = cv2.split(image)

# Show individual channels
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()
