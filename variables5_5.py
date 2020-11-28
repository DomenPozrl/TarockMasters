import pickle
from get_states_GST_functions import *
from action_functions import *
from MilestoneAgents import *

#############################################################################################
########################################5_5##################################################
#############################################################################################
#Q tables
solo_first_5_5 = pickle.load(open("q_tables/solo_first_5_5.pickle", "rb"))
solo_second_5_5 = pickle.load(open("q_tables/solo_second_5_5.pickle", "rb"))
solo_third_5_5 = pickle.load(open("q_tables/solo_third_5_5.pickle", "rb"))
duo_first_5_5 = pickle.load(open("q_tables/duo_first_5_5.pickle", "rb"))
duo_second_5_5 = pickle.load(open("q_tables/duo_second_5_5.pickle", "rb"))
duo_third_5_5 = pickle.load(open("q_tables/duo_third_5_5.pickle", "rb"))

#get states version2 functions
solo_first_fun_5_5 = get_state_version5_solo_open
solo_second_fun_5_5 = get_state_version5_solo_second
solo_third_fun_5_5 = get_state_version5_solo_third
duo_first_fun_5_5 = get_state_version5_duo_open
duo_second_fun_5_5 = get_state_version5_duo_second
duo_third_fun_5_5 = get_state_version5_duo_third

solo_first_action_5_5 = get_actions_version5_open
solo_first_action_len_5_5 = len(ACTIONS_VERSION5_OPEN)

solo_second_action_5_5 = get_actions_version5_second
solo_second_action_len_5_5 = len(ACTIONS_VERSION5_SECOND)

solo_third_action_5_5 = get_actions_version5_third
solo_third_action_len_5_5 = len(ACTIONS_VERSION5_THIRD)


duo_first_action_5_5 = solo_first_action_5_5
duo_first_action_len_5_5 = solo_first_action_len_5_5

duo_second_action_5_5 = solo_second_action_5_5
duo_second_action_len_5_5 = solo_second_action_len_5_5

duo_third_action_5_5 = solo_third_action_5_5
duo_third_action_len_5_5 = solo_third_action_len_5_5


def get_solo_first_card_5_5(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_first_fun_5_5(id, ma)

    # current vector of q table for this state
    if state1 in solo_first_5_5:
        vector = solo_first_5_5[state1]
    else:
        vector = [0 for i in range(solo_first_action_len_5_5)]
        solo_first_5_5[state1] = vector

    # get card
    rez = solo_first_action_5_5(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_second_card_5_5(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_second_fun_5_5(id, ma)

    # current vector of q table for this state
    if state1 in solo_second_5_5:
        vector = solo_second_5_5[state1]
    else:
        vector = [0 for i in range(solo_second_action_len_5_5)]
        solo_second_5_5[state1] = vector

    # get card
    rez = solo_second_action_5_5(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_third_card_5_5(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_third_fun_5_5(id, ma)

    # current vector of q table for this state
    if state1 in solo_third_5_5:
        vector = solo_third_5_5[state1]
    else:
        vector = [0 for i in range(solo_third_action_len_5_5)]
        solo_third_5_5[state1] = vector

    # get card
    rez = solo_third_action_5_5(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_first_card_5_5(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_first_fun_5_5(id, ma)

    # current vector of q table for this state
    if state1 in duo_first_5_5:
        vector = duo_first_5_5[state1]
    else:
        vector = [0 for i in range(duo_first_action_len_5_5)]
        duo_first_5_5[state1] = vector

    # get card
    rez = duo_first_action_5_5(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_second_card_5_5(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_second_fun_5_5(id, ma)

    # current vector of q table for this state
    if state1 in duo_second_5_5:
        vector = duo_second_5_5[state1]
    else:
        vector = [0 for i in range(duo_second_action_len_5_5)]
        duo_second_5_5[state1] = vector

    # get card
    rez = duo_second_action_5_5(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_third_card_5_5(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_third_fun_5_5(id, ma)

    # current vector of q table for this state
    if state1 in duo_third_5_5:
        vector = duo_third_5_5[state1]
    else:
        vector = [0 for i in range(duo_third_action_len_5_5)]
        duo_third_5_5[state1] = vector

    # get card
    rez = duo_third_action_5_5(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card