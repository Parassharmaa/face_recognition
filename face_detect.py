import cv2
import sys


imagePath = "img/"+sys.argv[1]
cascPath = "data_t/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print "Found {0} people".format(len(faces))


for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (145, 55, 30), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
