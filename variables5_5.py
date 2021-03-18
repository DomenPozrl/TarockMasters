import pickle
from get_states_GST_functions import *
from action_functions import *
from MilestoneAgents import *

class ModelConfigError5_5(Exception):
    pass

#############################################################################################
########################################5_5##################################################
#############################################################################################
#Q tables
filename1 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\5_5\\rwf3\\qf2\\solo_first_5_5_3rd.pickle"
filename2 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\5_5\\rwf3\\qf2\\solo_second_5_5_3rd.pickle"
filename3 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\5_5\\rwf3\\qf2\\solo_third_5_5_3rd.pickle"
filename4 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\5_5\\rwf3\\qf2\\duo_first_5_5_3rd.pickle"
filename5 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\5_5\\rwf3\\qf2\\duo_second_5_5_3rd.pickle"
filename6 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\5_5\\rwf3\\qf2\\duo_third_5_5_3rd.pickle"
solo_first_5_5 = pickle.load(open(filename1, "rb"))
solo_second_5_5 = pickle.load(open(filename2, "rb"))
solo_third_5_5 = pickle.load(open(filename3, "rb"))
duo_first_5_5 = pickle.load(open(filename4, "rb"))
duo_second_5_5 = pickle.load(open(filename5, "rb"))
duo_third_5_5 = pickle.load(open(filename6, "rb"))

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


def check_and_report_filenames():
    global filename1
    global filename2
    global filename3
    global filename4
    global filename5
    global filename6

    #extract model, rwf and qf from each filename and add them to a set
    #if all three sets only contain 1 item then all the models are matching and we can proceed with testing
    models = set()
    rwfs = set()
    qfs = set()

    for filename in [filename1, filename2, filename3, filename4, filename5, filename6]:
        if filename != None:
            filename_split = filename.split("\\")
            models.add(filename_split[7])
            rwfs.add(filename_split[8])
            qfs.add(filename_split[9])
    
    if len(models) == 1 and len(rwfs) == 1 and len(qfs) == 1:
        return models.pop(), rwfs.pop(), qfs.pop()
    else:
        raise ModelConfigError5_5


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