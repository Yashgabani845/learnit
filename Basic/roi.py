import cv2

# Read the image
image = cv2.imread('ab.jpg')

# Define the coordinates of the top-left and bottom-right corners of the ROI
x, y, w, h = 100, 100, 200, 200  # Example: (x, y) is top-left, (w, h) is width and height

# Extract the ROI
roi = image[y:y+h, x:x+w]

# Show the extracted ROI
cv2.imshow('Region of Interest', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
