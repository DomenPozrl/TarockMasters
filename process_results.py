
import pickle
import copy

from TarockBasics import TarockBasics
from GameStateTarock import GameStateTarock
from MilestoneAgents import MilestoneAgents

from probamo import index

import matplotlib.pyplot as plt

gst = GameStateTarock([], [], [], [1,2,3], 1, [2,3])
tb = TarockBasics()


MODELS = ["1_1", "2_2", "3_3", "5_5"]
MSAS = ["LWW", "LW", "random", "LB", "LBB"]
RWFS = ["rwf1", "rwf2", "rwf3"]
QFS = ["qf1", "qf2"]
CQ = ["1", "2"]


name_preslikava ={"rwf1 qf1": "1_1", "rwf1 qf2": "1_2", "rwf2 qf1": "2_1", "rwf2 qf2": "2_2", "rwf3 qf1": "3_1", "rwf3 qf2": "3_2"}

def get_dummy_discards():
    """
    TESTED IF HAND RECONSTRUCTION WORKS CORRECTLY, IT DOES

    confs = []
    for i in range(100000):
        print(i)
        p1, p2, p3, discard, duo = get_dummy_discards()
        reconstructed_hands = reconstruct_hands(discard, duo)
        confs.append((sorted(p1) == sorted(reconstructed_hands[1])) and (sorted(p2) == sorted(reconstructed_hands[2])) and (sorted(p3) == sorted(reconstructed_hands[3])))
    
    print(all(confs))
    """


    p1, p2, p3, talon = tb.deal_cards()
    p1_copy = copy.deepcopy(p1)
    p2_copy = copy.deepcopy(p2)
    p3_copy = copy.deepcopy(p3)

    solo = 1
    duo = [2,3]
    msa = MilestoneAgents(p1, p2, p3, [1,2,3], solo, duo)
    msa.update_state_talon(talon)
    
    while p1:
        first = msa.starting_player
        second = msa.second_player
        third = msa.third_player

        card1 = msa.random_agent(first)
        msa.update_state(card1, first)

        card2 = msa.random_agent(second)
        msa.update_state(card2, second)

        card3 = msa.random_agent(third)
        msa.update_state(card3, third)

        msa.clear_state()
    
    return p1_copy, p2_copy, p3_copy, msa.discard, duo


def get_playing_order(starting_player):
    players = [1,2,3]
    players2 = players + players

    second_player = players2[players2.index(starting_player) + 1]
    third_player = players2[players2.index(starting_player) + 2]

    return starting_player, second_player, third_player

def reconstruct_hands(discard, duo):
    starting_player = {1,2,3}.difference(set(duo)).pop()
    
    starting_player, second_player, third_player = get_playing_order(starting_player)

    player_hands = {1: [], 2: [], 3: []}

    for stack in discard[1:]:
        
        
        player_hands[starting_player].append(stack[0]) 
        player_hands[second_player].append(stack[1]) 
        player_hands[third_player].append(stack[2]) 

        player_order = [starting_player, second_player, third_player]
        
        win_index = gst.winning_card(stack)
        starting_player = player_order[win_index]
        starting_player, second_player, third_player = get_playing_order(starting_player)
    
    return player_hands

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

def index_results():
    file_name = "Results/"

    
    for model in ["1_1", "2_2", "3_3", "5_5"]:
        for rwf in ["rwf1", "rwf2", "rwf3"]:
            for qf in ["qf1", "qf2"]:
                for msa in ["LWW", "LW", "random", "LB", "LBB"]:
                    data = pickle.load(open(file_name  + model + "/" + rwf + "/" + qf + "/" + model + " " + msa + " " + msa + ".pickle", "rb"))
                    discards = data["discards"]
                    duos = data["duos"]
                    points = data["overall points"]

                    for i in range(15000):
                        current_game_discard = discards[i]
                        current_game_duo = duos[i]
                        current_game_points = {1: points[1][i], 2: points[2][i], 3: points[3][i]}

                        player_hands = reconstruct_hands(current_game_discard, current_game_duo)

                        current_game = {"player hands": player_hands, "discard": current_game_discard, "points": current_game_points, "duo": current_game_duo}
                        card_quality = good_cards(player_hands[1])
                        
                        key = model + " " + rwf + " " + qf + " " + msa + " " + str(card_quality)

                        index[key].append(current_game)
                    print(f"Opened: {model, rwf, qf, msa}")
    
    file = open("indexed_1v2.pickle", "wb")
    pickle.dump(index, file)
    file.close()

    return index

def select_games(index, model=None, rwf=None, qf=None, msa=None, cq=None):
    ref_points = []
    if model:
        ref_points.append(model)
    if rwf:
        ref_points.append(rwf)
    if qf:
        ref_points.append(qf)
    if msa:
        ref_points.append(msa + " ")
    if cq:
        ref_points.append(" " + cq)
    
    games = []
    names = []
    control_count = 0

    for key in index:
        if all([p in key for p in ref_points]):
            games.extend(index[key])
            for i in range(len(index[key])):
                names.append(key)
            control_count += 1
        
    return games, names
        
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

    return sum(tocke)/len(tocke)

def basic_averages(index):
    final_results = dict()

    for model in MODELS:
        final_results[model] = dict()
        for msa in MSAS:
            final_results[model][msa] =[]

    for model in MODELS:
        for msa in MSAS:
            buffer = []
            for rwf in RWFS:
                for qf in QFS:
                    games, names = select_games(index, model=model, msa=msa, rwf=rwf, qf=qf)
                    effective_name = {" ".join(name.split()[:3]) for name in names}.pop()
                    splitana = effective_name.split()
                    effective_name = name_preslikava[splitana[1] + " " + splitana[2]]
                    avg = avg_points(games)
                    buffer.append((msa, avg, effective_name))
            final_results[model][msa] = buffer
    
    print(final_results)
    for x in final_results:
        print(x)
        print("------------------------")

        fig, axs = plt.subplots(1,5)
        fig.suptitle("All variations of model " + x + " playing with milestone agents")
        fig.text(0.5, 0.02, 'Model variations', ha='center')
        fig.text(0.08, 0.5, 'Average points per game', va='center', rotation='vertical')   
        for i in range(len(MSAS)):
            msa = MSAS[i]
            povprecja = final_results[x][msa]

            urejeno = list(sorted(povprecja, key= lambda x: x[1]))
            values = [x[1] for x in urejeno]
            names = [x[2] for x in urejeno]

            active_axis = axs[i]
            active_axis.bar(names, values)
            active_axis.set_ylim([12, 32])
            #active_axis.set_ylabel("Average points per game")
            #active_axis.set_xlabel("Model variations")
            active_axis.set_xticklabels(names, rotation = -45)
            active_axis.title.set_text("Playing with 2 " + msa)
        
        plt.show()

def basic_averages_solo_duo(index):
    final_results = dict()

    for model in MODELS:
        final_results[model] = dict()
        for msa in MSAS:
            final_results[model][msa] ={"solo": [], "duo": []}

    print(final_results)
    for model in MODELS:
        for msa in MSAS:
            buffer_solo = []
            buffer_duo = []
            for rwf in RWFS:
                for qf in QFS:
                    games, names = select_games(index, model=model, msa=msa, rwf=rwf, qf=qf)
                    effective_name = {" ".join(name.split()[:3]) for name in names}.pop()
                    splitana = effective_name.split()
                    effective_name = name_preslikava[splitana[1] + " " + splitana[2]]
                    avg_solo = avg_points(games, solo=True)
                    avg_duo = avg_points(games, solo=False)
                    buffer_solo.append((msa, avg_solo, effective_name))
                    buffer_duo.append((msa, avg_duo, effective_name + " "))

            final_results[model][msa]["solo"] = buffer_solo
            final_results[model][msa]["duo"] = buffer_duo

    
    for x in final_results:
        print(x)
        print("------------------------")

        fig, axs = plt.subplots(1,5)
        fig.suptitle("All variations of model " + x + " playing with milestone agents")
        fig.text(0.5, 0.02, 'Model variations', ha='center')
        fig.text(0.08, 0.5, 'Average points per game', va='center', rotation='vertical')   
        for i in range(len(MSAS)):
            msa = MSAS[i]
            povprecja_solo = final_results[x][msa]["solo"]
            povprecja_duo = final_results[x][msa]["duo"]

            urejeno_solo = list(sorted(povprecja_solo, key= lambda x: x[1]))
            values_solo = [x[1] for x in urejeno_solo]
            names_solo = [x[2] for x in urejeno_solo]

            urejeno_duo = list(sorted(povprecja_duo, key= lambda x: x[1]))
            values_duo = [x[1] for x in urejeno_duo]
            names_duo = [x[2] for x in urejeno_duo]

            print(names_solo)
            print(names_duo)
            active_axis = axs[i]
            active_axis.bar(names_solo, values_solo, label="Solo play")
            active_axis.bar(names_duo, values_duo, label="Duo play")
            active_axis.set_ylim([7, 35])
            #active_axis.set_ylabel("Average points per game")
            #active_axis.set_xlabel("Model variations")
            active_axis.set_xticklabels(names_solo + names_duo, rotation = -45)
            active_axis.title.set_text("Playing with 2 " + msa)
        
        plt.legend(loc="upper right")
        plt.show()


def overall_averages(index):
    final_results = {msa: [] for msa in MSAS}

    for msa in MSAS:
        for model in MODELS:        
            for rwf in RWFS:
                for qf in QFS:
                    games, names = select_games(index, model=model, rwf=rwf, qf=qf, msa=msa)
                    effective_name = {" ".join(name.split()[:3]) for name in names}.pop()
                    splitana = effective_name.split()
                    effective_name = splitana[0] + "_" + name_preslikava[splitana[1] + " " + splitana[2]]

                    avg = avg_points(games)
                    final_results[msa].append((avg, effective_name))
    
    for msa in final_results:
        
        urejeno = list(sorted(final_results[msa]))
        values = [x[0] for x in urejeno]
        names = [x[1] for x in urejeno]

        plt.bar(names, values)
        plt.ylim = ([7,35])
        plt.xticks(rotation=-45)
        plt.title("All models playing with 2 " + msa)
        plt.ylabel("Average points per game")
        plt.xlabel("Models")
        plt.show()

    

def card_quality_averages_per_msa(index):
    final_results = dict()

    for model in MODELS:
        final_results[model] = dict()
        for msa in MSAS:
            final_results[model][msa] ={"0": [], "1": [], "2": []}

    print(final_results)
    for model in MODELS:
        for msa in MSAS:
            buffer_0 = []
            buffer_1 = []
            buffer_2 = []
            for rwf in RWFS:
                for qf in QFS:

                    games, names = select_games(index, model=model, msa=msa, rwf=rwf, qf=qf, cq="0")
                    effective_name = {" ".join(name.split()[:3]) for name in names}.pop()
                    splitana = effective_name.split()
                    effective_name = name_preslikava[splitana[1] + " " + splitana[2]]
                    avg = avg_points(games)
                    buffer_0.append((msa, avg, effective_name))

                    games, names = select_games(index, model=model, msa=msa, rwf=rwf, qf=qf, cq="1")
                    effective_name = {" ".join(name.split()[:3]) for name in names}.pop()
                    splitana = effective_name.split()
                    effective_name = name_preslikava[splitana[1] + " " + splitana[2]]
                    avg = avg_points(games)
                    buffer_1.append((msa, avg, effective_name + " "))


                    games, names = select_games(index, model=model, msa=msa, rwf=rwf, qf=qf, cq="2")
                    effective_name = {" ".join(name.split()[:3]) for name in names}.pop()
                    splitana = effective_name.split()
                    effective_name = name_preslikava[splitana[1] + " " + splitana[2]]
                    avg = avg_points(games)
                    buffer_2.append((msa, avg, effective_name + "  "))
                        

            final_results[model][msa]["0"] = buffer_0
            final_results[model][msa]["1"] = buffer_1
            final_results[model][msa]["2"] = buffer_2

    
    for x in final_results:
        print(x)
        print("------------------------")

        fig, axs = plt.subplots(1,5)
        fig.suptitle("All variations of model " + x + " playing with milestone agents with respect to quality of cards")
        fig.text(0.5, 0.02, 'Model variations', ha='center')
        fig.text(0.08, 0.5, 'Average points per game', va='center', rotation='vertical')   
        for i in range(len(MSAS)):
            msa = MSAS[i]
            povprecja_0 = final_results[x][msa]["0"]
            povprecja_1 = final_results[x][msa]["1"]
            povprecja_2 = final_results[x][msa]["2"]

            urejeno_0 = list(sorted(povprecja_0, key= lambda x: x[1]))
            values_0 = [x[1] for x in urejeno_0]
            names_0 = [x[2] for x in urejeno_0]

            urejeno_1 = list(sorted(povprecja_1, key= lambda x: x[1]))
            values_1 = [x[1] for x in urejeno_1]
            names_1 = [x[2] for x in urejeno_1]

            urejeno_2 = list(sorted(povprecja_2, key= lambda x: x[1]))
            values_2 = [x[1] for x in urejeno_2]
            names_2 = [x[2] for x in urejeno_2]

            active_axis = axs[i]
            active_axis.bar(names_0, values_0, label="Any cards")
            active_axis.bar(names_1, values_1, label="Good cards")
            active_axis.bar(names_2, values_2, label="Great cards")
            #active_axis.set_ylim([7, 35])
            #active_axis.set_ylabel("Average points per game")
            #active_axis.set_xlabel("Model variations")
            active_axis.set_xticklabels(names_0 + names_1 + names_2, rotation = -45)
            active_axis.title.set_text("Playing with 2 " + msa)
        
        plt.legend(loc="upper right")
        plt.show()





if __name__ == "__main__":
    #data = pickle.load(open("Results\\1_1\\rwf1\\qf1\\1_1 random random.pickle", "rb"))
    #print(data.keys())
    file_obj = open("indexed_1v2.pickle", "rb")
    index = pickle.load(file_obj)
    file_obj.close()

    basic_averages(index)
    #basic_averages_solo_duo(index)

    #overall_averages(index)
    card_quality_averages_per_msa(index)
