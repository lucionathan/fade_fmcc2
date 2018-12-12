import cv2
import os

img = cv2.imread("bolsonaro.jpg", 1)
img2 = cv2.imread("lula.jpg", 1)

path = "../output"





for i in range(0, 11):
	add = img2*(i/float(10)) + img*(1-i/float(10))
	cv2.imwrite(os.path.join(path,'bolsolula' + str(i) +'.jpg') ,add)

