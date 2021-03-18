import pickle
import copy

from TarockBasics import TarockBasics
from GameStateTarock import GameStateTarock
from MilestoneAgents import MilestoneAgents

from probamo import index

import matplotlib.pyplot as plt


from os import listdir
from os.path import isfile, join

gst = GameStateTarock([], [], [], [1,2,3], 1, [2,3])
tb = TarockBasics()
MODELS = ["1_1", "2_2", "3_3", "5_5"]


def get_files(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def get_playing_order(starting_player):
    players = [1,2,3]
    players2 = players + players

    second_player = players2[players2.index(starting_player) + 1]
    third_player = players2[players2.index(starting_player) + 2]

    return starting_player, second_player, third_player

def index_results():
    index = {"1_1": {"Solo brez": {"0": [], "1": [], "2": []}, "Naprej": {"0": [], "1": [], "2": []}},
            "2_2": {"Solo brez": {"0": [], "1": [], "2": []}, "Naprej": {"0": [], "1": [], "2": []}},
            "3_3": {"Solo brez": {"0": [], "1": [], "2": []}, "Naprej": {"0": [], "1": [], "2": []}},
            "5_5": {"Solo brez": {"0": [], "1": [], "2": []}, "Naprej": {"0": [], "1": [], "2": []}}
            }

    for model in MODELS:
        naprej_count = 0
        solobrez_count = 0
        for filename in get_files("siciljasti_tarokist/Results/" + model + "/"):
            file_obj = open("siciljasti_tarokist/Results/" + model + "/" + filename, "rb")

            msa, game, starting_player = pickle.load(file_obj)

            if game == "Naprej" and naprej_count < 50:
                player_hands, player_points = reconstruct_hands(msa.discard, msa.duo)

                current_game = {"player hands": player_hands, "discard": msa.discard, 
                "points": player_points, "duo": msa.duo}

                cq = good_cards(player_hands[1])

                index[model][game][str(cq)].append(current_game)
                naprej_count += 1
            
            if game == "Solo brez" and solobrez_count < 50:
                player_hands, player_points = reconstruct_hands(msa.discard, msa.duo)

                current_game = {"player hands": player_hands, "discard": msa.discard, 
                "points": player_points, "duo": msa.duo}

                cq = good_cards(player_hands[1])

                index[model][game][str(cq)].append(current_game)
                solobrez_count += 1

    return index

def reconstruct_hands(discard, duo):
    starting_player = {1,2,3}.difference(set(duo)).pop()
    
    starting_player, second_player, third_player = get_playing_order(starting_player)

    player_hands = {1: [], 2: [], 3: []}
    player_points = {1: 0, 2: 0, 3: 0}
    for stack in discard[1:]:
        
        
        player_hands[starting_player].append(stack[0]) 
        player_hands[second_player].append(stack[1]) 
        player_hands[third_player].append(stack[2]) 

        player_order = [starting_player, second_player, third_player]
        
        win_index = gst.winning_card(stack)
        starting_player = player_order[win_index]
        player_points[starting_player] += gst.eval_stack(stack)
        starting_player, second_player, third_player = get_playing_order(starting_player)
    
    return player_hands, player_points

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

def avg_points(games, player=1, solo=None):
    """
    1 games format:

    {'player hands': {1: [18, 28, 8, 47, 50, 58, 49, 44, 45, 4, 61, 52, 41, 51, 59, 24], 2: [17, 27, 6, 43, 53, 38, 60, 15, 26, 1, 25, 35, 22, 31, 32, 34], 3: [11, 21, 2, 42, 48, 33, 54, 13, 55, 3, 56, 14, 23, 5, 16, 7]}, 
    'discard': [[12, 36, 37, 40, 46, 57], [17, 11, 18], [28, 27, 21], [8, 6, 2], [47, 43, 42], [50, 53, 48], [38, 33, 58], [49, 60, 54], [15, 13, 44], [45, 26, 55], [3, 4, 1], [61, 25, 56], [52, 35, 14], [41, 22, 23], [51, 31, 5], [59, 32, 16], [24, 34, 7]], 
    'points': {1: 50, 2: 6, 3: 3}, 
    'duo': [1, 3]}
    """
    if solo == None:
        tocke = [game["points"][player] for game in games]
    elif solo == True:
        tocke = [game["points"][player] for game in games if player not in game["duo"]]
    elif solo == False:
        tocke = [game["points"][player] for game in games if player in game["duo"]]
    else:
        raise NotImplementedError

    if len(tocke) > 0:
        return sum(tocke)/len(tocke)
    else:
        return 0

def overall_averages(index):
    naprej_povprecja = []
    solobrez_povprecja = []

    for model in MODELS:
        games_naprej = index[model]["Naprej"]["0"] + index[model]["Naprej"]["1"] + index[model]["Naprej"]["2"]
        naprej_povprecja.append((model, avg_points(games_naprej)))

        games_solobrez = index[model]["Solo brez"]["0"] + index[model]["Solo brez"]["1"] + index[model]["Solo brez"]["2"]
        solobrez_povprecja.append((model, avg_points(games_solobrez)))
    

    fig, axs = plt.subplots(1,2)
    fig.suptitle("Best performing models playing with Silicijasti tarokist")
    fig.text(0.5, 0.02, 'Models', ha='center')
    fig.text(0.08, 0.5, 'Average points per game', va='center', rotation='vertical')   

    urejeno_naprej = list(sorted(naprej_povprecja, key= lambda x: x[1]))
    values_naprej = [x[1] for x in urejeno_naprej]
    names_naprej = [x[0] for x in urejeno_naprej]

    urejeno_solobrez = list(sorted(solobrez_povprecja, key= lambda x: x[1]))
    values_solobrez = [x[1] for x in urejeno_solobrez]
    names_solobrez = [x[0] for x in urejeno_solobrez]

    axs[0].bar(names_naprej, values_naprej)
    axs[0].title.set_text("Playing duo")
    #active_axis.set_ylim([7, 35])
    #active_axis.set_ylabel("Average points per game")
    #active_axis.set_xlabel("Model variations")
    axs[0].set_xticklabels(names_naprej, rotation = -45)

    axs[1].bar(names_solobrez, values_solobrez)
    axs[1].title.set_text("Playing solo")
    #active_axis.set_ylim([7, 35])
    #active_axis.set_ylabel("Average points per game")
    #active_axis.set_xlabel("Model variations")
    axs[1].set_xticklabels(names_solobrez, rotation = -45)
    plt.show()


def overall_averages_with_cq(index):
    naprej_povprecja_0 = []
    naprej_povprecja_1 = []
    naprej_povprecja_2 = []
    solobrez_povprecja_0 = []
    solobrez_povprecja_1 = []
    solobrez_povprecja_2 = []

    for model in MODELS:
        games_naprej_0 = index[model]["Naprej"]["0"] 
        games_naprej_1 = index[model]["Naprej"]["1"]
        games_naprej_2 = index[model]["Naprej"]["2"]
        naprej_povprecja_0.append((model, avg_points(games_naprej_0)))
        naprej_povprecja_1.append((model, avg_points(games_naprej_1)))
        naprej_povprecja_2.append((model, avg_points(games_naprej_2)))

        games_solobrez_0 = index[model]["Solo brez"]["0"]
        games_solobrez_1 = index[model]["Solo brez"]["1"]
        games_solobrez_2 = index[model]["Solo brez"]["2"]
        solobrez_povprecja_0.append((model, avg_points(games_solobrez_0)))
        solobrez_povprecja_1.append((model, avg_points(games_solobrez_1)))
        solobrez_povprecja_2.append((model, avg_points(games_solobrez_2)))
    

    fig, axs = plt.subplots(1,2)
    fig.suptitle("Best performing models playing with Silicijasti tarokist with respect to quality of cards")
    fig.text(0.5, 0.02, 'Models', ha='center')
    fig.text(0.08, 0.5, 'Average points per game', va='center', rotation='vertical')   

    urejeno_naprej_0 = list(sorted(naprej_povprecja_0, key= lambda x: x[1]))
    values_naprej_0 = [x[1] for x in urejeno_naprej_0]
    names_naprej_0 = [x[0] for x in urejeno_naprej_0]
    
    urejeno_naprej_1 = list(sorted(naprej_povprecja_1, key= lambda x: x[1]))
    values_naprej_1 = [x[1] for x in urejeno_naprej_1]
    names_naprej_1 = [x[0] + " " for x in urejeno_naprej_1]

    urejeno_naprej_2 = list(sorted(naprej_povprecja_2, key= lambda x: x[1]))
    values_naprej_2 = [x[1] for x in urejeno_naprej_2]
    names_naprej_2 = [x[0] + "  " for x in urejeno_naprej_2]
    
    urejeno_solobrez_0 = list(sorted(solobrez_povprecja_0, key= lambda x: x[1]))
    values_solobrez_0 = [x[1] for x in urejeno_solobrez_0]
    names_solobrez_0 = [x[0] for x in urejeno_solobrez_0]

    urejeno_solobrez_1 = list(sorted(solobrez_povprecja_1, key= lambda x: x[1]))
    values_solobrez_1 = [x[1] for x in urejeno_solobrez_1]
    names_solobrez_1 = [x[0] + " " for x in urejeno_solobrez_1]

    urejeno_solobrez_2 = list(sorted(solobrez_povprecja_2, key= lambda x: x[1]))
    values_solobrez_2 = [x[1] for x in urejeno_solobrez_2]
    names_solobrez_2 = [x[0] + "  " for x in urejeno_solobrez_2]

    axs[0].bar(names_naprej_0, values_naprej_0, label="Any cards")
    axs[0].bar(names_naprej_1, values_naprej_2, label="Good cards")
    axs[0].bar(names_naprej_2, values_naprej_2, label="Great cards")
    axs[0].title.set_text("Playing duo")
    #active_axis.set_ylim([7, 35])
    #active_axis.set_ylabel("Average points per game")
    #active_axis.set_xlabel("Model variations")
    axs[0].set_xticklabels(names_naprej_0 + names_naprej_1 + names_naprej_2, rotation = -45)

    axs[1].bar(names_solobrez_0, values_solobrez_0, label="Any cards")
    axs[1].bar(names_solobrez_1, values_solobrez_1, label="Good cards")
    axs[1].bar(names_solobrez_2, values_solobrez_2, label="Great cards")
    axs[1].title.set_text("Playing solo")
    #active_axis.set_ylim([7, 35])
    #active_axis.set_ylabel("Average points per game")
    #active_axis.set_xlabel("Model variations")
    axs[1].set_xticklabels(names_solobrez_0 + names_solobrez_1 + names_solobrez_2, rotation = -45)
    plt.legend(loc="upper right")
    plt.show()
        



if __name__ == "__main__":
    index = index_results()

    overall_averages(index)
    overall_averages_with_cq(index)