import pickle
from get_states_GST_functions import *
from action_functions import *
from MilestoneAgents import *


class ModelConfigError1_1(Exception):
    pass

#############################################################################################
#######################################1_1###################################################
#############################################################################################
#Q tables
filename1 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\1_1\\rwf3\\qf2\\solo_first_1_1_3rd.pickle"
filename2 =  "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\1_1\\rwf3\\qf2\\solo_second_1_1_3rd.pickle"
filename3 = None
filename4 = None
filename5 = None
filename6 = None

solo_first_1_1 = pickle.load(open(filename1, "rb"))
solo_second_1_1 = pickle.load(open(filename2, "rb"))
solo_third_1_1 = solo_second_1_1
duo_first_1_1 = solo_first_1_1
duo_second_1_1 = solo_second_1_1
duo_third_1_1 = solo_second_1_1

#get states functions
solo_first_fun_1_1 = get_state_version1_open
solo_second_fun_1_1 = get_state_version1_play
solo_third_fun_1_1 = solo_second_fun_1_1
duo_first_fun_1_1 = solo_first_fun_1_1
duo_second_fun_1_1 = solo_second_fun_1_1
duo_third_fun_1_1 = solo_second_fun_1_1


#action functions
solo_first_action_1_1 = get_actions_version1_open
solo_first_action_len_1_1 = len(ACTIONS_VERSION1_OPEN)
solo_second_action_1_1 = get_actions_version1_play
solo_second_action_len_1_1 = len(ACTIONS_VERSION1_PLAY)
solo_third_action_1_1 = solo_second_action_1_1
solo_third_action_len_1_1 = solo_second_action_len_1_1
duo_first_action_1_1 = solo_first_action_1_1
duo_first_action_len_1_1 = solo_first_action_len_1_1
duo_second_action_1_1 = solo_second_action_1_1
duo_second_action_len_1_1 = solo_second_action_len_1_1
duo_third_action_1_1 = solo_second_action_1_1
duo_third_action_len_1_1 = solo_second_action_len_1_1

#############################################################################################
#############################################################################################
#############################################################################################
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
        raise ModelConfigError1_1

def get_solo_first_card_1_1(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_first_fun_1_1(id, ma)

    # current vector of q table for this state
    if state1 in solo_first_1_1:
        vector = solo_first_1_1[state1]
    else:
        vector = [0 for i in range(solo_first_action_len_1_1)]
        solo_first_1_1[state1] = vector

    # get card
    rez = solo_first_action_1_1(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_second_card_1_1(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_second_fun_1_1(id, ma)

    # current vector of q table for this state
    if state1 in solo_second_1_1:
        vector = solo_second_1_1[state1]
    else:
        vector = [0 for i in range(solo_second_action_len_1_1)]
        solo_second_1_1[state1] = vector

    # get card
    rez = solo_second_action_1_1(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_third_card_1_1(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_third_fun_1_1(id, ma)

    # current vector of q table for this state
    if state1 in solo_third_1_1:
        vector = solo_third_1_1[state1]
    else:
        vector = [0 for i in range(solo_third_action_len_1_1)]
        solo_third_1_1[state1] = vector

    # get card
    rez = solo_third_action_1_1(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_first_card_1_1(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_first_fun_1_1(id, ma)

    # current vector of q table for this state
    if state1 in duo_first_1_1:
        vector = duo_first_1_1[state1]
    else:
        vector = [0 for i in range(duo_first_action_len_1_1)]
        duo_first_1_1[state1] = vector

    # get card
    rez = duo_first_action_1_1(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_second_card_1_1(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_second_fun_1_1(id, ma)

    # current vector of q table for this state
    if state1 in duo_second_1_1:
        vector = duo_second_1_1[state1]
    else:
        vector = [0 for i in range(duo_second_action_len_1_1)]
        duo_second_1_1[state1] = vector

    # get card
    rez = duo_second_action_1_1(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_third_card_1_1(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_third_fun_1_1(id, ma)

    # current vector of q table for this state
    if state1 in duo_third_1_1:
        vector = duo_third_1_1[state1]
    else:
        vector = [0 for i in range(duo_third_action_len_1_1)]
        duo_third_1_1[state1] = vector

    # get card
    rez = duo_third_action_1_1(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card