import cv2
import pyautogui

time_elapse = 200

def press_space():
    pyautogui.press('space')
    #pressed spacebar for pausing or resuming

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#palm_cascade = cv2.CascadeClassifier('palm.xml')

cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, img = cap.read()

    if ret == False:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 6)


    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            if(count>time_elapse):
                #Face detected again, resume
                press_space()
            count = 0
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
    if faces is ():
        count += 1
        if count == time_elapse:
            #'time_elapse' frames counted without face with eyes, pause player
            press_space()
    cv2.imshow('img',img)

    if cv2.waitKey(30) & 0xff == 27:
        break

cap.release()

cv2.destroyAllWindows()
