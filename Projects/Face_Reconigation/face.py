import cv2

# Load the Haar Cascade XML file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
image = cv2.imread('abs.jpg')

# Convert the image to grayscale (Haar Cascades work on grayscale images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(
    gray, 
    scaleFactor=1.1, 
    minNeighbors=5, 
    minSize=(30, 30)
)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Face Detection', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
