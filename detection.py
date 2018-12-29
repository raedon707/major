import cv2
import numpy as np
import os

def start_detection(name, year, section, user_id, branch):
    face_cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('cascade/haarcascade_eye.xml')
    face_samples = 40
    sample_number = 0

    path = "dataset/"+str(branch)+"/"+str(year)+"/"+str(section)
    if not os.path.exists(path):
        os.makedirs(path)
    
    cap = cv2.VideoCapture(0)
    while True:
        rec, img = cap.read()
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            cv2.imwrite(path+"/"+str(name)+"."+str(user_id)+"."+str(sample_number)+".jpg", roi_gray)
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            roi_color = img[y:y+h, x:x+w]
            sample_number += 1
            cv2.waitKey(100);
        cv2.imshow('img',img);
        cv2.waitKey(1);
        print (sample_number)
        k = cv2.waitKey(30) & 0xff
        if sample_number > face_samples:
            break
    cap.release()
    cv2.destroyAllWindows()


