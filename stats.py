import matplotlib.pyplot as plt
import numpy as np

def parse_file(filename):

    file = open(filename, "r")
    lines = file.readlines()

    dicts = []
    for line in lines:
        slovar = dict()
        x = eval(line)
        for key in x:
            if type(x[key]) == type("a"):
                slovar[key] = eval(x[key])
            else:
                slovar[key] = x[key]
        dicts.append(slovar)


    file.close()
    return filename, dicts

def parse_filename(name):
    mods = name.split()
    return mods[0], mods[1], mods[2]

def good_cards(hand):
    king_count = 0

    for card in hand:
        if card in [8,18,28, 38]:
            king_count += 1

    tarock_count = 0
    for card in hand:
        if card >= 40:
            tarock_count += 1

    if king_count < 2:
        return 0

    if king_count == 2:
        if tarock_count >= 6:
            return 1
        else:
            return 0

    if king_count >= 2:
        if tarock_count >= 8:
            return 2
        else:
            if tarock_count >= 5:
                return 1
            else:
                return 0



def plot(data, labels, title, xlabel, ylabel):
    # creating the bar plot
    plt.bar(labels, data, color='maroon',
            width=0.4)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig("Plots/" + title + ".png")
    plt.show()

def plot_groups(all_cards, good_cards, great_cards, title, xlabel, ylabel, xticks):
    # set width of bar
    barWidth = 0.25

    # Set position of bar on X axis
    br1 = np.arange(len(all_cards))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]


    # Make the plot
    plt.bar(br1, all_cards, color='r', width=barWidth,
            edgecolor='grey', label='Any cards')
    plt.bar(br2, good_cards, color='g', width=barWidth,
            edgecolor='grey', label='Good cards')
    plt.bar(br3, great_cards, color='b', width=barWidth,
            edgecolor='grey', label='Great cards')

    # Adding Xticks
    plt.xlabel(xlabel, fontweight='bold')
    plt.ylabel(ylabel, fontweight='bold')
    plt.xticks([r + barWidth for r in range(len(all_cards))],
               xticks)

    plt.legend()
    plt.title(title)
    plt.savefig("Plots/" + title + ".png")
    plt.show()

if __name__ == "__main__":
    result_files = ['1_1 1_1 1_1', '1_1 1_1 2_2', '1_1 1_1 3_3', '1_1 1_1 5_5', '1_1 1_1 LB', '1_1 1_1 LBB', '1_1 1_1 LW', '1_1 1_1 LWW', '1_1 1_1 random', '1_1 2_2 1_1', '1_1 2_2 2_2', '1_1 2_2 3_3', '1_1 2_2 5_5', '1_1 2_2 LB', '1_1 2_2 LBB', '1_1 2_2 LW', '1_1 2_2 LWW', '1_1 2_2 random', '1_1 3_3 1_1', '1_1 3_3 2_2', '1_1 3_3 3_3', '1_1 3_3 5_5', '1_1 3_3 LB', '1_1 3_3 LBB', '1_1 3_3 LW', '1_1 3_3 LWW', '1_1 3_3 random', '1_1 5_5 1_1', '1_1 5_5 2_2', '1_1 5_5 3_3', '1_1 5_5 5_5', '1_1 5_5 LB', '1_1 5_5 LBB', '1_1 5_5 LW', '1_1 5_5 LWW', '1_1 5_5 random', '1_1 LB 1_1', '1_1 LB 2_2', '1_1 LB 3_3', '1_1 LB 5_5', '1_1 LB LB', '1_1 LB LBB', '1_1 LB LW', '1_1 LB LWW', '1_1 LB random', '1_1 LBB 1_1', '1_1 LBB 2_2', '1_1 LBB 3_3', '1_1 LBB 5_5', '1_1 LBB LB', '1_1 LBB LBB', '1_1 LBB LW', '1_1 LBB LWW', '1_1 LBB random', '1_1 LW 1_1', '1_1 LW 2_2', '1_1 LW 3_3', '1_1 LW 5_5', '1_1 LW LB', '1_1 LW LBB', '1_1 LW LW', '1_1 LW LWW', '1_1 LW random', '1_1 LWW 1_1', '1_1 LWW 2_2', '1_1 LWW 3_3', '1_1 LWW 5_5', '1_1 LWW LB', '1_1 LWW LBB', '1_1 LWW LW', '1_1 LWW LWW', '1_1 LWW random', '1_1 random 1_1', '1_1 random 2_2', '1_1 random 3_3', '1_1 random 5_5', '1_1 random LB', '1_1 random LBB', '1_1 random LW', '1_1 random LWW', '1_1 random random', '2_2 1_1 1_1', '2_2 1_1 2_2', '2_2 1_1 3_3', '2_2 1_1 5_5', '2_2 1_1 LB', '2_2 1_1 LBB', '2_2 1_1 LW', '2_2 1_1 LWW', '2_2 1_1 random', '2_2 2_2 1_1', '2_2 2_2 2_2', '2_2 2_2 3_3', '2_2 2_2 5_5', '2_2 2_2 LB', '2_2 2_2 LBB', '2_2 2_2 LW', '2_2 2_2 LWW', '2_2 2_2 random', '2_2 3_3 1_1', '2_2 3_3 2_2', '2_2 3_3 3_3', '2_2 3_3 5_5', '2_2 3_3 LB', '2_2 3_3 LBB', '2_2 3_3 LW', '2_2 3_3 LWW', '2_2 3_3 random', '2_2 5_5 1_1', '2_2 5_5 2_2', '2_2 5_5 3_3', '2_2 5_5 5_5', '2_2 5_5 LB', '2_2 5_5 LBB', '2_2 5_5 LW', '2_2 5_5 LWW', '2_2 5_5 random', '2_2 LB 1_1', '2_2 LB 2_2', '2_2 LB 3_3', '2_2 LB 5_5', '2_2 LB LB', '2_2 LB LBB', '2_2 LB LW', '2_2 LB LWW', '2_2 LB random', '2_2 LBB 1_1', '2_2 LBB 2_2', '2_2 LBB 3_3', '2_2 LBB 5_5', '2_2 LBB LB', '2_2 LBB LBB', '2_2 LBB LW', '2_2 LBB LWW', '2_2 LBB random', '2_2 LW 1_1', '2_2 LW 2_2', '2_2 LW 3_3', '2_2 LW 5_5', '2_2 LW LB', '2_2 LW LBB', '2_2 LW LW', '2_2 LW LWW', '2_2 LW random', '2_2 LWW 1_1', '2_2 LWW 2_2', '2_2 LWW 3_3', '2_2 LWW 5_5', '2_2 LWW LB', '2_2 LWW LBB', '2_2 LWW LW', '2_2 LWW LWW', '2_2 LWW random', '2_2 random 1_1', '2_2 random 2_2', '2_2 random 3_3', '2_2 random 5_5', '2_2 random LB', '2_2 random LBB', '2_2 random LW', '2_2 random LWW', '2_2 random random', '3_3 1_1 1_1', '3_3 1_1 2_2', '3_3 1_1 3_3', '3_3 1_1 5_5', '3_3 1_1 LB', '3_3 1_1 LBB', '3_3 1_1 LW', '3_3 1_1 LWW', '3_3 1_1 random', '3_3 2_2 1_1', '3_3 2_2 2_2', '3_3 2_2 3_3', '3_3 2_2 5_5', '3_3 2_2 LB', '3_3 2_2 LBB', '3_3 2_2 LW', '3_3 2_2 LWW', '3_3 2_2 random', '3_3 3_3 1_1', '3_3 3_3 2_2', '3_3 3_3 3_3', '3_3 3_3 5_5', '3_3 3_3 LB', '3_3 3_3 LBB', '3_3 3_3 LW', '3_3 3_3 LWW', '3_3 3_3 random', '3_3 5_5 1_1', '3_3 5_5 2_2', '3_3 5_5 3_3', '3_3 5_5 5_5', '3_3 5_5 LB', '3_3 5_5 LBB', '3_3 5_5 LW', '3_3 5_5 LWW', '3_3 5_5 random', '3_3 LB 1_1', '3_3 LB 2_2', '3_3 LB 3_3', '3_3 LB 5_5', '3_3 LB LB', '3_3 LB LBB', '3_3 LB LW', '3_3 LB LWW', '3_3 LB random', '3_3 LBB 1_1', '3_3 LBB 2_2', '3_3 LBB 3_3', '3_3 LBB 5_5', '3_3 LBB LB', '3_3 LBB LBB', '3_3 LBB LW', '3_3 LBB LWW', '3_3 LBB random', '3_3 LW 1_1', '3_3 LW 2_2', '3_3 LW 3_3', '3_3 LW 5_5', '3_3 LW LB', '3_3 LW LBB', '3_3 LW LW', '3_3 LW LWW', '3_3 LW random', '3_3 LWW 1_1', '3_3 LWW 2_2', '3_3 LWW 3_3', '3_3 LWW 5_5', '3_3 LWW LB', '3_3 LWW LBB', '3_3 LWW LW', '3_3 LWW LWW', '3_3 LWW random', '3_3 random 1_1', '3_3 random 2_2', '3_3 random 3_3', '3_3 random 5_5', '3_3 random LB', '3_3 random LBB', '3_3 random LW', '3_3 random LWW', '3_3 random random', '5_5 1_1 1_1', '5_5 1_1 2_2', '5_5 1_1 3_3', '5_5 1_1 5_5', '5_5 1_1 LB', '5_5 1_1 LBB', '5_5 1_1 LW', '5_5 1_1 LWW', '5_5 1_1 random', '5_5 2_2 1_1', '5_5 2_2 2_2', '5_5 2_2 3_3', '5_5 2_2 5_5', '5_5 2_2 LB', '5_5 2_2 LBB', '5_5 2_2 LW', '5_5 2_2 LWW', '5_5 2_2 random', '5_5 3_3 1_1', '5_5 3_3 2_2', '5_5 3_3 3_3', '5_5 3_3 5_5', '5_5 3_3 LB', '5_5 3_3 LBB', '5_5 3_3 LW', '5_5 3_3 LWW', '5_5 3_3 random', '5_5 5_5 1_1', '5_5 5_5 2_2', '5_5 5_5 3_3', '5_5 5_5 5_5', '5_5 5_5 LB', '5_5 5_5 LBB', '5_5 5_5 LW', '5_5 5_5 LWW', '5_5 5_5 random', '5_5 LB 1_1', '5_5 LB 2_2', '5_5 LB 3_3', '5_5 LB 5_5', '5_5 LB LB', '5_5 LB LBB', '5_5 LB LW', '5_5 LB LWW', '5_5 LB random', '5_5 LBB 1_1', '5_5 LBB 2_2', '5_5 LBB 3_3', '5_5 LBB 5_5', '5_5 LBB LB', '5_5 LBB LBB', '5_5 LBB LW', '5_5 LBB LWW', '5_5 LBB random', '5_5 LW 1_1', '5_5 LW 2_2', '5_5 LW 3_3', '5_5 LW 5_5', '5_5 LW LB', '5_5 LW LBB', '5_5 LW LW', '5_5 LW LWW', '5_5 LW random', '5_5 LWW 1_1', '5_5 LWW 2_2', '5_5 LWW 3_3', '5_5 LWW 5_5', '5_5 LWW LB', '5_5 LWW LBB', '5_5 LWW LW', '5_5 LWW LWW', '5_5 LWW random', '5_5 random 1_1', '5_5 random 2_2', '5_5 random 3_3', '5_5 random 5_5', '5_5 random LB', '5_5 random LBB', '5_5 random LW', '5_5 random LWW', '5_5 random random', 'LB 1_1 1_1', 'LB 1_1 2_2', 'LB 1_1 3_3', 'LB 1_1 5_5', 'LB 1_1 LB', 'LB 1_1 LBB', 'LB 1_1 LW', 'LB 1_1 LWW', 'LB 1_1 random', 'LB 2_2 1_1', 'LB 2_2 2_2', 'LB 2_2 3_3', 'LB 2_2 5_5', 'LB 2_2 LB', 'LB 2_2 LBB', 'LB 2_2 LW', 'LB 2_2 LWW', 'LB 2_2 random', 'LB 3_3 1_1', 'LB 3_3 2_2', 'LB 3_3 3_3', 'LB 3_3 5_5', 'LB 3_3 LB', 'LB 3_3 LBB', 'LB 3_3 LW', 'LB 3_3 LWW', 'LB 3_3 random', 'LB 5_5 1_1', 'LB 5_5 2_2', 'LB 5_5 3_3', 'LB 5_5 5_5', 'LB 5_5 LB', 'LB 5_5 LBB', 'LB 5_5 LW', 'LB 5_5 LWW', 'LB 5_5 random', 'LB LB 1_1', 'LB LB 2_2', 'LB LB 3_3', 'LB LB 5_5', 'LB LB LB', 'LB LB LBB', 'LB LB LW', 'LB LB LWW', 'LB LB random', 'LB LBB 1_1', 'LB LBB 2_2', 'LB LBB 3_3', 'LB LBB 5_5', 'LB LBB LB', 'LB LBB LBB', 'LB LBB LW', 'LB LBB LWW', 'LB LBB random', 'LB LW 1_1', 'LB LW 2_2', 'LB LW 3_3', 'LB LW 5_5', 'LB LW LB', 'LB LW LBB', 'LB LW LW', 'LB LW LWW', 'LB LW random', 'LB LWW 1_1', 'LB LWW 2_2', 'LB LWW 3_3', 'LB LWW 5_5', 'LB LWW LB', 'LB LWW LBB', 'LB LWW LW', 'LB LWW LWW', 'LB LWW random', 'LB random 1_1', 'LB random 2_2', 'LB random 3_3', 'LB random 5_5', 'LB random LB', 'LB random LBB', 'LB random LW', 'LB random LWW', 'LB random random', 'LBB 1_1 1_1', 'LBB 1_1 2_2', 'LBB 1_1 3_3', 'LBB 1_1 5_5', 'LBB 1_1 LB', 'LBB 1_1 LBB', 'LBB 1_1 LW', 'LBB 1_1 LWW', 'LBB 1_1 random', 'LBB 2_2 1_1', 'LBB 2_2 2_2', 'LBB 2_2 3_3', 'LBB 2_2 5_5', 'LBB 2_2 LB', 'LBB 2_2 LBB', 'LBB 2_2 LW', 'LBB 2_2 LWW', 'LBB 2_2 random', 'LBB 3_3 1_1', 'LBB 3_3 2_2', 'LBB 3_3 3_3', 'LBB 3_3 5_5', 'LBB 3_3 LB', 'LBB 3_3 LBB', 'LBB 3_3 LW', 'LBB 3_3 LWW', 'LBB 3_3 random', 'LBB 5_5 1_1', 'LBB 5_5 2_2', 'LBB 5_5 3_3', 'LBB 5_5 5_5', 'LBB 5_5 LB', 'LBB 5_5 LBB', 'LBB 5_5 LW', 'LBB 5_5 LWW', 'LBB 5_5 random', 'LBB LB 1_1', 'LBB LB 2_2', 'LBB LB 3_3', 'LBB LB 5_5', 'LBB LB LB', 'LBB LB LBB', 'LBB LB LW', 'LBB LB LWW', 'LBB LB random', 'LBB LBB 1_1', 'LBB LBB 2_2', 'LBB LBB 3_3', 'LBB LBB 5_5', 'LBB LBB LB', 'LBB LBB LBB', 'LBB LBB LW', 'LBB LBB LWW', 'LBB LBB random', 'LBB LW 1_1', 'LBB LW 2_2', 'LBB LW 3_3', 'LBB LW 5_5', 'LBB LW LB', 'LBB LW LBB', 'LBB LW LW', 'LBB LW LWW', 'LBB LW random', 'LBB LWW 1_1', 'LBB LWW 2_2', 'LBB LWW 3_3', 'LBB LWW 5_5', 'LBB LWW LB', 'LBB LWW LBB', 'LBB LWW LW', 'LBB LWW LWW', 'LBB LWW random', 'LBB random 1_1', 'LBB random 2_2', 'LBB random 3_3', 'LBB random 5_5', 'LBB random LB', 'LBB random LBB', 'LBB random LW', 'LBB random LWW', 'LBB random random', 'LW 1_1 1_1', 'LW 1_1 2_2', 'LW 1_1 3_3', 'LW 1_1 5_5', 'LW 1_1 LB', 'LW 1_1 LBB', 'LW 1_1 LW', 'LW 1_1 LWW', 'LW 1_1 random', 'LW 2_2 1_1', 'LW 2_2 2_2', 'LW 2_2 3_3', 'LW 2_2 5_5', 'LW 2_2 LB', 'LW 2_2 LBB', 'LW 2_2 LW', 'LW 2_2 LWW', 'LW 2_2 random', 'LW 3_3 1_1', 'LW 3_3 2_2', 'LW 3_3 3_3', 'LW 3_3 5_5', 'LW 3_3 LB', 'LW 3_3 LBB', 'LW 3_3 LW', 'LW 3_3 LWW', 'LW 3_3 random', 'LW 5_5 1_1', 'LW 5_5 2_2', 'LW 5_5 3_3', 'LW 5_5 5_5', 'LW 5_5 LB', 'LW 5_5 LBB', 'LW 5_5 LW', 'LW 5_5 LWW', 'LW 5_5 random', 'LW LB 1_1', 'LW LB 2_2', 'LW LB 3_3', 'LW LB 5_5', 'LW LB LB', 'LW LB LBB', 'LW LB LW', 'LW LB LWW', 'LW LB random', 'LW LBB 1_1', 'LW LBB 2_2', 'LW LBB 3_3', 'LW LBB 5_5', 'LW LBB LB', 'LW LBB LBB', 'LW LBB LW', 'LW LBB LWW', 'LW LBB random', 'LW LW 1_1', 'LW LW 2_2', 'LW LW 3_3', 'LW LW 5_5', 'LW LW LB', 'LW LW LBB', 'LW LW LW', 'LW LW LWW', 'LW LW random', 'LW LWW 1_1', 'LW LWW 2_2', 'LW LWW 3_3', 'LW LWW 5_5', 'LW LWW LB', 'LW LWW LBB', 'LW LWW LW', 'LW LWW LWW', 'LW LWW random', 'LW random 1_1', 'LW random 2_2', 'LW random 3_3', 'LW random 5_5', 'LW random LB', 'LW random LBB', 'LW random LW', 'LW random LWW', 'LW random random', 'LWW 1_1 1_1', 'LWW 1_1 2_2', 'LWW 1_1 3_3', 'LWW 1_1 5_5', 'LWW 1_1 LB', 'LWW 1_1 LBB', 'LWW 1_1 LW', 'LWW 1_1 LWW', 'LWW 1_1 random', 'LWW 2_2 1_1', 'LWW 2_2 2_2', 'LWW 2_2 3_3', 'LWW 2_2 5_5', 'LWW 2_2 LB', 'LWW 2_2 LBB', 'LWW 2_2 LW', 'LWW 2_2 LWW', 'LWW 2_2 random', 'LWW 3_3 1_1', 'LWW 3_3 2_2', 'LWW 3_3 3_3', 'LWW 3_3 5_5', 'LWW 3_3 LB', 'LWW 3_3 LBB', 'LWW 3_3 LW', 'LWW 3_3 LWW', 'LWW 3_3 random', 'LWW 5_5 1_1', 'LWW 5_5 2_2', 'LWW 5_5 3_3', 'LWW 5_5 5_5', 'LWW 5_5 LB', 'LWW 5_5 LBB', 'LWW 5_5 LW', 'LWW 5_5 LWW', 'LWW 5_5 random', 'LWW LB 1_1', 'LWW LB 2_2', 'LWW LB 3_3', 'LWW LB 5_5', 'LWW LB LB', 'LWW LB LBB', 'LWW LB LW', 'LWW LB LWW', 'LWW LB random', 'LWW LBB 1_1', 'LWW LBB 2_2', 'LWW LBB 3_3', 'LWW LBB 5_5', 'LWW LBB LB', 'LWW LBB LBB', 'LWW LBB LW', 'LWW LBB LWW', 'LWW LBB random', 'LWW LW 1_1', 'LWW LW 2_2', 'LWW LW 3_3', 'LWW LW 5_5', 'LWW LW LB', 'LWW LW LBB', 'LWW LW LW', 'LWW LW LWW', 'LWW LW random', 'LWW LWW 1_1', 'LWW LWW 2_2', 'LWW LWW 3_3', 'LWW LWW 5_5', 'LWW LWW LB', 'LWW LWW LBB', 'LWW LWW LW', 'LWW LWW LWW', 'LWW LWW random', 'LWW random 1_1', 'LWW random 2_2', 'LWW random 3_3', 'LWW random 5_5', 'LWW random LB', 'LWW random LBB', 'LWW random LW', 'LWW random LWW', 'LWW random random', 'random 1_1 1_1', 'random 1_1 2_2', 'random 1_1 3_3', 'random 1_1 5_5', 'random 1_1 LB', 'random 1_1 LBB', 'random 1_1 LW', 'random 1_1 LWW', 'random 1_1 random', 'random 2_2 1_1', 'random 2_2 2_2', 'random 2_2 3_3', 'random 2_2 5_5', 'random 2_2 LB', 'random 2_2 LBB', 'random 2_2 LW', 'random 2_2 LWW', 'random 2_2 random', 'random 3_3 1_1', 'random 3_3 2_2', 'random 3_3 3_3', 'random 3_3 5_5', 'random 3_3 LB', 'random 3_3 LBB', 'random 3_3 LW', 'random 3_3 LWW', 'random 3_3 random', 'random 5_5 1_1', 'random 5_5 2_2', 'random 5_5 3_3', 'random 5_5 5_5', 'random 5_5 LB', 'random 5_5 LBB', 'random 5_5 LW', 'random 5_5 LWW', 'random 5_5 random', 'random LB 1_1', 'random LB 2_2', 'random LB 3_3', 'random LB 5_5', 'random LB LB', 'random LB LBB', 'random LB LW', 'random LB LWW', 'random LB random', 'random LBB 1_1', 'random LBB 2_2', 'random LBB 3_3', 'random LBB 5_5', 'random LBB LB', 'random LBB LBB', 'random LBB LW', 'random LBB LWW', 'random LBB random', 'random LW 1_1', 'random LW 2_2', 'random LW 3_3', 'random LW 5_5', 'random LW LB', 'random LW LBB', 'random LW LW', 'random LW LWW', 'random LW random', 'random LWW 1_1', 'random LWW 2_2', 'random LWW 3_3', 'random LWW 5_5', 'random LWW LB', 'random LWW LBB', 'random LWW LW', 'random LWW LWW', 'random LWW random', 'random random 1_1', 'random random 2_2', 'random random 3_3', 'random random 5_5', 'random random LB', 'random random LBB', 'random random LW', 'random random LWW', 'random random random']

    #solo games
    solo1_1 = []
    solo2_2 = []
    solo3_3 = []
    solo5_5 = []
    solo_random = []
    solo_LW = []
    solo_LB = []
    solo_LWW = []
    solo_LBB = []

    #duo games
    duo1_1 = []
    duo2_2 = []
    duo3_3 = []
    duo5_5 = []
    duo_random = []
    duo_LW = []
    duo_LB = []
    duo_LWW = []
    duo_LBB = []

    """for file in result_files:
        _, results = parse_file("tests/" + file)
        mode1, mode2, mode3 = parse_filename(file)
        for result in results:
            if mode1 == "1_1":
                if 1 == result["solo"]:
                    solo1_1.append(result["points"][1])
                else:
                    duo1_1.append(result["points"][1])
            elif mode1 == "2_2":
                if 1 == result["solo"]:
                    solo2_2.append(result["points"][1])
                else:
                    duo2_2.append(result["points"][1])
            elif mode1 == "3_3":
                if 1 == result["solo"]:
                    solo3_3.append(result["points"][1])
                else:
                    duo3_3.append(result["points"][1])
            elif mode1 == "5_5":
                if 1 == result["solo"]:
                    solo5_5.append(result["points"][1])
                else:
                    duo5_5.append(result["points"][1])
            elif mode1 == "random":
                if 1 == result["solo"]:
                    solo_random.append(result["points"][1])
                else:
                    duo_random.append(result["points"][1])
            elif mode1 == "LW":
                if 1 == result["solo"]:
                    solo_LW.append(result["points"][1])
                else:
                    duo_LW.append(result["points"][1])
            elif mode1 == "LB":
                if 1 == result["solo"]:
                    solo_LB.append(result["points"][1])
                else:
                    duo_LB.append(result["points"][1])
            elif mode1 == "LWW":
                if 1 == result["solo"]:
                    solo_LWW.append(result["points"][1])
                else:
                    duo_LWW.append(result["points"][1])
            elif mode1 == "LBB":
                if 1 == result["solo"]:
                    solo_LBB.append(result["points"][1])
                else:
                    duo_LBB.append(result["points"][1])
            else:
                raise NotImplemented


            if mode2 == "1_1":
                if 2 == result["solo"]:
                    solo1_1.append(result["points"][2])
                else:
                    duo1_1.append(result["points"][2])
            elif mode2 == "2_2":
                if 2 == result["solo"]:
                    solo2_2.append(result["points"][2])
                else:
                    duo2_2.append(result["points"][2])
            elif mode2 == "3_3":
                if 2 == result["solo"]:
                    solo3_3.append(result["points"][2])
                else:
                    duo3_3.append(result["points"][2])
            elif mode2 == "5_5":
                if 2 == result["solo"]:
                    solo5_5.append(result["points"][2])
                else:
                    duo5_5.append(result["points"][2])
            elif mode2 == "random":
                if 2 == result["solo"]:
                    solo_random.append(result["points"][2])
                else:
                    duo_random.append(result["points"][2])
            elif mode2 == "LW":
                if 2 == result["solo"]:
                    solo_LW.append(result["points"][2])
                else:
                    duo_LW.append(result["points"][2])
            elif mode2 == "LB":
                if 2 == result["solo"]:
                    solo_LB.append(result["points"][2])
                else:
                    duo_LB.append(result["points"][2])
            elif mode2 == "LWW":
                if 2 == result["solo"]:
                    solo_LWW.append(result["points"][2])
                else:
                    duo_LWW.append(result["points"][2])
            elif mode2 == "LBB":
                if 2 == result["solo"]:
                    solo_LBB.append(result["points"][2])
                else:
                    duo_LBB.append(result["points"][2])
            else:
                raise NotImplemented


            if mode3 == "1_1":
                if 3 == result["solo"]:
                    solo1_1.append(result["points"][3])
                else:
                    duo1_1.append(result["points"][3])
            elif mode3 == "2_2":
                if 3 == result["solo"]:
                    solo2_2.append(result["points"][3])
                else:
                    duo2_2.append(result["points"][3])
            elif mode3 == "3_3":
                if 3 == result["solo"]:
                    solo3_3.append(result["points"][3])
                else:
                    duo3_3.append(result["points"][3])
            elif mode3 == "5_5":
                if 3 == result["solo"]:
                    solo5_5.append(result["points"][3])
                else:
                    duo5_5.append(result["points"][3])
            elif mode3 == "random":
                if 3 == result["solo"]:
                    solo_random.append(result["points"][3])
                else:
                    duo_random.append(result["points"][3])
            elif mode3 == "LW":
                if 3 == result["solo"]:
                    solo_LW.append(result["points"][3])
                else:
                    duo_LW.append(result["points"][3])
            elif mode3 == "LB":
                if 3 == result["solo"]:
                    solo_LB.append(result["points"][3])
                else:
                    duo_LB.append(result["points"][3])
            elif mode3 == "LWW":
                if 3 == result["solo"]:
                    solo_LWW.append(result["points"][3])
                else:
                    duo_LWW.append(result["points"][3])
            elif mode3 == "LBB":
                if 3 == result["solo"]:
                    solo_LBB.append(result["points"][3])
                else:
                    duo_LBB.append(result["points"][3])
            else:
                raise NotImplemented


    print("-------SOLO PLAYING--------------")
    print(sum(solo1_1)/len(solo1_1))
    print(sum(solo2_2) / len(solo2_2))
    print(sum(solo3_3) / len(solo3_3))
    print(sum(solo5_5) / len(solo5_5))
    print(sum(solo_random) / len(solo_random))
    print(sum(solo_LW) / len(solo_LW))
    print(sum(solo_LB) / len(solo_LB))
    print(sum(solo_LWW) / len(solo_LWW))
    print(sum(solo_LBB) / len(solo_LBB))
    print("---------------------------------")

    print("--------DUO PLAYING--------------")
    print(sum(duo1_1) / len(duo1_1))
    print(sum(duo2_2) / len(duo2_2))
    print(sum(duo3_3) / len(duo3_3))
    print(sum(duo5_5) / len(duo5_5))
    print(sum(duo_random) / len(duo_random))
    print(sum(duo_LW) / len(duo_LW))
    print(sum(duo_LB) / len(duo_LB))
    print(sum(duo_LWW) / len(duo_LWW))
    print(sum(duo_LBB) / len(duo_LBB))
    print("---------------------------------")"""

    play_modes = ["1_1", "2_2", "3_3", "5_5", "random", "LW", "LB", "LWW", "LBB"]

    solo_all_average = [21.706315620643284,
                        21.877163904235726,
                        23.061153080527703,
                        21.299021371072772,
                        19.611067886826472,
                        15.224834932868609,
                        23.383435544971064,
                        15.24445847102068,
                        26.084089219330856]

    duo_all_average = [21.858089374918954,
                        21.80069328381306,
                        22.78258214543458,
                        21.586647123668993,
                        19.51179741647997,
                        16.675404598868237,
                        21.989102180181405,
                        16.677751678473005,
                        23.39634011090573]

    print("OVERALL AVERAGES")
    x = sorted(zip(solo_all_average, play_modes))
    print(x)
    data = [points for points, mode in x]
    labels = [mode for points, mode in x]

    plot(data, labels, "Average number of points for solo play", "Agents", "Points")
    y = sorted(zip(duo_all_average, play_modes))
    print(y)
    data = [points for points, mode in y]
    labels = [mode for points, mode in y]

    plot(data, labels, "Average number of points for duo play", "Agents", "Points")

    print("---------------------------------------------")

    """solo1_1_random = []
    solo1_1_LW = []
    solo1_1_LB = []
    solo1_1_LWW = []
    solo1_1_LBB = []

    solo2_2_random = []
    solo2_2_LW = []
    solo2_2_LB = []
    solo2_2_LWW = []
    solo2_2_LBB = []

    solo3_3_random = []
    solo3_3_LW = []
    solo3_3_LB = []
    solo3_3_LWW = []
    solo3_3_LBB = []

    solo5_5_random = []
    solo5_5_LW = []
    solo5_5_LB = []
    solo5_5_LWW = []
    solo5_5_LBB = []

    duo1_1_random = []
    duo1_1_LW = []
    duo1_1_LB = []
    duo1_1_LWW = []
    duo1_1_LBB = []

    duo2_2_random = []
    duo2_2_LW = []
    duo2_2_LB = []
    duo2_2_LWW = []
    duo2_2_LBB = []

    duo3_3_random = []
    duo3_3_LW = []
    duo3_3_LB = []
    duo3_3_LWW = []
    duo3_3_LBB = []

    duo5_5_random = []
    duo5_5_LW = []
    duo5_5_LB = []
    duo5_5_LWW = []
    duo5_5_LBB = []
    for file in result_files:
        _, results = parse_file("tests/" + file)
        mode1, mode2, mode3 = parse_filename(file)
        for result in results:
            if mode1 == "1_1":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        solo1_1_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        solo1_1_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        solo1_1_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        solo1_1_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        solo1_1_LBB.append(result["points"][1])
                    else:
                        continue
                else:
                    if mode2 == "random" and mode3 == "random":
                        duo1_1_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo1_1_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo1_1_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo1_1_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo1_1_LBB.append(result["points"][1])
                    else:
                        continue
            elif mode1 == "2_2":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        solo2_2_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        solo2_2_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        solo2_2_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        solo2_2_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        solo2_2_LBB.append(result["points"][1])
                    else:
                        continue
                else:
                    if mode2 == "random" and mode3 == "random":
                        duo2_2_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo2_2_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo2_2_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo2_2_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo2_2_LBB.append(result["points"][1])
                    else:
                        continue
            elif mode1 == "3_3":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        solo3_3_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        solo3_3_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        solo3_3_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        solo3_3_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        solo3_3_LBB.append(result["points"][1])
                    else:
                        continue
                else:
                    if mode2 == "random" and mode3 == "random":
                        duo3_3_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo3_3_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo3_3_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo3_3_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo3_3_LBB.append(result["points"][1])
                    else:
                        continue
            elif mode1 == "5_5":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        solo5_5_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        solo5_5_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        solo5_5_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        solo5_5_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        solo5_5_LBB.append(result["points"][1])
                    else:
                        continue
                else:
                    if mode2 == "random" and mode3 == "random":
                        duo5_5_random.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo5_5_LW.append(result["points"][1])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo5_5_LB.append(result["points"][1])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo5_5_LWW.append(result["points"][1])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo5_5_LBB.append(result["points"][1])
                    else:
                        continue
            else:
                continue

    print(sum(solo1_1_random)/len(solo1_1_random))
    print(sum(solo1_1_LW)/len(solo1_1_LW))
    print(sum(solo1_1_LB)/len(solo1_1_LB))
    print(sum(solo1_1_LWW)/len(solo1_1_LWW))
    print(sum(solo1_1_LBB)/len(solo1_1_LBB))

    print(sum(solo2_2_random)/len(solo2_2_random))
    print(sum(solo2_2_LW)/len(solo2_2_LW))
    print(sum(solo2_2_LB)/len(solo2_2_LB))
    print(sum(solo2_2_LWW)/len(solo2_2_LWW))
    print(sum(solo2_2_LBB)/len(solo2_2_LBB))

    print(sum(solo3_3_random)/len(solo3_3_random))
    print(sum(solo3_3_LW)/len(solo3_3_LW))
    print(sum(solo3_3_LB)/len(solo3_3_LB))
    print(sum(solo3_3_LWW)/len(solo3_3_LWW))
    print(sum(solo3_3_LBB)/len(solo3_3_LBB))

    print(sum(solo5_5_random)/len(solo5_5_random))
    print(sum(solo5_5_LW)/len(solo5_5_LW))
    print(sum(solo5_5_LB)/len(solo5_5_LB))
    print(sum(solo5_5_LWW)/len(solo5_5_LWW))
    print(sum(solo5_5_LBB)/len(solo5_5_LBB))"""

    play_modes = ["random", "LW", "LB", "LWW", "LBB"]
    print("Q AGENT VS 2 THEORETICAL AGENTS")
    solo_1_1 = [23.6355421686747,
                31.289634146341463,
                17.558073654390935,
                31.666666666666668,
                15.526690391459075]
    xx = sorted(zip(solo_1_1, play_modes))
    print(xx)

    data = [points for points, mode in xx]
    labels = [mode for points, mode in xx]

    plot(data, labels, "1_1 Q agent playing vs 2 theoretical agents", "Agents", "Points")

    solo_2_2 = [24.087774294670847,
                30.064606741573034,
                17.348973607038122,
                31.10355029585799,
                14.27076923076923]
    yy = sorted(zip(solo_2_2, play_modes))
    print(yy)

    data = [points for points, mode in yy]
    labels = [mode for points, mode in yy]

    plot(data, labels, "2_2 Q agent playing vs 2 theoretical agents", "Agents", "Points")

    solo_3_3 = [24.476744186046513,
                30.605187319884728,
                19.124629080118694,
                32.269113149847094,
                14.972222222222221]
    zz = sorted(zip(solo_3_3, play_modes))
    print(zz)

    data = [points for points, mode in zz]
    labels = [mode for points, mode in zz]

    plot(data, labels, "3_3 Q agent playing vs 2 theoretical agents", "Agents", "Points")

    solo_5_5 = [22.174418604651162,
                31.295731707317074,
                16.562874251497007,
                30.614197530864196,
                13.064024390243903]
    ww = sorted(zip(solo_5_5, play_modes))
    print(ww)

    data = [points for points, mode in ww]
    labels = [mode for points, mode in ww]

    plot(data, labels, "5_5 Q agent playing vs 2 theoretical agents", "Agents", "Points")
    print("----------------------------------------------------")
    """solo1_1_random = []
    solo1_1_LW = []
    solo1_1_LB = []
    solo1_1_LWW = []
    solo1_1_LBB = []

    solo2_2_random = []
    solo2_2_LW = []
    solo2_2_LB = []
    solo2_2_LWW = []
    solo2_2_LBB = []

    solo3_3_random = []
    solo3_3_LW = []
    solo3_3_LB = []
    solo3_3_LWW = []
    solo3_3_LBB = []

    solo5_5_random = []
    solo5_5_LW = []
    solo5_5_LB = []
    solo5_5_LWW = []
    solo5_5_LBB = []

    solo1_1_random_good = []
    solo1_1_LW_good = []
    solo1_1_LB_good = []
    solo1_1_LWW_good = []
    solo1_1_LBB_good = []

    solo2_2_random_good = []
    solo2_2_LW_good = []
    solo2_2_LB_good = []
    solo2_2_LWW_good = []
    solo2_2_LBB_good = []

    solo3_3_random_good = []
    solo3_3_LW_good = []
    solo3_3_LB_good = []
    solo3_3_LWW_good = []
    solo3_3_LBB_good = []

    solo5_5_random_good = []
    solo5_5_LW_good = []
    solo5_5_LB_good = []
    solo5_5_LWW_good = []
    solo5_5_LBB_good = []

    solo1_1_random_great = []
    solo1_1_LW_great = []
    solo1_1_LB_great = []
    solo1_1_LWW_great = []
    solo1_1_LBB_great = []

    solo2_2_random_great = []
    solo2_2_LW_great = []
    solo2_2_LB_great = []
    solo2_2_LWW_great = []
    solo2_2_LBB_great = []

    solo3_3_random_great = []
    solo3_3_LW_great = []
    solo3_3_LB_great = []
    solo3_3_LWW_great = []
    solo3_3_LBB_great = []

    solo5_5_random_great = []
    solo5_5_LW_great = []
    solo5_5_LB_great = []
    solo5_5_LWW_great = []
    solo5_5_LBB_great = []

    for file in result_files:
        _, results = parse_file("tests/" + file)
        mode1, mode2, mode3 = parse_filename(file)

        for result in results:
            p1 = result["p1"]
            card_quality = good_cards(p1)
            if mode1 == "1_1":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        if card_quality == 0:
                            solo1_1_random.append(result["points"][1])
                        elif card_quality == 1:
                            solo1_1_random_good.append(result["points"][1])
                        else:
                            solo1_1_random_great.append(result["points"][1])
                    elif mode2 == "LW" and mode3 == "LW":
                        if card_quality == 0:
                            solo1_1_LW.append(result["points"][1])
                        elif card_quality == 1:
                            solo1_1_LW_good.append(result["points"][1])
                        else:
                            solo1_1_LW_great.append(result["points"][1])

                    elif mode2 == "LB" and mode3 == "LB":
                        if card_quality == 0:
                            solo1_1_LB.append(result["points"][1])
                        elif card_quality == 1:
                            solo1_1_LB_good.append(result["points"][1])
                        else:
                            solo1_1_LB_great.append(result["points"][1])

                    elif mode2 == "LWW" and mode3 == "LWW":
                        if card_quality == 0:
                            solo1_1_LWW.append(result["points"][1])
                        elif card_quality == 1:
                            solo1_1_LWW_good.append(result["points"][1])
                        else:
                            solo1_1_LWW_great.append(result["points"][1])

                    elif mode2 == "LBB" and mode3 == "LBB":
                        if card_quality == 0:
                            solo1_1_LBB.append(result["points"][1])
                        elif card_quality == 1:
                            solo1_1_LBB_good.append(result["points"][1])
                        else:
                            solo1_1_LBB_great.append(result["points"][1])

                    else:
                        continue

            elif mode1 == "2_2":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        if card_quality == 0:
                            solo2_2_random.append(result["points"][1])
                        elif card_quality == 1:
                            solo2_2_random_good.append(result["points"][1])
                        else:
                            solo2_2_random_great.append(result["points"][1])

                    elif mode2 == "LW" and mode3 == "LW":
                        if card_quality == 0:
                            solo2_2_LW.append(result["points"][1])
                        elif card_quality == 1:
                            solo2_2_LW_good.append(result["points"][1])
                        else:
                            solo2_2_LW_great.append(result["points"][1])

                    elif mode2 == "LB" and mode3 == "LB":
                        if card_quality == 0:
                            solo2_2_LB.append(result["points"][1])
                        elif card_quality == 1:
                            solo2_2_LB_good.append(result["points"][1])
                        else:
                            solo2_2_LB_great.append(result["points"][1])

                    elif mode2 == "LWW" and mode3 == "LWW":
                        if card_quality == 0:
                            solo2_2_LWW.append(result["points"][1])
                        elif card_quality == 1:
                            solo2_2_LWW_good.append(result["points"][1])
                        else:
                            solo2_2_LWW_great.append(result["points"][1])

                    elif mode2 == "LBB" and mode3 == "LBB":
                        if card_quality == 0:
                            solo2_2_LBB.append(result["points"][1])
                        elif card_quality == 1:
                            solo2_2_LBB_good.append(result["points"][1])
                        else:
                            solo2_2_LBB_great.append(result["points"][1])

                    else:
                        continue

            elif mode1 == "3_3":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        if card_quality == 0:
                            solo3_3_random.append(result["points"][1])
                        elif card_quality == 1:
                            solo3_3_random_good.append(result["points"][1])
                        else:
                            solo3_3_random_great.append(result["points"][1])

                    elif mode2 == "LW" and mode3 == "LW":
                        if card_quality == 0:
                            solo3_3_LW.append(result["points"][1])
                        elif card_quality == 1:
                            solo3_3_LW_good.append(result["points"][1])
                        else:
                            solo3_3_LW_great.append(result["points"][1])

                    elif mode2 == "LB" and mode3 == "LB":
                        if card_quality == 0:
                            solo3_3_LB.append(result["points"][1])
                        elif card_quality == 1:
                            solo3_3_LB_good.append(result["points"][1])
                        else:
                            solo3_3_LB_great.append(result["points"][1])

                    elif mode2 == "LWW" and mode3 == "LWW":
                        if card_quality == 0:
                            solo3_3_LWW.append(result["points"][1])
                        elif card_quality == 1:
                            solo3_3_LWW_good.append(result["points"][1])
                        else:
                            solo3_3_LWW_great.append(result["points"][1])

                    elif mode2 == "LBB" and mode3 == "LBB":
                        if card_quality == 0:
                            solo3_3_LBB.append(result["points"][1])
                        elif card_quality == 1:
                            solo3_3_LBB_good.append(result["points"][1])
                        else:
                            solo3_3_LBB_great.append(result["points"][1])

                    else:
                        continue

            elif mode1 == "5_5":
                if 1 == result["solo"]:
                    if mode2 == "random" and mode3 == "random":
                        if card_quality == 0:
                            solo5_5_random.append(result["points"][1])
                        elif card_quality == 1:
                            solo5_5_random_good.append(result["points"][1])
                        else:
                            solo5_5_random_great.append(result["points"][1])

                    elif mode2 == "LW" and mode3 == "LW":
                        if card_quality == 0:
                            solo5_5_LW.append(result["points"][1])
                        elif card_quality == 1:
                            solo5_5_LW_good.append(result["points"][1])
                        else:
                            solo5_5_LW_great.append(result["points"][1])

                    elif mode2 == "LB" and mode3 == "LB":
                        if card_quality == 0:
                            solo5_5_LB.append(result["points"][1])
                        elif card_quality == 1:
                            solo5_5_LB_good.append(result["points"][1])
                        else:
                            solo5_5_LB_great.append(result["points"][1])

                    elif mode2 == "LWW" and mode3 == "LWW":
                        if card_quality == 0:
                            solo5_5_LWW.append(result["points"][1])
                        elif card_quality == 1:
                            solo5_5_LWW_good.append(result["points"][1])
                        else:
                            solo5_5_LWW_great.append(result["points"][1])

                    elif mode2 == "LBB" and mode3 == "LBB":
                        if card_quality == 0:
                            solo5_5_LBB.append(result["points"][1])
                        elif card_quality == 1:
                            solo5_5_LBB_good.append(result["points"][1])
                        else:
                            solo5_5_LBB_great.append(result["points"][1])

                    else:
                        continue
            else:
                continue

    print(sum(solo1_1_random) / len(solo1_1_random))
    print(sum(solo1_1_LW) / len(solo1_1_LW))
    print(sum(solo1_1_LB) / len(solo1_1_LB))
    print(sum(solo1_1_LWW) / len(solo1_1_LWW))
    print(sum(solo1_1_LBB) / len(solo1_1_LBB))

    print(sum(solo2_2_random) / len(solo2_2_random))
    print(sum(solo2_2_LW) / len(solo2_2_LW))
    print(sum(solo2_2_LB) / len(solo2_2_LB))
    print(sum(solo2_2_LWW) / len(solo2_2_LWW))
    print(sum(solo2_2_LBB) / len(solo2_2_LBB))

    print(sum(solo3_3_random) / len(solo3_3_random))
    print(sum(solo3_3_LW) / len(solo3_3_LW))
    print(sum(solo3_3_LB) / len(solo3_3_LB))
    print(sum(solo3_3_LWW) / len(solo3_3_LWW))
    print(sum(solo3_3_LBB) / len(solo3_3_LBB))

    print(sum(solo5_5_random) / len(solo5_5_random))
    print(sum(solo5_5_LW) / len(solo5_5_LW))
    print(sum(solo5_5_LB) / len(solo5_5_LB))
    print(sum(solo5_5_LWW) / len(solo5_5_LWW))
    print(sum(solo5_5_LBB) / len(solo5_5_LBB))

    print(sum(solo1_1_random_good) / len(solo1_1_random_good))
    print(sum(solo1_1_LW_good) / len(solo1_1_LW_good))
    print(sum(solo1_1_LB_good) / len(solo1_1_LB_good))
    print(sum(solo1_1_LWW_good) / len(solo1_1_LWW_good))
    print(sum(solo1_1_LBB_good) / len(solo1_1_LBB_good))

    print(sum(solo2_2_random_good) / len(solo2_2_random_good))
    print(sum(solo2_2_LW_good) / len(solo2_2_LW_good))
    print(sum(solo2_2_LB_good) / len(solo2_2_LB_good))
    print(sum(solo2_2_LWW_good) / len(solo2_2_LWW_good))
    print(sum(solo2_2_LBB_good) / len(solo2_2_LBB_good))

    print(sum(solo3_3_random_good) / len(solo3_3_random_good))
    print(sum(solo3_3_LW_good) / len(solo3_3_LW_good))
    print(sum(solo3_3_LB_good) / len(solo3_3_LB_good))
    print(sum(solo3_3_LWW_good) / len(solo3_3_LWW_good))
    print(sum(solo3_3_LBB_good) / len(solo3_3_LBB_good))

    print(sum(solo5_5_random_good) / len(solo5_5_random_good))
    print(sum(solo5_5_LW_good) / len(solo5_5_LW_good))
    print(sum(solo5_5_LB_good) / len(solo5_5_LB_good))
    print(sum(solo5_5_LWW_good) / len(solo5_5_LWW_good))
    print(sum(solo5_5_LBB_good) / len(solo5_5_LBB_good))

    print(sum(solo1_1_random_great) / len(solo1_1_random_great))
    print(sum(solo1_1_LW_great) / len(solo1_1_LW_great))
    print(sum(solo1_1_LB_great) / len(solo1_1_LB_great))
    print(sum(solo1_1_LWW_great) / len(solo1_1_LWW_great))
    print(sum(solo1_1_LBB_great) / len(solo1_1_LBB_great))

    print(sum(solo2_2_random_great) / len(solo2_2_random_great))
    print(sum(solo2_2_LW_great) / len(solo2_2_LW_great))
    print(sum(solo2_2_LB_great) / len(solo2_2_LB_great))
    print(sum(solo2_2_LWW_great) / len(solo2_2_LWW_great))
    print(sum(solo2_2_LBB_great) / len(solo2_2_LBB_great))

    print(sum(solo3_3_random_great) / len(solo3_3_random_great))
    print(sum(solo3_3_LW_great) / len(solo3_3_LW_great))
    print(sum(solo3_3_LB_great) / len(solo3_3_LB_great))
    print(sum(solo3_3_LWW_great) / len(solo3_3_LWW_great))
    print(sum(solo3_3_LBB_great) / len(solo3_3_LBB_great))

    print(sum(solo5_5_random_great) / len(solo5_5_random_great))
    print(sum(solo5_5_LW_great) / len(solo5_5_LW_great))
    print(sum(solo5_5_LB_great) / len(solo5_5_LB_great))
    print(sum(solo5_5_LWW_great) / len(solo5_5_LWW_great))
    print(sum(solo5_5_LBB_great) / len(solo5_5_LBB_great))"""

    solo1_1= [21.600790513833992,
                29.58498023715415,
                15.254545454545454,
                29.72463768115942,
                12.99047619047619]

    solo2_2 = [22.164,
                27.41090909090909,
                15.891472868217054,
                28.788,
                12.0]
    solo3_3 = [22.433070866141733,
                28.745454545454546,
                17.78148148148148,
                30.481781376518217,
                12.745173745173744]

    solo5_5 = [20.19083969465649,
                29.320158102766797,
                14.8125,
                28.30801687763713,
                11.324]

    solo1_1_good = [30.141025641025642,
                        36.44444444444444,
                        25.333333333333332,
                        37.794520547945204,
                        22.823529411764707]

    solo2_2_good = [30.91176470588235,
                    38.08,
                    21.102564102564102,
                    37.258823529411764,
                    21.34285714285714]

    solo3_3_good = [30.137931034482758,
                    37.14705882352941,
                    24.384615384615383,
                    37.013513513513516,
                    20.494949494949495]

    solo5_5_good = [27.636363636363637,
                    38.02777777777778,
                    21.23611111111111,
                    36.397590361445786,
                    18.558441558441558]

    solo_1_1_great = [31.0,
                        51.333333333333336,
                        34.333333333333336,
                        49.4,
                        27.666666666666668]

    solo_2_2_great = [41.0,
                        51.5,
                        34.0,
                        49.666666666666664,
                        28.8]

    solo_3_3_great = [33.333333333333336,
                        47.25,
                        29.5,
                        47.333333333333336,
                        30.0]
    solo_5_5_great = [42.0,
                        36.333333333333336,
                        35.166666666666664,
                        47.25,
                        25.0]

    print("Q AGENT VS 2 THEORETICAL AGENTS WITH REGARDS TO QUALITY OF CARDS")

    plot_groups(solo_1_1, solo1_1_good, solo_1_1_great, "1_1 Q agent vs 2 theoretical agents with respect to quality of cards", "Theoretical agents",
                "Points", play_modes)

    plot_groups(solo_2_2, solo2_2_good, solo_2_2_great,
                "2_2 Q agent vs 2 theoretical agents with respect to quality of cards", "Theoretical agents",
                "Points", play_modes)

    plot_groups(solo_3_3, solo3_3_good, solo_3_3_great,
                "3_3 Q agent vs 2 theoretical agents with respect to quality of cards", "Theoretical agents",
                "Points", play_modes)

    plot_groups(solo_5_5, solo5_5_good, solo_5_5_great,
                "5_5 Q agent vs 2 theoretical agents with respect to quality of cards", "Theoretical agents",
                "Points", play_modes)



    print("EVERY GAME")
    xxx = sorted(zip(solo_1_1, play_modes))
    print(xxx)
    yyy = sorted(zip(solo_2_2, play_modes))
    print(yyy)
    zzz = sorted(zip(solo_3_3, play_modes))
    print(zzz)
    www = sorted(zip(solo_5_5, play_modes))
    print(www)

    print("ONLY GOOD CARDS")
    xxx = sorted(zip(solo1_1_good, play_modes))
    print(xxx)
    yyy = sorted(zip(solo2_2_good, play_modes))
    print(yyy)
    zzz = sorted(zip(solo3_3_good, play_modes))
    print(zzz)
    www = sorted(zip(solo5_5_good, play_modes))
    print(www)

    print("ONLY GREAT CARDS")
    xxx = sorted(zip(solo_1_1_great, play_modes))
    print(xxx)
    yyy = sorted(zip(solo_2_2_great, play_modes))
    print(yyy)
    zzz = sorted(zip(solo_3_3_great, play_modes))
    print(zzz)
    www = sorted(zip(solo_5_5_great, play_modes))
    print(www)
    print("----------------------------------")

    """duo1_1_random = []
    duo1_1_LW = []
    duo1_1_LB = []
    duo1_1_LWW = []
    duo1_1_LBB = []

    duo2_2_random = []
    duo2_2_LW = []
    duo2_2_LB = []
    duo2_2_LWW = []
    duo2_2_LBB = []

    duo3_3_random = []
    duo3_3_LW = []
    duo3_3_LB = []
    duo3_3_LWW = []
    duo3_3_LBB = []

    duo5_5_random = []
    duo5_5_LW = []
    duo5_5_LB = []
    duo5_5_LWW = []
    duo5_5_LBB = []

    duo1_1_random_partner = []
    duo1_1_LW_partner = []
    duo1_1_LB_partner = []
    duo1_1_LWW_partner = []
    duo1_1_LBB_partner = []

    duo2_2_random_partner = []
    duo2_2_LW_partner = []
    duo2_2_LB_partner = []
    duo2_2_LWW_partner = []
    duo2_2_LBB_partner = []

    duo3_3_random_partner = []
    duo3_3_LW_partner = []
    duo3_3_LB_partner = []
    duo3_3_LWW_partner = []
    duo3_3_LBB_partner = []

    duo5_5_random_partner = []
    duo5_5_LW_partner = []
    duo5_5_LB_partner = []
    duo5_5_LWW_partner = []
    duo5_5_LBB_partner = []

    for file in result_files:
        _, results = parse_file("tests/" + file)
        mode1, mode2, mode3 = parse_filename(file)
        for result in results:
            duo_partner = result["duo"][1] if result["duo"][0] == 1 else result["duo"][0]
            if mode1 == "1_1":
                if 1 in result["duo"]:
                    if mode2 == "random" and mode3 == "random":
                        duo1_1_random.append(result["points"][1])
                        duo1_1_random_partner.append(result["points"][duo_partner])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo1_1_LW.append(result["points"][1])
                        duo1_1_LW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo1_1_LB.append(result["points"][1])
                        duo1_1_LB_partner.append(result["points"][duo_partner])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo1_1_LWW.append(result["points"][1])
                        duo1_1_LWW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo1_1_LBB.append(result["points"][1])
                        duo1_1_LBB_partner.append(result["points"][duo_partner])
                    else:
                        continue
            elif mode1 == "2_2":
                if 1 in result["duo"]:
                    if mode2 == "random" and mode3 == "random":
                        duo2_2_random.append(result["points"][1])
                        duo2_2_random_partner.append(result["points"][duo_partner])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo2_2_LW.append(result["points"][1])
                        duo2_2_LW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo2_2_LB.append(result["points"][1])
                        duo2_2_LB_partner.append(result["points"][duo_partner])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo2_2_LWW.append(result["points"][1])
                        duo2_2_LWW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo2_2_LBB.append(result["points"][1])
                        duo2_2_LBB_partner.append(result["points"][duo_partner])
                    else:
                        continue
            elif mode1 == "3_3":
                if 1 in result["duo"]:
                    if mode2 == "random" and mode3 == "random":
                        duo3_3_random.append(result["points"][1])
                        duo3_3_random_partner.append(result["points"][duo_partner])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo3_3_LW.append(result["points"][1])
                        duo3_3_LW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo3_3_LB.append(result["points"][1])
                        duo3_3_LB_partner.append(result["points"][duo_partner])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo3_3_LWW.append(result["points"][1])
                        duo3_3_LWW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo3_3_LBB.append(result["points"][1])
                        duo3_3_LBB_partner.append(result["points"][duo_partner])
                    else:
                        continue
            elif mode1 == "5_5":
                if 1 in result["duo"]:
                    if mode2 == "random" and mode3 == "random":
                        duo5_5_random.append(result["points"][1])
                        duo5_5_random_partner.append(result["points"][duo_partner])
                    elif mode2 == "LW" and mode3 == "LW":
                        duo5_5_LW.append(result["points"][1])
                        duo5_5_LW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LB" and mode3 == "LB":
                        duo5_5_LB.append(result["points"][1])
                        duo5_5_LB_partner.append(result["points"][duo_partner])
                    elif mode2 == "LWW" and mode3 == "LWW":
                        duo5_5_LWW.append(result["points"][1])
                        duo5_5_LWW_partner.append(result["points"][duo_partner])
                    elif mode2 == "LBB" and mode3 == "LBB":
                        duo5_5_LBB.append(result["points"][1])
                        duo5_5_LBB_partner.append(result["points"][duo_partner])
                    else:
                        continue
            else:
                continue

    print(sum(duo1_1_random) / len(duo1_1_random))
    print(sum(duo1_1_LW) / len(duo1_1_LW))
    print(sum(duo1_1_LB) / len(duo1_1_LB))
    print(sum(duo1_1_LWW) / len(duo1_1_LWW))
    print(sum(duo1_1_LBB) / len(duo1_1_LBB))

    print(sum(duo2_2_random) / len(duo2_2_random))
    print(sum(duo2_2_LW) / len(duo2_2_LW))
    print(sum(duo2_2_LB) / len(duo2_2_LB))
    print(sum(duo2_2_LWW) / len(duo2_2_LWW))
    print(sum(duo2_2_LBB) / len(duo2_2_LBB))

    print(sum(duo3_3_random) / len(duo3_3_random))
    print(sum(duo3_3_LW) / len(duo3_3_LW))
    print(sum(duo3_3_LB) / len(duo3_3_LB))
    print(sum(duo3_3_LWW) / len(duo3_3_LWW))
    print(sum(duo3_3_LBB) / len(duo3_3_LBB))

    print(sum(duo5_5_random) / len(duo5_5_random))
    print(sum(duo5_5_LW) / len(duo5_5_LW))
    print(sum(duo5_5_LB) / len(duo5_5_LB))
    print(sum(duo5_5_LWW) / len(duo5_5_LWW))
    print(sum(duo5_5_LBB) / len(duo5_5_LBB))

    print(sum(duo1_1_random_partner) / len(duo1_1_random_partner))
    print(sum(duo1_1_LW_partner) / len(duo1_1_LW_partner))
    print(sum(duo1_1_LB_partner) / len(duo1_1_LB_partner))
    print(sum(duo1_1_LWW_partner) / len(duo1_1_LWW_partner))
    print(sum(duo1_1_LBB_partner) / len(duo1_1_LBB_partner))

    print(sum(duo2_2_random_partner) / len(duo2_2_random_partner))
    print(sum(duo2_2_LW_partner) / len(duo2_2_LW_partner))
    print(sum(duo2_2_LB_partner) / len(duo2_2_LB_partner))
    print(sum(duo2_2_LWW_partner) / len(duo2_2_LWW_partner))
    print(sum(duo2_2_LBB_partner) / len(duo2_2_LBB_partner))

    print(sum(duo3_3_random_partner) / len(duo3_3_random_partner))
    print(sum(duo3_3_LW_partner) / len(duo3_3_LW_partner))
    print(sum(duo3_3_LB_partner) / len(duo3_3_LB_partner))
    print(sum(duo3_3_LWW_partner) / len(duo3_3_LWW_partner))
    print(sum(duo3_3_LBB_partner) / len(duo3_3_LBB_partner))

    print(sum(duo5_5_random_partner) / len(duo5_5_random_partner))
    print(sum(duo5_5_LW_partner) / len(duo5_5_LW_partner))
    print(sum(duo5_5_LB_partner) / len(duo5_5_LB_partner))
    print(sum(duo5_5_LWW_partner) / len(duo5_5_LWW_partner))
    print(sum(duo5_5_LBB_partner) / len(duo5_5_LBB_partner))"""

    duo_1_1 = [22.961077844311376,
    25.828869047619047,
    22.109737248840805,
    25.595975232198143,
    20.41585535465925]
    duo_2_2 = [23.40381791483113,
    26.038819875776397,
    23.446130500758727,
    26.23716012084592,
    20.202962962962964]
    duo_3_3 = [23.073170731707318,
    26.19601837672282,
    23.128205128205128,
    26.826151560178307,
    20.95625]
    duo_5_5 = [22.55640243902439,
    25.790178571428573,
    23.496996996996998,
    25.39644970414201,
    20.053571428571427]
    duo_1_1_partner = [19.778443113772454,
    18.479166666666668,
    20.017001545595054,
    18.809597523219814,
    20.603616133518777]
    duo_2_2_partner = [19.387665198237887,
    17.964285714285715,
    19.558421851289832,
    18.338368580060422,
    20.50814814814815]
    duo_3_3_partner = [19.45579268292683,
    18.48238897396631,
    20.42835595776772,
    17.61961367013373,
    19.978125]

    duo_5_5_partner = [19.70731707317073,
    19.322916666666668,
    18.97897897897898,
    19.17751479289941,
    20.78422619047619]

    print("QAGENTs PARTNER SCORES")
    xxx = sorted(zip(duo_1_1_partner, play_modes))
    print(xxx)
    data = [x for x,y in xxx]
    labels = [y for x, y in xxx]
    plot(data, labels, "Scores of partners of 1_1 Q agent vs theoretical agents", "Agents", "Points")
    yyy = sorted(zip(duo_2_2_partner, play_modes))
    print(yyy)
    data = [x for x, y in yyy]
    labels = [y for x, y in yyy]
    plot(data, labels, "Scores of partners of 2_2 Q agent vs theoretical agents", "Agents", "Points")
    zzz = sorted(zip(duo_3_3_partner, play_modes))
    print(zzz)
    data = [x for x, y in zzz]
    labels = [y for x, y in zzz]
    plot(data, labels, "Scores of partners of 3_3 Q agent vs theoretical agents", "Agents", "Points")
    www = sorted(zip(duo_5_5_partner, play_modes))
    print(www)
    data = [x for x, y in www]
    labels = [y for x, y in www]
    plot(data, labels, "Scores of partners of 5_5 Q agent vs theoretical agents", "Agents", "Points")
    print("---------------------------------------")

