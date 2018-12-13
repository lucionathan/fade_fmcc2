import cv2
import os
import numpy
from itertools import cycle

img = cv2.imread("../input/gandalf.jpg", 1)
img2 = cv2.imread("../input/gandalfrosa.jpeg", 1)

img2 = cv2.resize(img2, (480, 535))
output = list()

path = "../output"
# Manipulacao:
for i in range(0, 11):
    add = img2*(i/float(10)) + img*(1-i/float(10))

    cv2.imwrite(os.path.join(path, 'output' + str(i) + '.jpg'), add)

    output.append(path + '/' + 'output' + str(i) + '.jpg')

# Resultado:

for actual in cycle(output):
    tmp = cv2.imread(actual, 1)

    k = cv2.waitKey(1000)
    # aperte ESC para fechar
    if k == 27:
        cv2.destroyAllWindows()
        break
