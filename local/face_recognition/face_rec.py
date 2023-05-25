import face_recognition
import os
import cv2

# létrehoz két listát
known_faces = []
known_names = []

# végigmegy a megadott mappában lévő fájlokon
# és a neveiket belerakja a known_names be
# a képből létrehoz egy arclenyomatot
for filename in os.listdir('../web/adminSite/takePicture/images/'):
    image = face_recognition.load_image_file(f'../web/adminSite/takePicture/images/{filename}')
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]
        known_faces.append(face_encoding)
        known_names.append(os.path.splitext(filename)[0])
    else:
        # handle the case where no face was found in the image
        print(f"No face found in {filename}")
        continue

# inicializálja a kamerát
video_capture = cv2.VideoCapture(0)

while True:
    # minden ciklusnál az aktuális képkoclát hasuználja
    ret, frame = video_capture.read()

    # átalakítja a BGR képet RGB-vé
    rgb_frame = frame[:, :, ::-1]

    # meghatározza az arc helyét
    face_locations = face_recognition.face_locations(rgb_frame)
    # elkészíti az arclenyomatot
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # összehasonlítja a mostani arclenyomatot az ism,ert arclenyomattal 
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        # ha nem ismeri akkor a név Unknown
        name = "Unknown"

        # ha igen akkor beállítja a nevet az eggyező arcéra
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # megjelenít egy négyzetet az arc köré és odaírja a nevet
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
