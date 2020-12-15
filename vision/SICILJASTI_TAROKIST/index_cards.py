import cv2
import numpy as np

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("Slike/") if isfile(join("Slike/", f))]
print(onlyfiles)

#(128, 72, 3)
#(100, 55, 3)
for filename in onlyfiles:
    im = cv2.imread("Slike/" + filename)
    b = im[:,:,0]
    print(np.sum(b))
    g = im[:,:,1]
    print(np.sum(g))
    r = im[:,:,2]
    print(np.sum(r))
    print(im.shape)
    cv2.imshow("Display", im)
    cv2.waitKey()