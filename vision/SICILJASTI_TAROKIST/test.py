import cv2
import numpy as np
import os
import time
from TarockBasics import *
from GameStateTarock import *
from os import listdir
from os.path import isfile, join
import pyautogui
import pickle
import os

onlyfiles = [f for f in listdir("pictures/") if isfile(join("pictures/", f))]
onlyfiles = [f for f in onlyfiles if ".png" not in f]

#https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/


def compare_images(im1, im2):
    h,w, d = im1.shape
    for i in range(h):
        for j in range(w):
            b1, g1, r1 = im1[i][j]
            b2, g2, r2 = im2[i][j]
            if b1 != b2 or g1 != g2 or r1 != r2:
                return False
    return True

def compare_images2(im1, sum_images):
    best_fit = None
    diff = 100000000
    vsota = np.sum(im1)

    for key in sum_images:
        if np.abs(vsota - sum_images[key]) < diff:
            diff = np.abs(vsota - sum_images[key])
            best_fit = key

    return best_fit

def cos_sim(vA, vB):
    cos = np.dot(vA, vB) / (np.sqrt(np.dot(vA, vA)) * np.sqrt(np.dot(vB, vB)))
    return cos

def compare_images3(im1, database):
    b1 = im1[:,:,0]
    g1 = im1[:, :, 1]
    r1 = im1[:, :, 2]
    b1 = np.squeeze(np.asarray(cv2.calcHist([b1], [0], None, [256], [0, 256])))
    g1 = np.squeeze(np.asarray(cv2.calcHist([g1], [0], None, [256], [0, 256])))
    r1 = np.squeeze(np.asarray(cv2.calcHist([r1], [0], None, [256], [0, 256])))

    best_fit = None
    best_sim = 0
    #
    for key in database:
        im2 = database[key]
        b2 = im2[:, :, 0]
        g2 = im2[:, :, 1]
        r2 = im2[:, :, 2]
        b2 = np.squeeze(np.asarray(cv2.calcHist([b2], [0], None, [256], [0, 256])))
        g2 = np.squeeze(np.asarray(cv2.calcHist([g2], [0], None, [256], [0, 256])))
        r2 = np.squeeze(np.asarray(cv2.calcHist([r2], [0], None, [256], [0, 256])))

        sim_b = cos_sim(b1, b2)
        sim_g = cos_sim(g1, g2)
        sim_r = cos_sim(r1, r2)

        current_sum_sim = sim_b + sim_g + sim_r




    return list(reversed(sorted(fit, key=lambda x: x[1])))

path = r"C:\Users\User\Desktop\Magistrska\TarockMasters\vision\SICILJASTI_TAROKIST\Tarok.exe"
os.startfile(path)
time.sleep(1)

im1 = pyautogui.screenshot()
image = np.array(im1)[...,::-1]

image = cv2.rectangle(image, (350,141), (450,161), (0,0,255), 2)
image = cv2.rectangle(image, (350,341), (450,361), (0,0,255), 2)
image = cv2.rectangle(image, (350,541), (450,561), (0,0,255), 2)

image = cv2.rectangle(image, (1482,200), (1555,330), (255,0,0), 2)
image = cv2.rectangle(image, (1482,400), (1555,530), (255,0,0), 2)
image = cv2.rectangle(image, (1482,600), (1555,730), (255,0,0), 2)

#cv2.imshow("display", image)
#cv2.waitKey()
print(pyautogui.size())

time.sleep(2)
#400, 950 = Nova igra
#840, 720 = Potrdi novo igro
#500, 950 = Naprej

pyautogui.click(400, 950)
time.sleep(1)
pyautogui.click(840, 720)
time.sleep(1)
pyautogui.click(500, 950)
time.sleep(1)
#pyautogui.click(500, 950)


time.sleep(1)

im1 = pyautogui.screenshot()
image = np.array(np.array(im1)[...,::-1])

#sirina crne podloge = 72
#visina crne podloge = 128
#un gap = 8

starting_x = 1483
ending_x = 1555
top_y = 201
bot_y = 329

starting_x -= 8 + 72 #gap + sirina karte
ending_x -= 8 + 72

im1 = pyautogui.screenshot()
image = np.array(im1)[...,::-1]

hand = []

loaded_images = dict()
for pic in onlyfiles:
    key = int(pic.split(".")[0])
    loaded_images[key] = pickle.load(open("pictures/" + pic, "rb"))

hand = []
all_card_dists = []
for i in range(16):
    x = image[top_y:bot_y,starting_x:ending_x]
    #cv2.imwrite(str(i) + "x.png", x)
    #pickle.dump(x, open(str(i) + "x.pickle", "wb"))

    card_dist = compare_images3(x, loaded_images)

    all_card_dists.append(card_dist)


    starting_x -= 70  #sirina karte
    ending_x -= 70

possible_cards = list(loaded_images.keys())
first_choices = [x[0][0] for x in all_card_dists]
if len(first_choices) == len(set(first_choices)):
    hand = possible_cards
else:
    print(4)
tb = TarockBasics()
tb.print_hand(hand)

