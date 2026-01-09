import cv2
import os
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces = []
labels = []
label_map = {}
label_id = 0

dataset_path = "dataset"

for person in os.listdir(dataset_path):
    label_map[label_id] = person
    person_path = os.path.join(dataset_path, person)

    for img in os.listdir(person_path):
        img_path = os.path.join(person_path, img)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        faces.append(image)
        labels.append(label_id)

    label_id += 1

recognizer.train(faces, np.array(labels))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in detected:
        face = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(face)
        name = label_map[label]

        cv2.putText(frame, name, (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow("Attendance Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
