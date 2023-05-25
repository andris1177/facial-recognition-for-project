import threading
import cv2
import os
from deepface import DeepFace
import donloadimage


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

counter = 0
face_match = False
dataset_path = "dataset"

def check_face(frame, reference_img, file_name):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img)['verified']:
            face_match = True
            print("Match found:", file_name)

        else:
            face_match = False

    except ValueError:
        face_match = False
        

def recognize_faces():
    for file_name in os.listdir(dataset_path):
        if file_name.endswith(".jpg"):
            reference_img = cv2.imread(os.path.join(dataset_path, file_name))
            threading.Thread(target=check_face, args=(frame.copy(), reference_img.copy(), file_name)).start()


while True:
    ret, frame = cap.read()
    
    if ret:
        if counter % 30 == 0:
            threading.Thread(target=recognize_faces).start()

        counter += 1

        if face_match:
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
