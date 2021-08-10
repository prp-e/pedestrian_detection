import cv2 


classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
image = cv2.imread("pedestrian1.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
pedestrians = classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

for x,y,w,h in pedestrians:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow("HUD", image)
cv2.waitKey(0)