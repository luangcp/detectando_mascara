
# Importando bibliotecas
import numpy as np
import time

import cv2
from cv2.cv2 import CascadeClassifier

video = cv2.VideoCapture(0)


face_cascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')  # file to classifier the face
nariz_cascade = cv2.CascadeClassifier(
    'haarcascade_mcs_nose.xml')  # file to classifier the nose
mouth_cascade = cv2.CascadeClassifier(
    'haarcascade_mcs_mouth.xml')  # file to classifier the mouth
# eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml') #file to classifier the face

timemouth_bad = time.time()
timenos_bad = time.time()
timenos_ok = time.time()
timemouth_ok = time.time()
aux = 0
nos_ = 0
mouth_ = 0
while True:
    conected, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Turn the cam gray
    # faces variable receives the return of classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


#    time_count=time.now()

    for (x, y, w, h) in faces:  # X and Y are the coordinates of the begginer of face; W is the width of face and H is the height
        # time.sleep(0.5)

        # This instruction forms the rectagle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # x,y are the coordinates of begginer;  x+w = Total Width; y+h = Total Height; (255,0,0) in order blue, green, red - in this case will be blue; 2= thickness contour of rectangle

        roi_gray = gray[y:y+h, x:x+w]  # show only face in a gray boxe
        roi_color = frame[y:y + h, x:x + w]

        nariz = nariz_cascade.detectMultiScale(roi_gray, 1.3, 5)
        mouth = mouth_cascade.detectMultiScale(roi_gray, 1.3, 5)
       # eye = eye_cascade.detectMultiScale(roi_gray)

        if (nos_ == 0 and mouth_ == 0 and time.time() - timemouth_bad > 5 and time.time() - timenos_bad > 5):
            if (aux == 0):
                timenos_ok = time.time()
                timemouth_ok = time.time()
            else:
                timenos_ok = timenos_ok
                timemouth_ok = timenos_ok
            print('ok', time.time() - timemouth_bad,
                  time.time() - timenos_bad, nos_, mouth_)
        aux = 0
        nos_ = 0
        mouth_ = 0
        for(nx, ny, nw, nh) in nariz:  # ex and ey are the coordinates of the begginer of eyes; ew is the width of face and eh is the height of eye
            cv2.rectangle(roi_color, (nx, ny),
                          (nx + nw, ny + nh), (0, 255, 0), 2)

            aux = 1
            if (time.time() - timenos_ok > 5):
                nos_ = 1
                timenos_bad = time.time()
            else:
                if (aux == 0):
                    nos_ = 0
        print(aux, nos_)

        for (mx, my, mw, mh) in mouth:  # ex and ey are the coordinates of the begginer of eyes; ew is the width of face and eh is the height of eye
            cv2.rectangle(roi_color, (mx, my),
                          (mx + mw, my + mh), (255, 0, 0), 2)

            aux = 1
            if(time.time()-timemouth_ok > 5):
                mouth_ = 1
                timemouth_bad = time.time()
            else:
                if (aux == 0):
                    mouth_ = 0
        print(aux, mouth_)

        if (nos_ != 0 or mouth_ != 0):
            print('você está usando a máscara de maneira incorreta',
                  time.time() - timemouth_ok, time.time() - timenos_ok)

        # for (ex, ey, ew,eh) in eye:  # ex and ey are the coordinates of the begginer of eyes; ew is the width of face and eh is the height of eye
        #    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

        cv2.imshow("roi_gray", roi_gray)  # show only the face

    cv2.imshow('Video', frame)

  #  print(nose_time)

    # print(time_count)
    k = cv2.waitKey(1)
    if k == ord('q'):  # when press 'q', turn off the video
        break

video.release()
cv2.destroyAllWindows()

del faces
del nose
del nose_

del mouth_
del face_cascade
del mouth_cascade
del nose_cascade
