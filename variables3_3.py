import pickle
from get_states_GST_functions import *
from action_functions import *
from MilestoneAgents import *

class ModelConfigError3_3(Exception):
    pass

#############################################################################################
########################################3_3##################################################
#############################################################################################
#Q tables
filename1 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\3_3\\rwf3\\qf2\\solo_first_3_3_3rd.pickle"
filename2 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\3_3\\rwf3\\qf2\\solo_second_3_3_3rd.pickle"
filename3 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\3_3\\rwf3\\qf2\\solo_third_3_3_3rd.pickle"
filename4 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\3_3\\rwf3\\qf2\\duo_first_3_3_3rd.pickle"
filename5 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\3_3\\rwf3\\qf2\\duo_second_3_3_3rd.pickle"
filename6 = "C:\\Users\\User\\Desktop\\Magistrska\\TarockMasters\\QTABLES\\3_3\\rwf3\\qf2\\duo_third_3_3_3rd.pickle"
solo_first_3_3 = pickle.load(open(filename1, "rb"))
solo_second_3_3 = pickle.load(open(filename2, "rb"))
solo_third_3_3 = pickle.load(open(filename3, "rb"))
duo_first_3_3 = pickle.load(open(filename4, "rb"))
duo_second_3_3 = pickle.load(open(filename5, "rb"))
duo_third_3_3 = pickle.load(open(filename6, "rb"))

#get states functions
solo_first_fun_3_3 = get_state_version3_solo_open
solo_second_fun_3_3 = get_state_version3_solo_second
solo_third_fun_3_3 = get_state_version3_solo_third
duo_first_fun_3_3 = get_state_version3_duo_open
duo_second_fun_3_3 = get_state_version3_duo_second
duo_third_fun_3_3 = get_state_version3_duo_third


#action functions
solo_first_action_3_3 = get_actions_version3_open
solo_first_action_len_3_3 = len(ACTIONS_VERSION3_OPEN)
solo_second_action_3_3 = get_actions_version3_play
solo_second_action_len_3_3 = len(ACTIONS_VERSION3_PLAY)
solo_third_action_3_3 = solo_second_action_3_3
solo_third_action_len_3_3 = solo_second_action_len_3_3
duo_first_action_3_3 = solo_first_action_3_3
duo_first_action_len_3_3 = solo_first_action_len_3_3
duo_second_action_3_3 = solo_second_action_3_3
duo_second_action_len_3_3 = solo_second_action_len_3_3
duo_third_action_3_3 = solo_second_action_3_3
duo_third_action_len_3_3 = solo_second_action_len_3_3

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
        raise ModelConfigError3_3

#############################################################################################
#############################################################################################
#############################################################################################

def get_solo_first_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_first_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in solo_first_3_3:
        vector = solo_first_3_3[state1]
    else:
        vector = [0 for i in range(solo_first_action_len_3_3)]
        solo_first_3_3[state1] = vector

    # get card
    rez = solo_first_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_second_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_second_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in solo_second_3_3:
        vector = solo_second_3_3[state1]
    else:
        vector = [0 for i in range(solo_second_action_len_3_3)]
        solo_second_3_3[state1] = vector

    # get card
    rez = solo_second_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_solo_third_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = solo_third_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in solo_third_3_3:
        vector = solo_third_3_3[state1]
    else:
        vector = [0 for i in range(solo_third_action_len_3_3)]
        solo_third_3_3[state1] = vector

    # get card
    rez = solo_third_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_first_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_first_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in duo_first_3_3:
        vector = duo_first_3_3[state1]
    else:
        vector = [0 for i in range(duo_first_action_len_3_3)]
        duo_first_3_3[state1] = vector

    # get card
    rez = duo_first_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_second_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_second_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in duo_second_3_3:
        vector = duo_second_3_3[state1]
    else:
        vector = [0 for i in range(duo_second_action_len_3_3)]
        duo_second_3_3[state1] = vector

    # get card
    rez = duo_second_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card

def get_duo_third_card_3_3(ma: MilestoneAgents, id, qlearning):
    # get state
    state1 = duo_third_fun_3_3(id, ma)

    # current vector of q table for this state
    if state1 in duo_third_3_3:
        vector = duo_third_3_3[state1]
    else:
        vector = [0 for i in range(duo_third_action_len_3_3)]
        duo_third_3_3[state1] = vector

    # get card
    rez = duo_third_action_3_3(vector, ma.player_hands[id], ma)
    card, action_index1, num_possible_actions1 = qlearning.choose_action_testing(rez)
    return card