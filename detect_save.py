import cv2, sys, os, glob
from PIL import Image as img

imagePath = "img/"+sys.argv[1]
cascPath = "data_t/haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

im = img.open(imagePath)
px,py = im.size

if (px>1000 or py>1000):
	im = im.resize((800,600), img.ANTIALIAS)
	im.save("img/"+sys.argv[1],"JPEG")


image = cv2.imread(imagePath)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print "Found {0} people".format(len(faces))




print "Image Resolution:"+ str(px)+"x"+ str(py)
i=1
try:
	for (x, y, w, h) in faces:
		im.crop((x-10,y-25,x+w+10,y+h+10)).save("scan/person"+str(i)+".jpg","JPEG")
		i+=1
except Exception as e:
	print "Unable to crop: "+str(e)
	
	
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x-10, y-25), (x+w+10, y+h+10), (255, 90, 80), 2)

print faces

cv2.imshow("Faces Found: "+str(len(faces)),image)

cv2.waitKey(0)