import cv2
import numpy as np

slike =  ["Ka1.bmp",
            "Ka2.bmp",
            "Ka3.bmp",
            "Ka4.bmp",
            "KaC.bmp",
            "KaD.bmp",
            "KaJ.bmp",
            "KaK.bmp",
            "Kr7.bmp",
            "Kr8.bmp",
            "Kr9.bmp",
            "Kr10.bmp",
            "KrC.bmp",
            "KrD.bmp",
            "KrJ.bmp",
            "KrK.bmp",
            "Pi7.bmp",
            "Pi8.bmp",
            "Pi9.bmp",
            "Pi10.bmp",
            "PiC.bmp",
            "PiD.bmp",
            "PiJ.bmp",
            "PiK.bmp",
            "Sr1.bmp",
            "Sr2.bmp",
            "Sr3.bmp",
            "Sr4.bmp",
            "SrC.bmp",
            "SrD.bmp",
            "SrJ.bmp",
            "SrK.bmp",
            "T1.bmp",
            "T2.bmp",
            "T3.bmp",
            "T4.bmp",
            "T5.bmp",
            "T6.bmp",
            "T7.bmp",
            "T8.bmp",
            "T9.bmp",
            "T10.bmp",
            "T11.bmp",
            "T12.bmp",
            "T13.bmp",
            "T14.bmp",
            "T15.bmp",
            "T16.bmp",
            "T17.bmp",
            "T18.bmp",
            "T19.bmp",
            "T20.bmp",
            "T21.bmp",
            "T22.bmp"]


for slika in slike:

    im = cv2.imread("Slike2/" + slika)

    h,w,c = im.shape

    h_half = h//2
    w_half = w//2
    im[h_half:h,:] = np.array([0,0,0])

    cv2.imwrite("Slike3/" + slika, im)

kriz = [[176.62771739,  98.69836957,  93.32880435],
[158.71487603,  99.29338843,  95.19834711],
]

karo = [[ 89.24022346,  86.84916201, 150.35195531],
            [ 82.85477178, 79.21161826, 173.26141079]]

pik = [[ 96.30851064, 164.54468085,  67.95531915]]

herc = [[ 63.7, 126.83673469, 218.77959184],
[ 52.66051661, 135.0295203, 255.0]]

tarok = []



