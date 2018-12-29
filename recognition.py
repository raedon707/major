import cv2
import numpy as np
import pymysql
from res.vars import host, port, user, passwd, db
import sheets
import datetime
import os

conn = pymysql.connect(host = host, port = port, user = user, passwd = passwd, db = db)
cur = conn.cursor()

def getProfile(IDs, path2):
    cur.execute("SELECT NAME FROM "+path2+" WHERE ENROLLMENT={}".format(IDs))
    name = cur.fetchone()
    return name

def start_recognition(path,path2):
    faceDetector = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(path+"trainingData.yml")
    IDs = 0
    font = cv2.FONT_HERSHEY_DUPLEX

    temp_file = open(path+str(datetime.datetime.now()).split()[0]+".csv", "wt")
    temp_file.write("enrollment,name,status\n")

    while True:
        ret, img = cam.read()
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetector.detectMultiScale(gray, 1.2, 3)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
            roi_gray = gray[y:y+h, x:x+w]
            IDs,conf = recognizer.predict(roi_gray)

            if(conf<60):
                profile=getProfile(IDs, path2)
                temp_file.write(str(IDs)+','+str(profile[0])+",p\n")
            else:
                IDs=0
                profile="unknown"
            if(profile!=None):
##                cv2.rectangle(im, (x-22,y-90), (x+w+80, y-22), (0,255,0), -1)
                cv2.putText(img, str(profile), (x,y+h), font, 1, (0,255,0), 2, cv2.LINE_AA)
        
##            if name is None:
##                name = "no face found"
##            cv2.putText(img, str(name), (x,y+h), font, 1, (0,255,0), 2, cv2.LINE_AA)
            #sheets.main(name, IDs)
            
        cv2.imshow("face", img)
        if(cv2.waitKey(1) == ord('q')):
            temp_file.close()
            seen = set()
            seen2 = set()
            with open(path+str(datetime.datetime.now()).split()[0]+".csv", 'r') as in_file, open(path+str(datetime.datetime.now()).split()[0]+"2.csv", 'w') as out_file:
                for line in in_file:
                    if line in seen:
                        continue
                    seen.add(line)
                    seen2.add(line.split(",")[0]+","+line.split(",")[1])
                    out_file.write(line)
            os.remove(path+str(datetime.datetime.now()).split()[0]+".csv")
            cur.execute("SELECT NAME,ENROLLMENT FROM "+path2)
            name = cur.fetchall()
            file = open(path+str(datetime.datetime.now()).split()[0]+"2.csv", "at")
            for data_line in name:
                for file_line in seen:
                    if file_line.split(",")[0] == data_line[1]:
                        continue
                    if (data_line[1]+","+data_line[0]) in seen2:
                        continue
                    seen2.add(data_line[1]+","+data_line[0])
                    file.write(data_line[1]+","+data_line[0]+",a\n")
            file.close()
            file = open(path+str(datetime.datetime.now()).split()[0]+"2.csv", "rt")
            print(file.read())
            file.close()
            conn.close()
            break
    cam.release()
    cv2.destroyAllWindows()
