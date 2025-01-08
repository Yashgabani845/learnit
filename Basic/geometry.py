import cv2
import numpy as np

# Create a blank image (black background)
image = np.zeros((500, 500, 3), dtype="uint8")

# Draw a rectangle (x, y, width, height) - Blue color (BGR), thickness 2
cv2.rectangle(image, (50, 50), (450, 450), (255, 0, 0), 2)

# Draw a circle (center, radius) - Green color, thickness -1 for filled circle
cv2.circle(image, (250, 250), 100, (0, 255, 0), -1)

# Draw a line (start point, end point) - Red color, thickness 3
cv2.line(image, (50, 50), (450, 450), (0, 0, 255), 3)

# Draw a polygon (vertices) - Yellow color, thickness 2
points = np.array([[50, 450], [250, 50], [450, 450]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(image, [points], isClosed=True, color=(0, 255, 255), thickness=2)

# Show the image with the shapes drawn
cv2.imshow("Geometric Shapes", image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
