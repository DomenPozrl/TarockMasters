from QLearning import *
from GameStateTarock import *
from get_states_GST_functions import *
from action_functions import *


#Q tables
solo_first = None
solo_second = None
solo_third = None
duo_first = None
duo_second = None
duo_third = None

#get states functions
solo_first_fun = None
solo_second_fun = None
solo_third_fun = None
duo_first_fun = None
duo_second_fun = None
duo_third_fun = None


#action functions
solo_first_action = None
solo_first_action_len = 0
solo_second_action = None
solo_second_action_len = 0
solo_third_action = None
solo_third_action_len = 0
duo_first_action = None
duo_first_action_len = 0
duo_second_action = None
duo_second_action_len = 0
duo_third_action = None
duo_third_action_len = 0

def set_table_function_vars_version1():
    #get states version1 tables
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    solo_first = dict()
    solo_second = dict()
    solo_third = solo_second
    duo_first = solo_first
    duo_second = solo_second
    duo_third = solo_third

    #get states version1 functions
    solo_first_fun = get_state_version1_open
    solo_second_fun = get_state_version1_play
    solo_third_fun = solo_second_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_second_fun
    duo_third_fun = solo_third_fun

def load_table_function_vars_version1(filename1, filename2):
    #get states version1 tables
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    file1 = open(filename1, "rb")
    file2 = open(filename2, "rb")

    solo_first = pickle.load(file1)
    solo_second = pickle.load(file2)
    file1.close()
    file2.close()

    solo_third = solo_second
    duo_first = solo_first
    duo_second = solo_second
    duo_third = solo_third

    #get states version1 functions
    solo_first_fun = get_state_version1_open
    solo_second_fun = get_state_version1_play
    solo_third_fun = solo_second_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_second_fun
    duo_third_fun = solo_third_fun

def set_table_function_vars_version2():
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version2 tables
    solo_first = dict()
    solo_second = solo_first
    solo_third = solo_first
    duo_first = solo_first
    duo_second = solo_first
    duo_third = solo_first

    #get states version2 functions
    solo_first_fun = get_state_version2
    solo_second_fun = solo_first_fun
    solo_third_fun = solo_first_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_first_fun
    duo_third_fun = solo_first_fun

def load_table_function_vars_version2(filename1):
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version2 tables
    file1 = open(filename1, "rb")
    solo_first = pickle.load(file1)
    file1.close()

    solo_second = solo_first
    solo_third = solo_first
    duo_first = solo_first
    duo_second = solo_first
    duo_third = solo_first

    #get states version2 functions
    solo_first_fun = get_state_version2
    solo_second_fun = solo_first_fun
    solo_third_fun = solo_first_fun
    duo_first_fun = solo_first_fun
    duo_second_fun = solo_first_fun
    duo_third_fun = solo_first_fun

def set_table_function_vars_version3():
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version3 tables
    solo_first = dict()
    solo_second = dict()
    solo_third = dict()
    duo_first = dict()
    duo_second = dict()
    duo_third = dict()

    #get states version3 functions
    solo_first_fun = get_state_version3_solo_open
    solo_second_fun = get_state_version3_solo_second
    solo_third_fun = get_state_version3_solo_third
    duo_first_fun = get_state_version3_duo_open
    duo_second_fun = get_state_version3_duo_second
    duo_third_fun = get_state_version3_duo_third


def load_table_function_vars_version3(filename1, filename2, filename3, filename4, filename5, filename6):
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    file1 = open(filename1, "rb")
    file2 = open(filename2, "rb")
    file3 = open(filename3, "rb")
    file4 = open(filename4, "rb")
    file5 = open(filename5, "rb")
    file6 = open(filename6, "rb")

    #get states version3 tables
    solo_first = pickle.load(file1)
    solo_second = pickle.load(file2)
    solo_third = pickle.load(file3)
    duo_first = pickle.load(file4)
    duo_second = pickle.load(file5)
    duo_third = pickle.load(file6)

    file1.close()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()

    #get states version3 functions
    solo_first_fun = get_state_version3_solo_open
    solo_second_fun = get_state_version3_solo_second
    solo_third_fun = get_state_version3_solo_third
    duo_first_fun = get_state_version3_duo_open
    duo_second_fun = get_state_version3_duo_second
    duo_third_fun = get_state_version3_duo_third

def set_action_vars_version1():
    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version1_open
    solo_first_action_len = len(ACTIONS_VERSION1_OPEN)

    solo_second_action = get_actions_version1_play
    solo_second_action_len = len(ACTIONS_VERSION1_PLAY)

    solo_third_action = solo_second_action
    solo_third_action_len = solo_second_action_len


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len

def set_action_vars_version2():

    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version2
    solo_first_action_len = len(ACTIONS_VERSION2)

    solo_second_action = get_actions_version2
    solo_second_action_len = len(ACTIONS_VERSION2)

    solo_third_action = solo_second_action
    solo_third_action_len = solo_first_action_len


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len

def set_action_vars_version3():
    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version3_open
    solo_first_action_len = len(ACTIONS_VERSION3_OPEN)

    solo_second_action = get_actions_version3_play
    solo_second_action_len = len(ACTIONS_VERSION3_PLAY)

    solo_third_action = solo_second_action
    solo_third_action_len = solo_second_action_len


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len

def set_table_function_vars_version5():
    global solo_first
    global solo_second
    global solo_third
    global duo_first
    global duo_second
    global duo_third
    global solo_first_fun
    global solo_second_fun
    global solo_third_fun
    global duo_first_fun
    global duo_second_fun
    global duo_third_fun

    #get states version2 tables
    solo_first = dict()
    solo_second = dict()
    solo_third = dict()
    duo_first = dict()
    duo_second = dict()
    duo_third = dict()

    #get states version2 functions
    solo_first_fun = get_state_version5_solo_open
    solo_second_fun = get_state_version5_solo_second
    solo_third_fun = get_state_version5_solo_third
    duo_first_fun = get_state_version5_duo_open
    duo_second_fun = get_state_version5_duo_second
    duo_third_fun = get_state_version5_duo_third

def set_action_vars_version5():
    global solo_first_action
    global solo_second_action
    global solo_third_action
    global duo_first_action
    global duo_second_action
    global duo_third_action
    global solo_first_action_len
    global solo_second_action_len
    global solo_third_action_len
    global duo_first_action_len
    global duo_second_action_len
    global duo_third_action_len

    solo_first_action = get_actions_version5_open
    solo_first_action_len = len(ACTIONS_VERSION5_OPEN)

    solo_second_action = get_actions_version5_second
    solo_second_action_len = len(ACTIONS_VERSION5_SECOND)

    solo_third_action = get_actions_version5_third
    solo_third_action_len = len(ACTIONS_VERSION5_THIRD)


    duo_first_action = solo_first_action
    duo_first_action_len = solo_first_action_len

    duo_second_action = solo_second_action
    duo_second_action_len = solo_second_action_len

    duo_third_action = solo_third_action
    duo_third_action_len = solo_third_action_len

def reward_function2(stack, player_order, player_hands, gst1: GameStateTarock, gst2: GameStateTarock, gst3: GameStateTarock, num_possible_actions1, num_possible_actions2, num_possible_actions3):
    p1  = player_order[0]
    p2 = player_order[1]
    p3 = player_order[2]

    solo = list(set(player_order).difference(set(gst1.duo)))[0]


    player1 = player_hands[player_order[0]] + [stack[0]]
    player2 = player_hands[player_order[1]] + [stack[1]]
    player3 = player_hands[player_order[2]] + [stack[2]]

    player1_koef = num_possible_actions1
    player2_koef = num_possible_actions2
    player3_koef = num_possible_actions3

    card1 = stack[0]
    card2 = stack[1]
    card3 = stack[2]

    stack_value = gst.eval_stack(stack)
    winner = player_order[gst.winning_card(stack)]
    duo_win = True if winner in gst.duo else False

    rw1 = stack_value if p1 == winner or (p1 in gst1.duo and duo_win) else -1 * stack_value

    #player1
    if p1 in gst1.duo:
        #p1 je v duo
        p1_partner = list(set(gst1.duo).difference({p1}))[0]

        #nagradimo ce igra kralja neglede na to a je nas zadnji al predzadnji
        if card1 in [8, 18, 28, 38]:
            rw1 += 3

        if p3 in gst1.duo:
            #p3 je v duo, sepravi v primerih ko smo mi prvi in zadnji
            #nagradimo, če smo igrali barvo, katere je škrt naš zadnji
            if gst1.isHeart(card1) and gst1.players_skrti[p3]["heart"]:
                rw1 += 2
            if gst1.isDiamond(card1) and gst1.players_skrti[p3]["diamond"]:
                rw1 += 2
            if gst1.isSpade(card1) and gst1.players_skrti[p3]["spade"]:
                rw1 += 2
            if gst1.isClub(card1) and gst1.players_skrti[p3]["club"]:
                rw1 += 2
        else:
            # nagradimo, če smo igrali barvo, katere je škrt naš drugi
            # nagradimo manj kot če je zadnji, ker je slabsi strat
            if gst1.isHeart(card1) and gst1.players_skrti[p2]["heart"]:
                rw1 += 1
            if gst1.isDiamond(card1) and gst1.players_skrti[p2]["diamond"]:
                rw1 += 1
            if gst1.isSpade(card1) and gst1.players_skrti[p2]["spade"]:
                rw1 += 1
            if gst1.isClub(card1) and gst1.players_skrti[p2]["club"]:
                rw1 += 1

        #kaznujemo če je igral nekej kar ve da je škrt nasprotnik
        if gst1.isHeart(card1) and gst1.players_skrti[solo]["heart"]:
            rw1 -= 2
        if gst1.isDiamond(card1) and gst1.players_skrti[solo]["diamond"]:
            rw1 -= 2
        if gst1.isSpade(card1) and gst1.players_skrti[solo]["spade"]:
            rw1 -= 2
        if gst1.isClub(card1) and gst1.players_skrti[solo]["club"]:
            rw1 -= 2

        #še bolj kaznujemo, če je igral nekej kar ve da je škrt nasprotnik in ni škrt kolega
        if gst1.isHeart(card1) and gst1.players_skrti[solo]["heart"] and not gst1.players_skrti[p1_partner]["heart"]:
            rw1 -= 3
        if gst1.isDiamond(card1) and gst1.players_skrti[solo]["diamond"] and not gst1.players_skrti[p1_partner]["diamond"]:
            rw1 -= 3
        if gst1.isSpade(card1) and gst1.players_skrti[solo]["spade"] and not gst1.players_skrti[p1_partner]["spade"]:
            rw1 -= 3
        if gst1.isClub(card1) and gst1.players_skrti[solo]["club"] and not gst1.players_skrti[p1_partner]["club"]:
            rw1 -= 3

        rw1 *= player1_koef
    else:
        #nagrada ce igra kralja
        if card1 in [8, 18, 28, 38]:
            rw1 += 3

        #kazen ce igra barvo k vemo da je kdo od njiju skrt
        if gst1.isHeart(card1) and (gst1.players_skrti[p2]["heart"] or gst1.players_skrti[p3]["heart"]):
            rw1 -= 3
        if gst1.isDiamond(card1) and (gst1.players_skrti[p2]["diamond"] or gst1.players_skrti[p3]["diamond"]):
            rw1 -= 3
        if gst1.isSpade(card1) and (gst1.players_skrti[p2]["spade"] or gst1.players_skrti[p3]["spade"]):
            rw1 -= 3
        if gst1.isClub(card1) and (gst1.players_skrti[p2]["club"] or gst1.players_skrti[p3]["club"]):
            rw1 -= 3

        rw1 *= player1_koef

    rw2 = stack_value if p2 == winner or (p2 in gst2.duo and duo_win) else -1 * stack_value


    #player2
    if p2 in gst2.duo:

        p2_partner = list(set(gst2.duo).difference(set([p2])))[0]
        legal = gst2.legal_moves(card1, player2)
        can = gst2.can_pickup_stack([card1], player2)

        if gst2.isHeart(card1):
            barva = "heart"
        elif gst2.isDiamond(card1):
            barva = "diamond"
        elif gst2.isSpade(card1):
            barva = "spade"
        elif gst2.isClub(card1):
            barva = "club"
        else:
            barva = "tarock"

        #ce je player3 moj duo
        if p3 == p2_partner:
            if gst2.players_skrti[p3][barva]:
                if card2 != max(legal):
                    rw2 -= 1
            else:
                if card1 in [8, 18, 28, 38]:
                    if card2 != min(legal):
                        rw2 -= 1
        else:
            if gst2.players_skrti[p3][barva]:
                if card2 != min(legal):
                    rw2 -= 1
            else:
                if card1 in [8, 18, 28, 38]:
                    if card2 != max(legal):
                        rw2 -= 1
        rw2 *= player2_koef
    else:

        #če ve da je nasledni skrt pa igra visoko k bi lahko nizko
        legal = gst2.legal_moves(card1, player2)
        can = gst2.can_pickup_stack([card1], player2)

        #smo mi škrti?
        p2_skrt = any([gst2.isTarock(karta) for karta in legal])
        if gst2.players_skrti[p3]:
            if not p2_skrt:
                if gst2.id_to_points[card2] > gst2.id_to_points[min(legal)]:
                    rw2 -= gst2.id_to_points[card2]
        else:
            if len(can) > 0:
                if card2 not in can:
                    rw2 -= 2

        rw2 *= player2_koef


    rw3 = stack_value if p3 == winner or (p3 in gst3.duo and duo_win) else -1 * stack_value
    if p3 in gst3.duo:
        legal = gst2.legal_moves(card1, player2)
        can = gst2.can_pickup_stack([card1], player2)

        p3_partner = list(set(gst3.duo).difference(set([p3])))[0]

        if gst3.current_winning_player == p3_partner:
            if card3 != max(legal):
                rw3 -= 1
        else:
            if len(can) == 0:
                if gst3.id_to_points[card3] != gst3.id_to_points[min(legal)]:
                    rw3 -= 2
            else:
                if card3 not in can:
                    rw3 -= 2
        rw3 *= player3_koef
    else:
        legal = gst2.legal_moves(card1, player2)
        can = gst2.can_pickup_stack([card1], player2)

        if len(can) > 0:
            if card3 > min(can):
                rw3 -= 1
            if card3 not in can:
                rw3 -= 2
        rw3 *= player3_koef


    return rw1, rw2, rw3


def reward_function3(discard, player_hands):
    print("Hello, world!")
    prvi_trio = discard[0]





if __name__ == "__main__":

    qlearning = QLearning(1, 0.1, 0.2)
    num_games = 1000000
    count = 0
    

    #cant combine action vars1 and vars3 with table vars2
    #that is because q table for version2 has only 1 table but the previously mentioned actions have two different size vectors
    #so this is a no go

    set_table_function_vars_version5()
    set_action_vars_version5()
    #print(solo_first, solo_second, solo_third, duo_first, duo_second, duo_third)
    while count < num_games:
        print(count/num_games)

        #deal cards
        tb = TarockBasics()
        p1, p2, p3, talon = tb.deal_cards()

        #init the game state
        gst = GameStateTarock(p1, p2, p3, [1,2,3], 1, [2,3])

        #update the state according to talon cards
        gst.update_state_talon(talon)


        #play while there are still cards in p1
        while p1:

            first = gst.player_order[0]
            second = gst.player_order[1]
            third = gst.player_order[2]

            po = [copy.deepcopy(first), copy.deepcopy(second), copy.deepcopy(third)]
            gst1 = copy.deepcopy(gst)
            #first player plays
            if first not in gst.duo:

                #get state
                state1 = solo_first_fun(first, gst)

                #current vector of q table for this state
                if state1 in solo_first:
                    vector = solo_first[state1]
                else:
                    vector = [0 for i in range(solo_first_action_len)]
                    solo_first[state1] = vector

                #get card
                rez = solo_first_action(vector, gst.player_hands[first], gst)
                card, action_index1, num_possible_actions1 = qlearning.choose_action(rez)
                gst.update_state(card, first)
            else:
                state1 = duo_first_fun(first, gst)

                # current vector of q table for this state
                if state1 in duo_first:
                    vector = duo_first[state1]
                else:
                    vector = [0 for i in range(duo_first_action_len)]
                    duo_first[state1] = vector

                # get card
                rez = duo_first_action(vector, gst.player_hands[first], gst)
                card, action_index1, num_possible_actions1 = qlearning.choose_action(rez)
                gst.update_state(card, first)

            gst2 = copy.deepcopy(gst)
            # second player plays
            if second not in gst.duo:

                state2 = solo_second_fun(second, gst)

                # current vector of q table for this state
                if state2 in solo_second:
                    vector = solo_second[state2]
                else:
                    vector = [0 for i in range(solo_second_action_len)]
                    solo_second[state2] = vector

                # get card
                rez = solo_second_action(vector, gst.player_hands[second], gst)
                card, action_index2, num_possible_actions2 = qlearning.choose_action(rez)
                gst.update_state(card, second)

            else:
                state2 = duo_second_fun(second, gst)

                # current vector of q table for this state
                if state2 in duo_second:
                    vector = duo_second[state2]
                else:
                    vector = [0 for i in range(duo_second_action_len)]
                    duo_second[state2] = vector

                # get card
                # print(vector, gst.player_hands[second])
                rez = duo_second_action(vector, gst.player_hands[second], gst)
                card, action_index2, num_possible_actions2 = qlearning.choose_action(rez)
                gst.update_state(card, second)

            gst3 = copy.deepcopy(gst)
            # third player plays
            if third not in gst.duo:
                state3 = solo_third_fun(third, gst)

                # current vector of q table for this state
                if state3 in solo_third:
                    vector = solo_third[state3]
                else:
                    vector = [0 for i in range(solo_third_action_len)]
                    solo_third[state3] = vector

                # get card
                rez = solo_third_action(vector, gst.player_hands[third], gst)
                card, action_index3, num_possible_actions3 = qlearning.choose_action(rez)
                gst.update_state(card, third)

            else:
                state3 = duo_third_fun(third, gst)

                # current vector of q table for this state
                if state3 in duo_third:
                    vector = duo_third[state3]
                else:
                    vector = [0 for i in range(duo_third_action_len)]
                    duo_third[state3] = vector

                # get card
                rez = duo_third_action(vector, gst.player_hands[third], gst)
                card, action_index3, num_possible_actions3 = qlearning.choose_action(rez)
                gst.update_state(card, third)

            #zaenkrat bo reward function samo točke, ki smo jih nabrali po stacku
            points = gst.eval_stack(gst.stack)
            winner = gst.current_winning_player


            # state1, action_index1, num_possible_actions1

            if first == winner:
                if first not in gst.duo:
                    qlearning.update_table(solo_first, state1, action_index1, points*num_possible_actions1)
                else:
                    qlearning.update_table(duo_first, state1, action_index1, points * num_possible_actions1)
            else:
                if first not in gst.duo:
                    qlearning.update_table(solo_first, state1, action_index1, -1*points*num_possible_actions1)
                else:
                    if winner in gst.duo:
                        qlearning.update_table(duo_first, state1, action_index1, 0.5* points * num_possible_actions1)
                    else:
                        qlearning.update_table(duo_first, state1, action_index1, -1 * 0.5 * points * num_possible_actions1)

            # state2, action_index2, num_possible_actions2
            if second == winner:
                if second not in gst.duo:
                    qlearning.update_table(solo_second, state2, action_index2, points*num_possible_actions2)
                else:
                    qlearning.update_table(duo_second, state2, action_index2, points * num_possible_actions2)
            else:
                if second not in gst.duo:
                    qlearning.update_table(solo_second, state2, action_index2, -1 * points * num_possible_actions2)
                else:
                    if winner in gst.duo:
                        qlearning.update_table(duo_second, state2, action_index2, 0.5 * points * num_possible_actions2)
                    else:
                        qlearning.update_table(duo_second, state2, action_index2, -1 * 0.5 * points * num_possible_actions2)

            # state3, action_idnex3, num_possible_actions3
            if third == winner:
                if third not in gst.duo:
                    qlearning.update_table(solo_third, state3, action_index3, points*num_possible_actions3)
                else:
                    qlearning.update_table(duo_third, state3, action_index3, points * num_possible_actions3)
            else:
                if third not in gst.duo:
                    qlearning.update_table(solo_third, state3, action_index3, -1 * points * num_possible_actions3)
                else:
                    if winner in gst.duo:
                        qlearning.update_table(duo_third, state3, action_index3, 0.5 * points * num_possible_actions3)
                    else:
                        qlearning.update_table(duo_third, state3, action_index3, -1 * 0.5 * points * num_possible_actions3)

            """#def reward_function2(stack, player_order, player_hands, gst1: GameStateTarock, gst2: GameStateTarock, gst3: GameStateTarock, num_possible_actions1, num_possible_actions2, num_possible_actions3):
            rw1, rw2, rw3 = reward_function2(gst.stack, po, gst.player_hands, gst1, gst2, gst3, num_possible_actions1, num_possible_actions2, num_possible_actions3)

            if first in gst.duo:
                qlearning.update_table(duo_first, state1, action_index1, rw1)
            else:
                qlearning.update_table(solo_first, state1, action_index1, rw1)

            if second in gst.duo:
                qlearning.update_table(duo_second, state2, action_index2, rw2)
            else:
                qlearning.update_table(solo_second, state2, action_index2, rw2)

            if third in gst.duo:
                qlearning.update_table(duo_third, state3, action_index3, rw3)
            else:
                qlearning.update_table(solo_third, state3, action_index3, rw3)"""


            gst.clear_state()


        count += 1

    qlearning.pickle_table(solo_first, "q_tables/solo_first_5_5.pickle")
    qlearning.pickle_table(solo_second, "q_tables/solo_second_5_5.pickle")
    qlearning.pickle_table(solo_third, "q_tables/solo_third_5_5.pickle")
    qlearning.pickle_table(duo_first, "q_tables/duo_first_5_5.pickle")
    qlearning.pickle_table(duo_second, "q_tables/duo_second_5_5.pickle")
    qlearning.pickle_table(duo_third, "q_tables/duo_third_5_5.pickle")