import numpy as np
import cv2
import os

########## KNN CODE ############
def distance(v1, v2):
    # Euclidean Distance
    return np.sqrt(((v1 - v2) ** 2).sum())

def knn(train, test, k=5):
    dist = []

    for i in range(train.shape[0]):
        # Get the vector and label
        ix = train[i, :-1]
        iy = train[i, -1]
        # Compute the distance from the test point
        d = distance(test, ix)
        dist.append([d, iy])

    # Sort based on distance and get top k
    dk = sorted(dist, key=lambda x: x[0])[:k]
    # Retrieve only the labels
    labels = np.array(dk)[:, -1]

    # Get frequencies of each label
    output = np.unique(labels, return_counts=True)
    # Find the label with the maximum frequency
    index = np.argmax(output[1])
    return output[0][index]
################################

# Initialize webcam and Haar Cascade
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

dataset_path = "./face_dataset/"

face_data = []
labels = []
class_id = 0
names = {}

# Dataset preparation
for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        # Extract the name of the person from the filename
        names[class_id] = fx[:-4]  # Remove .npy extension
        data_item = np.load(dataset_path + fx, allow_pickle=True)

        face_data.append(data_item)

        # Create labels for the current class
        target = class_id * np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)

# Combine all face data and labels
face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

print("Face labels shape:", face_labels.shape)
print("Face dataset shape:", face_dataset.shape)

# Create the training dataset
trainset = np.concatenate((face_dataset, face_labels), axis=1)
print("Trainset shape:", trainset.shape)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for face in faces:
        x, y, w, h = face

        # Get the face ROI (Region of Interest)
        offset = 10
        face_section = frame[y-offset:y+h+offset, x-offset:x+w+offset]
        face_section = cv2.resize(face_section, (100, 100))

        # Flatten the face section and classify it
        try:
            out = knn(trainset, face_section.flatten())
            label = names[int(out)]
        except Exception as e:
            label = "Unknown"

        # Draw rectangle and label on the frame
        cv2.putText(frame, label, (x, y - 10), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

    cv2.imshow("Faces", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
