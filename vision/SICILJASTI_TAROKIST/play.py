import pyautogui
import numpy as np
import cv2
import pickle
import os
import time
import pytesseract
from TarockBasics import *

class Play:

    def __init__(self):
        self.card_templates = dict()
        self.starting_x = 1483
        self.ending_x = 1555
        self.top_y = 201
        self.bot_y = 329
        self.discard = {}
        self.player1_top_left = (350, 141)
        self.player1_bot_right = (450, 161)
        self.game_coords = [(900, 495), (900, 515), (900, 535), (900, 555), (900, 575), (900, 595)]
    # 400, 950 = Nova igra
    # 840, 720 = Potrdi novo igro
    # 500, 950 = Naprej

    def load_tempaltes(self):
        for pic in ['1.pickle', '11.pickle', '12.pickle', '13.pickle', '14.pickle', '15.pickle', '16.pickle', '17.pickle', '18.pickle', '2.pickle', '21.pickle', '22.pickle', '23.pickle', '24.pickle', '25.pickle', '26.pickle', '27.pickle', '28.pickle', '3.pickle', '31.pickle', '32.pickle', '33.pickle', '34.pickle', '35.pickle', '36.pickle', '37.pickle', '38.pickle', '4.pickle', '40.pickle', '41.pickle', '42.pickle', '43.pickle', '44.pickle', '45.pickle', '46.pickle', '47.pickle', '48.pickle', '49.pickle', '5.pickle', '50.pickle', '51.pickle', '52.pickle', '53.pickle', '54.pickle', '55.pickle', '56.pickle', '57.pickle', '58.pickle', '59.pickle', '6.pickle', '60.pickle', '61.pickle', '7.pickle', '8.pickle']:
            key = int(pic.split(".")[0])
            self.card_templates[key] = pickle.load(open("pictures/" + pic, "rb"))

    def start_game(self):
        path = r"C:\Users\User\Desktop\Magistrska\TarockMasters\vision\SICILJASTI_TAROKIST\Tarok.exe"
        os.startfile(path)
        time.sleep(1)


    def press_X(self):
        time.sleep(0.5)
        pyautogui.click(1540, 120)
        time.sleep(0.5)

    def press_uncheck_pocakaj(self):
        time.sleep(0.5)
        pyautogui.click(715, 675)
        time.sleep(0.5)

    def press_check_pokazi_talon(self):
        time.sleep(0.5)
        pyautogui.click(725, 630)
        time.sleep(0.5)

    def press_nova_igra(self):
        time.sleep(0.5)
        pyautogui.click(400, 950)
        time.sleep(0.5)

    def press_potrdi_novo_igro(self):
        time.sleep(0.5)
        pyautogui.click(840, 720)
        time.sleep(0.5)

    def press_naprej(self):
        time.sleep(0.5)
        pyautogui.click(500, 950)
        time.sleep(0.5)

    def press_licitacija_potrdi(self):
        time.sleep(0.5)
        pyautogui.click(900, 630)
        time.sleep(0.5)

    def press_licitacija_naprej(self):
        time.sleep(0.5)
        pyautogui.click(980, 630)
        time.sleep(0.5)

    def press_licitacija_X(self):
        time.sleep(0.5)
        pyautogui.click(1025, 435)
        time.sleep(0.5)

    def get_licitacija_image(self):
        image = self.get_screenshot()
        image = image[485:605, 880:1015]
        return image

    def get_talon_cards(self):
        image = self.get_screenshot()

        im = image[800:930,355:775]

        c1 = im[:, 0:70]
        c2 = im[:, 70:140]
        c3 = im[:, 140:210]
        c4 = im[:, 210:280]
        c5 = im[:, 280:350]
        c6 = im[:, 350:420]

        fits = [self.match_card_histograms(c1),
                self.match_card_histograms(c2),
                self.match_card_histograms(c3),
                self.match_card_histograms(c4),
                self.match_card_histograms(c5),
                self.match_card_histograms(c6)]

        viable = [x[0][0] for x in fits]
        if len(viable) == len(set(viable)):
            return viable
        else:
            for i in range(len(viable)):
                for j in range(len(viable)):
                    if viable[i] == viable[j] and i != j:
                        i_score = fits[i][0][1]
                        j_score = fits[j][0][1]

                        if i_score > j_score:
                            viable[j] = fits[j][1][0]

                        if j_score > i_score:
                            viable[i] = fits[i][1][0]

            return viable


    def press_licitacija_solo(self):
        image = self.get_licitacija_image()
        igre = self.get_text(image)

        index = None

        for i in range(len(igre)):
            if "solo" in igre[i].lower():
                index = i
                break

        time.sleep(0.5)
        x, y = self.game_coords[index]
        pyautogui.click(x, y)
        time.sleep(0.5)

    def get_vrstni_red(self):
        image = self.get_screenshot()
        vrstni_red = image[170:190, 872:897]
        grey = cv2.cvtColor(vrstni_red, cv2.COLOR_BGR2GRAY)
        grey2 = copy.deepcopy(grey)

        grey2[grey2 > 200] = 254
        grey2[grey2 <= 200] = 0
        if not 0 in grey2:
            return None
        else:
            custom_config = r'--oem 3 --psm 6'
            g = pytesseract.image_to_string(grey, config=custom_config)
            return int(g.split()[0])


    def press_talon_potrdi(self):
        time.sleep(0.5)
        pyautogui.click(840, 765)
        time.sleep(0.5)

    def get_screenshot(self):
        im1 = pyautogui.screenshot()
        image = np.array(im1)[..., ::-1]
        return image

    def get_hand_images(self, image):
        self.starting_x -= 8 + 72  # gap + sirina karte
        self.ending_x -= 8 + 72
        hand_images = []
        for i in range(16):
            x = image[self.top_y:self.bot_y, self.starting_x:self.ending_x]

            self.starting_x -= 70
            self.ending_x -= 70
            hand_images.append(x)

        return hand_images

    def cos_sim(self, vA, vB):
        cos = np.dot(vA, vB) / (np.sqrt(np.dot(vA, vA)) * np.sqrt(np.dot(vB, vB)))
        return cos

    def match_card_histograms(self, im1):
        b1 = im1[:, :, 0]
        g1 = im1[:, :, 1]
        r1 = im1[:, :, 2]
        b1 = np.squeeze(np.asarray(cv2.calcHist([b1], [0], None, [256], [0, 256])))
        g1 = np.squeeze(np.asarray(cv2.calcHist([g1], [0], None, [256], [0, 256])))
        r1 = np.squeeze(np.asarray(cv2.calcHist([r1], [0], None, [256], [0, 256])))

        fit = []
        #
        for key in self.card_templates:
            im2 = self.card_templates[key]
            b2 = im2[:, :, 0]
            g2 = im2[:, :, 1]
            r2 = im2[:, :, 2]
            b2 = np.squeeze(np.asarray(cv2.calcHist([b2], [0], None, [256], [0, 256])))
            g2 = np.squeeze(np.asarray(cv2.calcHist([g2], [0], None, [256], [0, 256])))
            r2 = np.squeeze(np.asarray(cv2.calcHist([r2], [0], None, [256], [0, 256])))

            sim_b = self.cos_sim(b1, b2)
            sim_g = self.cos_sim(g1, g2)
            sim_r = self.cos_sim(r1, r2)

            current_sum_sim = sim_b + sim_g + sim_r

            fit.append((key, current_sum_sim))

        return list(reversed(sorted(fit, key=lambda x: x[1])))

    def detect_card(self, image):
        h,w,_ = image.shape

        h2 = h//2

        rec = image[h2:-1,:]
        newh, neww, _ = rec.shape
        meritve = []

        oranzna = np.array([255,127,39])


        for i in range(newh):
            for j in range(neww):
                piksl = rec[i][j]
                dist = np.linalg.norm(piksl - oranzna)

                meritve.append((dist, piksl))


        print(sorted(meritve, key=lambda x: x[0])[0])
        cv2.imshow("Display", rec)
        cv2.waitKey()



    def get_hand(self):
        image = self.get_screenshot()
        hand_images = self.get_hand_images(image)


        for image in hand_images:
            self.detect_card(image)

        """fits = []

        for img in hand_images:
            fits.append(self.match_card_histograms(img))

        viable = [x[0][0] for x in fits]
        if len(viable) == len(set(viable)):
            return viable
        else:
            for i in range(len(viable)):
                for j in range(len(viable)):
                    if viable[i] == viable[j] and i != j:
                        i_score = fits[i][0][1]
                        j_score = fits[j][0][1]

                        if i_score > j_score:
                            viable[j] = fits[j][1][0]

                        if j_score > i_score:
                            viable[i] = fits[i][1][0]

            return viable"""

        # This color is used to normalize a RGB image
    def normalize(self, image):

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

    def wait_turn(self):
        not_my_turn = True
        while not_my_turn:
            image = self.get_screenshot()
            y1, y2 = self.player1_top_left[1], self.player1_bot_right[1]
            x1, x2 = self.player1_top_left[0], self.player1_bot_right[0]

            player1 = image[y1:y2, x1:x2]
            player1 = self.normalize(player1)
            player1 = player1[:, :, 2]
            player1[player1 > 200] = 255
            player1[player1 <= 200] = 0

            if 255 in player1:
                not_my_turn = False

    def get_text(self, image):

        # add white line
        image[18:22, :] = np.array([255, 255, 255])

        # seperate the first one
        x = image[0:18, :]

        # remove the blue
        h, w, _ = x.shape
        for i in range(h):
            for j in range(w):
                if tuple(x[i][j]) == (215, 120, 0):
                    x[i][j] = np.array([0, 0, 0])

        # convert to grayscale
        gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

        # invert the colors white -> black and vice versa
        gray[gray == 0] = 1
        h, w = gray.shape
        for i in range(h):
            for j in range(w):
                if gray[i][j] == 1:
                    gray[i][j] = 255
                else:
                    gray[i][j] = 254 - gray[i][j]

        gray2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray2[0:18, :] = gray

        # cv2.imshow("Display", gray2)
        # cv2.waitKey()

        custom_config = r'--oem 3 --psm 6'
        g = pytesseract.image_to_string(gray2, config=custom_config)
        return g.split()

    def print_mouse_pos(self):
        while True:
            print(pyautogui.position())
if __name__ == "__main__":
    game = Play()
    game.load_tempaltes()
    game.start_game()
    game.press_nova_igra()
    game.press_uncheck_pocakaj()
    game.press_check_pokazi_talon()
    game.press_potrdi_novo_igro()
    game.wait_turn()
    game.get_hand()
    #slike = game.get_hand_images(img)

    """talon = game.get_talon_cards()

    hand = game.get_hand()


    tb = TarockBasics()
    tb.print_hand(talon)
    tb.print_hand(hand)

    #time.sleep(5)
    game.wait_turn()
    time.sleep(1)
    game.press_licitacija_solo()
    game.press_licitacija_potrdi()
    game.get_vrstni_red()
    game.press_licitacija_potrdi()
    game.press_talon_potrdi()
    yy = game.get_vrstni_red()
    print(yy)
    #game.print_mouse_pos()
    #game.press_licitacija_potrdi()
    #game.wait_turn()
    #game.press_X()

    tb = TarockBasics()
    tb.print_hand(hand)

    game.press_X()"""