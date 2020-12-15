import pytesseract
import cv2
import numpy as np
import copy

def normalize(image):
    # Making sure, that there will be no division by 0
    image[image[:, :, :] == 0] = 1

    # Convert everything to float because we had an overflow issue and also if the type is int the division
    # we do later on is whole number division and so every result was 0
    image = np.array(image, np.float)

    # Store the individual color channels
    b = image[:, :, 0]
    g = image[:, :, 1]
    r = image[:, :, 2]

    # Add them together
    vsota = b + g + r

    # Normalize
    nb = np.divide(b, vsota)
    ng = np.divide(g, vsota)
    nr = np.divide(r, vsota)

    # Set up an empty matrix
    normalized = np.zeros((image.shape), np.float)

    # Store the values in the empty matrix
    normalized[:, :, 0] = np.multiply(nb, 255.0)
    normalized[:, :, 1] = np.multiply(ng, 255.0)
    normalized[:, :, 2] = np.multiply(nr, 255.0)

    # Return the matrix
    return np.array(normalized, np.uint8)




"""for i in range(h):
    for j in range(w):

        if (image[i][j] == np.array([120, 120, 120])).all():
            image[i][j] = np.array([255, 255, 255])

        #[215, 120, 0]
        if (image[i][j] == np.array([215, 120, 0])).all():
            image[i][j] = np.array([255, 255, 255])

        if (image[i][j] != np.array([255, 255, 255])).all():
            print(image[i][j])"""

#image = cv2.circle(image, (50, 21), 3, (0, 0, 0), 3)

def get_text(image):

    #add white line
    image[18:22,:] = np.array([255,255,255])

    #seperate the first one
    x = image[0:18,:]

    #remove the blue
    h,w,_ = x.shape
    for i in range(h):
        for j in range(w):
            if tuple(x[i][j]) == (215, 120, 0):
                x[i][j] = np.array([0,0,0])

    #convert to grayscale
    gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)


    #invert the colors white -> black and vice versa
    gray[gray == 0] = 1
    h,w = gray.shape
    for i in range(h):
        for j in range(w):
            if gray[i][j] == 1:
                gray[i][j] = 255
            else:
                gray[i][j] = 254 - gray[i][j]

    gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray2[0:18, :] = gray

    #cv2.imshow("Display", gray2)
    #cv2.waitKey()

    custom_config = r'--oem 3 --psm 6'
    g = pytesseract.image_to_string(gray2, config=custom_config)
    return g.split()






#(215, 120, 0)
"""for val in mnozica:
    pomozni = copy.deepcopy(x)

    for i in range(h):
        for j in range(w):
            if (pomozni[i][j] == np.array(val)).all():
                pomozni[i][j] = np.array([0, 0, 0])
    print(val)
    
    cv2.imshow("Display", pomozni)
    cv2.waitKey()


cv2.imshow("Display", x)
cv2.waitKey()
print(image.shape)
cv2.imshow("Display", image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#135 x 120
#120 visoko
#135 siroko
gray[0:18,:] = gray1
#image = normalize(image)
cv2.imshow("Display", gray)
cv2.waitKey()

cv2.imshow("Display", gray)
cv2.waitKey()

custom_config = r'--oem 3 --psm 6'
g = pytesseract.image_to_string(gray, config=custom_config)
print(g.split())"""

image = cv2.imread("testocr.png")
h, w, _ = image.shape

a  = get_text(image)
print(a)