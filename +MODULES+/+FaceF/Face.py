import cv2

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2. VideoCapture(0)
while True:
    succes, image = cap.read()

    #image = cv2.imread("")
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(image_gray,1.1,19)
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255),2)

    cv2.imshow('rez', image)

    if cv2.waitKey(1)& 0xff == ord('q'):
        break

