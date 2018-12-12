import cv2
import os
import numpy

img = cv2.imread("../input/gandalf.jpg", 1)
img2 = cv2.imread("../input/gandalfrosa.jpeg", 1)

img2 = cv2.resize(img2, (480, 535))

path = "../output"

for i in range(0, 11):
    add = img2*(i/float(10)) + img*(1-i/float(10))

    cv2.imshow("actual", add)
    cv2.waitKey(0)

    cv2.imwrite(os.path.join(path, 'output' + str(i) + '.jpg'), add)
    cv2.destroyAllWindows
