from GameStateTarock import GameStateTarock

GET_STATE_VERSION1_PLAY = [("vrednost igranih kart", [1, 2, 3]),  #1 = runing sum 1, 2 = running sum <= 3, 3 = running sum > 3
                           ("skrt igrane karte", [0,1]),
                           ("lahko poberes igrane karte", [0,1]),
                           ("player2 skrt igrane karte", [0,1]),
                           ("player3 skrt igrane karte", [0,1]),
                           ("imam se tarokov", [0,1]),
                           ("player2 nima vec tarokov", [0,1]),
                           ("player3 nima vec tarokov", [0,1])]

GET_STATE_VERSION1_OPEN = [("imas kralja", [0, 1]),
                           ("imas damo", [0,1]),
                           ("imas pob/caval", [0,1]),
                           ("imas platlca", [0,1]),
                           ("imam se tarokov", [0,1]),
                           ("player2 nima vec tarokov", [0,1]),
                           ("player3 nima vec tarokov", [0,1])]

GET_STATE_VERSION2 = [("herc kralj", [0,1,2]),
			  ("herc dama", [0,1,2]),
			  ("kara kralj", [0,1,2]),
			  ("kara dama", [0,1,2]),
			  ("pik kralj", [0,1,2]),
			  ("pik dama", [0,1,2]),
			  ("kriz kralj", [0,1,2]),
			  ("kriz dama", [0,1,2]),
			  ("mond", [0,1,2]),
			  ("skis", [0,1,2]),
			  ("pagat", [0,1,2]),
			  ("vrednost stacka", [0,1,2]),
			  ("player2 brez tarokov", [0, 1]),
			  ("player3 brez tarokov", [0, 1])]

GET_STATE_VERSION3_SOLO_OPEN = [
		["herc kralj", [0,1,2]],
		["herc dama", [0, 1]],
		["karo kralj", [0,1,2]],
		["karo dama", [0, 1]],
		["pik kralj", [0,1,2]],
		["pik dama", [0, 1]],
		["kriz kralj", [0,1,2]],
		["kriz dama", [0, 1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["player2 skrt herc", [0,1]],
		["player2 skrt karo", [0,1]],
		["player2 skrt pik", [0,1]],
		["player2 skrt kriz", [0,1]],
		["player2 skrt taroki", [0,1]],
		["player3 skrt herc", [0,1]],
		["player3 skrt karo", [0,1]],
		["player3 skrt pik", [0,1]],
		["player3 skrt kriz", [0,1]],
		["player3 skrt taroki", [0,1]],]

GET_STATE_VERSION3_SOLO_SECOND =[
		["vrednost prve karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["zadnji player skrt barve", [0,1]],
		["zadnji player skrt tarokov", [0,1]]
	]

GET_STATE_VERSION3_SOLO_THIRD = [
		["vrednost prve karte", [0,2,3,4,5]],
		["vrednost druge karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]]]

GET_STATE_VERSION3_DUO_OPEN = [
		["herc kralj", [0,1,2]],
		["herc dama", [0, 1]],
		["karo kralj", [0,1,2]],
		["karo dama", [0, 1]],
		["pik kralj", [0,1,2]],
		["pik dama", [0, 1]],
		["kriz kralj", [0,1,2]],
		["kriz dama", [0, 1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["player2 skrt herc", [0,1]],
		["player2 skrt karo", [0,1]],
		["player2 skrt pik", [0,1]],
		["player2 skrt kriz", [0,1]],
		["player2 taroki", [0,1]],
		["player3 skrt herc", [0,1]],
		["player3 skrt karo", [0,1]],
		["player3 skrt pik", [0,1]],
		["player3 skrt kriz", [0,1]],
		["player3 taroki", [0,1]],
		["a je moj kolega zadnji", [0, 1]]]

GET_STATE_VERSION3_DUO_SECOND = [
		["vrednost prve karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["zadnji player skrt barve", [0,1]],
		["zadnji player ima se taroke", [0,1]],
        ["a je za mano se kolega", [0, 1]]]

GET_STATE_VERSION3_DUO_THIRD = [
		["vrednost prve karte", [0,2,3,4,5]],
		["vrednost druge karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["kolega ze pobere", [0, 1]]]

GET_STATE_VERSION5_SOLO_OPEN = [
    ["Kral herc", [0, 1, 2]],
    ["Dama herc", [0, 1, 2]],
    ["Kaval herc", [0, 1, 2]],
    ["Pob herc", [0, 1, 2]],
    ["Platlci herc", [0, 1]],
    ["Stevilo hercev v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["Kral karo", [0, 1, 2]],
    ["Dama karo", [0, 1, 2]],
    ["Kaval karo", [0, 1, 2]],
    ["Pob karo", [0, 1, 2]],
    ["Platlci karo", [0, 1]],
    ["Stevilo kar v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["Kral pik", [0, 1, 2]],
    ["Dama pik", [0, 1, 2]],
    ["Kaval pik", [0, 1, 2]],
    ["Pob pik", [0, 1, 2]],
    ["Platlci pik", [0, 1]],
    ["Stevilo pikov v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["Kral kriz", [0, 1, 2]],
    ["Dama kriz", [0, 1, 2]],
    ["Kaval kriz", [0, 1, 2]],
    ["Pob kriz", [0, 1, 2]],
    ["Platlci kriz", [0, 1]],
    ["Stevilo krizev v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["škis", [0, 1, 2]],
    ["mond", [0, 1, 2]],
    ["pagat", [0, 1, 2]],
    ["II - VII", [0, 1, 2]],
    ["VIII - XV", [0, 1, 2]],
    ["XVI - XX", [0, 1, 2]]]

GET_STATE_VERSION5_SOLO_SECOND = [
    ["Jz skrt barve", [0, 1]],
    ["Lahko poberem", [0, 1]],
    ["Kralj barve stacka", [0, 1, 2]],
    ["Dama barve stacka", [0, 1, 2]],
    ["Kaval barve stacka", [0, 1, 2]],
    ["Pob barve stacka", [0, 1, 2]],
    ["Max platlc barve stacka", [0, 1, 2]],
    ["top mid platlc barve stacka", [0, 1, 2]],
    ["bot mid barve stacka", [0, 1, 2]],
    ["Min platlc barve stacka", [0, 1, 2]],
    ["koliko tarokov se v igri", list(range(23))],
    ["zadnji player skrt barve", [0, 1]],
    ["vrednost prve karte", [0, 2, 3, 4, 5]],
]

GET_STATE_VERSION5_SOLO_THIRD = [
    ["vrednost prve karte", [0, 2, 3, 4, 5]],
    ["vrednost druge karte", [0, 2, 3, 4, 5]],
    ["Jz skrt barve", [0, 1]],
    ["Lahko poberem", [0, 1]],
    ["Kralj barve stacka", [0, 1, 2]],
    ["Dama barve stacka", [0, 1, 2]],
    ["Kaval barve stacka", [0, 1, 2]],
    ["Pob barve stacka", [0, 1, 2]],
    ["Max platlc barve stacka", [0, 1, 2]],
    ["top mid platlc barve stacka", [0, 1, 2]],
    ["bot mid barve stacka", [0, 1, 2]],
    ["Min platlc barve stacka", [0, 1, 2]],
    ["koliko tarokov se v igri", list(range(23))],

]


GET_STATE_VERSION5_DUO_OPEN = [
    ["Kral herc", [0, 1, 2]],
    ["Dama herc", [0, 1, 2]],
    ["Kaval herc", [0, 1, 2]],
    ["Pob herc", [0, 1, 2]],
    ["Platlci herc", [0, 1]],
    ["Stevilo hercev v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["Kral karo", [0, 1, 2]],
    ["Dama karo", [0, 1, 2]],
    ["Kaval karo", [0, 1, 2]],
    ["Pob karo", [0, 1, 2]],
    ["Platlci karo", [0, 1]],
    ["Stevilo kar v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["Kral pik", [0, 1, 2]],
    ["Dama pik", [0, 1, 2]],
    ["Kaval pik", [0, 1, 2]],
    ["Pob pik", [0, 1, 2]],
    ["Platlci pik", [0, 1]],
    ["Stevilo pikov v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["Kral kriz", [0, 1, 2]],
    ["Dama kriz", [0, 1, 2]],
    ["Kaval kriz", [0, 1, 2]],
    ["Pob kriz", [0, 1, 2]],
    ["Platlci kriz", [0, 1]],
    ["Stevilo krizev v igri", [0, 1, 2, 3, 4, 5, 6, 7, 8]],
    ["2. player skrt", [0, 1]],
    ["3. player skrt", [0, 1]],
    ["škis", [0, 1, 2]],
    ["mond", [0, 1, 2]],
    ["pagat", [0, 1, 2]],
    ["II - VII", [0, 1, 2]],
    ["VIII - XV", [0, 1, 2]],
    ["XVI - XX", [0, 1, 2]],
    ["Nas teammate je za nami", [0,1]]]

GET_STATE_VERSION5_DUO_SECOND = [
    ["Jz skrt barve", [0, 1]],
    ["Lahko poberem", [0, 1]],
    ["Kralj barve stacka", [0, 1, 2]],
    ["Dama barve stacka", [0, 1, 2]],
    ["Kaval barve stacka", [0, 1, 2]],
    ["Pob barve stacka", [0, 1, 2]],
    ["Max platlc barve stacka", [0, 1, 2]],
    ["top mid platlc barve stacka", [0, 1, 2]],
    ["bot mid barve stacka", [0, 1, 2]],
    ["Min platlc barve stacka", [0, 1, 2]],
    ["koliko tarokov se v igri", list(range(23))],
    ["zadnji player skrt barve", [0, 1]],
    ["vrednost prve karte", [0, 2, 3, 4, 5]],
    ["Teammate je naslednji", [0, 1]]
]


GET_STATE_VERSION5_DUO_THIRD = [
    ["vrednost prve karte", [0, 2, 3, 4, 5]],
    ["vrednost druge karte", [0, 2, 3, 4, 5]],
    ["Jz skrt barve", [0, 1]],
    ["Lahko poberem", [0, 1]],
    ["Kralj barve stacka", [0, 1, 2]],
    ["Dama barve stacka", [0, 1, 2]],
    ["Kaval barve stacka", [0, 1, 2]],
    ["Pob barve stacka", [0, 1, 2]],
    ["Max platlc barve stacka", [0, 1, 2]],
    ["top mid platlc barve stacka", [0, 1, 2]],
    ["bot mid barve stacka", [0, 1, 2]],
    ["Min platlc barve stacka", [0, 1, 2]],
    ["koliko tarokov se v igri", list(range(23))],
    ["a teammate ze pobere", [0, 1]]

]
def get_state_version1_play(current_player_id, game_state: GameStateTarock):
    """
    state_labels1 = [("vrednost igranih kart", [1,2,3]), #1 = runing sum 1, 2 = running sum <= 3, 3 = running sum > 3
					("skrt igrane karte", [0,1]),
					("lahko poberes igrane karte", [0,1]),
					("player2 skrt igrane karte", [0,1]),
					("player3 skrt igrane karte", [0,1]),
					("imam se tarokov", [0,1]),
					("player2 nima vec tarokov", [0,1]),
					("player3 nima vec tarokov", [0,1])]
    """

    state = []

    #vrednost igranih kart
    if game_state.stack_value <= 1:
        state.append(1)
    elif (game_state.stack_value <= 3) and (game_state.stack_value > 1):
        state.append(2)
    else:
        state.append(3)


    #skrt igrane karte
    #game_state.player1_skrt se updejta na enak nacin kt za playerje, sepravi za 1 move kasneje zves da je skrt ko je ze enkrat odigral skrto rundo
    #ampak za nas lahko to ze vemo prej tko da treba je
    skrt = True
    for card in game_state.player_hands[current_player_id]:
        if game_state.is_same_color(card, game_state.stack[0]):
            skrt = False

    if skrt:
        state.append(1)
    else:
        state.append(0)

    #lahko poberes igrane karte
    can = game_state.can_pickup_stack(game_state.stack, game_state.player_hands[current_player_id])
    if len(can) > 0:
        state.append(1)
    else:
        state.append(0)


    #player2 skrt igrane karte
    #player3 skrt igrane karte
    if current_player_id == game_state.players[0]:
        if game_state.player2_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    else:
        if game_state.player1_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player2_skrt[game_state.stack_color]:
            state.append(1)
        else:
            state.append(0)

    #imam se tarokov
    se_tarokov = False
    for card in game_state.player_hands[current_player_id]:
        if game_state.is_same_color(card, 61):
            se_tarokov = True
    if se_tarokov:
        state.append(1)
    else:
        state.append(0)

    # player2 skrt tarokov
    # player3 skrt tarokov
    if current_player_id == game_state.players[0]:
        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    else:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    return tuple(state)

def get_state_version1_open(current_player_id, game_state: GameStateTarock):
    """
    state_labels2 = [("imas kralja", [0,1]),
				("imas damo", [0,1]),
				("imas pob/caval", [0,1]),
				("imas platlca", [0,1]),
				("imam se tarokov", [0,1]),
				("player2 nima vec tarokov", [0,1]),
				("player3 nima vec tarokov", [0,1])]

    """

    state = []

    #imas kralja
    if current_player_id == game_state.players[0]:

        if (8 in game_state.player1_cards) or (18 in game_state.player1_cards) or (28 in game_state.player1_cards) or (38 in game_state.player1_cards):
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if (8 in game_state.player2_cards) or (18 in game_state.player2_cards) or (28 in game_state.player2_cards) or (38 in game_state.player2_cards):
            state.append(1)
        else:
            state.append(0)
    else:
        if (8 in game_state.player3_cards) or (18 in game_state.player3_cards) or (28 in game_state.player3_cards) or (38 in game_state.player3_cards):
            state.append(1)
        else:
            state.append(0)
    #print("imas kralja", state)

    # imas damo
    if current_player_id == game_state.players[0]:

        if (7 in game_state.player1_cards) or (17 in game_state.player1_cards) or (27 in game_state.player1_cards) or (37 in game_state.player1_cards):
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if (7 in game_state.player2_cards) or (17 in game_state.player2_cards) or (27 in game_state.player2_cards) or (37 in game_state.player2_cards):
            state.append(1)
        else:
            state.append(0)
    else:
        if (7 in game_state.player3_cards) or (17 in game_state.player3_cards) or (27 in game_state.player3_cards) or (37 in game_state.player3_cards):
            state.append(1)
        else:
            state.append(0)
    #print("imas damo", state)

    #imas pob/caval
    if current_player_id == game_state.players[0]:

        if (6 in game_state.player1_cards) or (16 in game_state.player1_cards) or (26 in game_state.player1_cards) or (36 in game_state.player1_cards) or (5 in game_state.player1_cards) or (15 in game_state.player1_cards) or (25 in game_state.player1_cards) or (35 in game_state.player1_cards):
            state.append(1)
        else:
            state.append(0)
    elif current_player_id == game_state.players[1]:
        if (6 in game_state.player2_cards) or (16 in game_state.player2_cards) or (26 in game_state.player2_cards) or (36 in game_state.player2_cards) or (5 in game_state.player2_cards) or (15 in game_state.player2_cards) or (25 in game_state.player2_cards) or (35 in game_state.player2_cards):
            state.append(1)
        else:
            state.append(0)
    else:
        if (6 in game_state.player2_cards) or (16 in game_state.player3_cards) or (26 in game_state.player3_cards) or (36 in game_state.player3_cards) or (5 in game_state.player3_cards) or (15 in game_state.player3_cards) or (25 in game_state.player3_cards) or (35 in game_state.player3_cards):
            state.append(1)
        else:
            state.append(0)
    #print("imas pob/caval", state)

    #imas platlca
    if current_player_id == game_state.players[0]:

        sem = False
        for card in game_state.player1_cards:
            if card in game_state.platelci:
                sem = True
        if not sem:
            state.append(0)
        else:
            state.append(1)

    elif current_player_id == game_state.players[1]:
        sem = False
        for card in game_state.player2_cards:
            if card in game_state.platelci:
                sem = True
        if not sem:
            state.append(0)
        else:
            state.append(1)

    else:
        sem = False
        for card in game_state.player3_cards:
            if card in game_state.platelci:
                sem = True
        if not sem:
            state.append(0)
        else:
            state.append(1)

    # imas se tarokov
    se_tarokov = False
    for card in game_state.player_hands[current_player_id]:
        if game_state.is_same_color(card, 61):
            se_tarokov = True
    if se_tarokov:
        state.append(1)
    else:
        state.append(0)
    #print("imas platlc", state)
    #player2 nima vec tarokov
    #player3 nima vec tarokov
    if current_player_id == game_state.players[0]:

        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player3_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

    else:
        if game_state.player1_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)

        if game_state.player2_skrt["tarock"]:
            state.append(1)
        else:
            state.append(0)
    #print("skrt taroka player2 in player3", state)
    return tuple(state)

def get_state_version2(current_player_id, game_state: GameStateTarock):
    #this state is a bit different
    #instead of binary attributes we have 3 values for each
    #0 -> ni v igri
    #1 -> imam jz
    #2 -> je v igri nimam jz
    """
    :param current_player_id: id of the player calling for the state
    :param game_state: the gamestate struct with all the information
    :return: a vector which represents the current state of the game
    """
    """
    GET_STATE_VERSION2 = [("herc kralj", [0,1,2]),
			  ("herc dama", [0,1,2]),
			  ("kara kralj", [0,1,2]),
			  ("kara dama", [0,1,2]),
			  ("pik kralj", [0,1,2]),
			  ("pik dama", [0,1,2]),
			  ("kriz kralj", [0,1,2]),
			  ("kriz dama", [0,1,2]),
			  ("mond", [0,1,2]),
			  ("skis", [0,1,2]),
			  ("pagat", [0,1,2]),
			  ("vrednost stacka", [0,1,2]),
			  ("player2 brez tarokov", [0, 1]),
			  ("player3 brez tarokov", [0, 1])]
    """

    vector = []

    #herc kralj
    if 8 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 8 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 0:
        vector.append(2)

    #herc dama
    if 7 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 7 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 1:
        vector.append(2)

    # karo kralj
    if 18 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 18 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 2:
        vector.append(2)

    # karo dama
    if 17 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 17 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 3:
        vector.append(2)

    #pik kralj
    if 28 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 28 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 4:
        vector.append(2)

    #pik dama
    if 27 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 27 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 5:
        vector.append(2)

    #kriz kralj
    if 38 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 38 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 6:
        vector.append(2)

    #kriz dama
    if 37 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 37 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 7:
        vector.append(2)

    #mond
    if 60 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 60 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 8:
        vector.append(2)

    #skis
    if 61 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 61 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 9:
        vector.append(2)

    #pagat
    if 40 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 40 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 10:
        vector.append(2)

    # vrednost igranih kart
    if game_state.stack_value <= 1:
        vector.append(1)
    elif (game_state.stack_value <= 3) and (game_state.stack_value > 1):
        vector.append(2)
    else:
        vector.append(3)

    # player2 skrt tarokov
    # player3 skrt tarokov
    if current_player_id == game_state.players[0]:
        if game_state.player2_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

        if game_state.player3_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

    elif current_player_id == game_state.players[1]:
        if game_state.player1_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

        if game_state.player3_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

    else:
        if game_state.player1_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

        if game_state.player2_skrt["tarock"]:
            vector.append(1)
        else:
            vector.append(0)

    return tuple(vector)

def get_state_version3_solo_open(current_player_id, game_state: GameStateTarock):
    """

    :param current_player_id: the id of the current player
    :param game_state: represents the current state of the game
    :return: vector

    GET_STATE_VERSION3_SOLO_OPEN = [
		["herc kralj", [0,1,2]],
		["herc dama", [0, 1]],
		["karo kralj", [0,1,2]],
		["karo dama", [0, 1]],
		["pik kralj", [0,1,2]],
		["pik dama", [0, 1]],
		["kriz kralj", [0,1,2]],
		["kriz dama", [0, 1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["player2 skrt herc", [0,1]],
		["player2 skrt karo", [0,1]],
		["player2 skrt pik", [0,1]],
		["player2 skrt kriz", [0,1]],
		["player2 taroki", [0,1]],
		["player3 skrt herc", [0,1]],
		["player3 skrt karo", [0,1]],
		["player3 skrt pik", [0,1]],
		["player3 skrt kriz", [0,1]],
		["player3 taroki", [0,1]],]

    """
    vector = []

    # herc kralj
    if 8 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 8 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 0:
        vector.append(2)

    # herc dama
    if 7 in game_state.player_hands[current_player_id]:
        vector.append(1)
    else:
        vector.append(0)

    # karo kralj
    if 18 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 18 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 2:
        vector.append(2)

    # karo dama
    if 17 in game_state.player_hands[current_player_id]:
        vector.append(1)
    else:
        vector.append(0)

    # pik kralj
    if 28 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 28 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 4:
        vector.append(2)

    # pik dama
    if 27 in game_state.player_hands[current_player_id]:
        vector.append(1)
    else:
        vector.append(0)

    # kriz kralj
    if 38 in game_state.player_hands[current_player_id]:
        vector.append(1)
    if 38 in game_state.played_cards:
        vector.append(0)
    if len(vector) == 6:
        vector.append(2)

    # kriz dama
    if 37 in game_state.player_hands[current_player_id]:
        vector.append(1)
    else:
        vector.append(0)

    #nizki taroki
    if len({40, 41, 42, 43, 44, 45, 46, 47}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    #srednji taroki
    if len({48, 49, 50, 51, 52, 53}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    #visoki taroki
    if len({54, 55, 56, 57, 58, 59, 60, 61}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    #temporarly store the skrt information
    player2_skrt = None
    player3_skrt = None
    if game_state.player_order[1] == game_state.players[0]:
        player2_skrt = game_state.player1_skrt
    if game_state.player_order[1] == game_state.players[1]:
        player2_skrt = game_state.player2_skrt
    if game_state.player_order[1] == game_state.players[2]:
        player2_skrt = game_state.player3_skrt
    if game_state.player_order[2] == game_state.players[0]:
        player3_skrt = game_state.player1_skrt
    if game_state.player_order[2] == game_state.players[1]:
        player3_skrt = game_state.player2_skrt
    if game_state.player_order[2] == game_state.players[2]:
        player3_skrt = game_state.player3_skrt

    # player2 skrt herc
    #{"heart": False, "diamond": False, "spade": False, "club": False, "tarock": False}
    if player2_skrt["heart"]:
        vector.append(1)
    else:
        vector.append(0)

    #player2 skrt karo
    if player2_skrt["diamond"]:
        vector.append(1)
    else:
        vector.append(0)

    #player2 skrt pik
    if player2_skrt["spade"]:
        vector.append(1)
    else:
        vector.append(0)

    #player2 skrt kriz
    if player2_skrt["club"]:
        vector.append(1)
    else:
        vector.append(0)

    #player2 skrt tarok
    if player2_skrt["tarock"]:
        vector.append(1)
    else:
        vector.append(0)

    #player3 skrt herc
    if player3_skrt["heart"]:
        vector.append(1)
    else:
        vector.append(0)

    #player3 skrt karo
    if player3_skrt["diamond"]:
        vector.append(1)
    else:
        vector.append(0)

    #player3 skrt pik
    if player3_skrt["spade"]:
        vector.append(1)
    else:
        vector.append(0)

    #player3 skrt kriz
    if player3_skrt["club"]:
        vector.append(1)
    else:
        vector.append(0)

    #player3 skrt tarok
    if player3_skrt["tarock"]:
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version3_solo_second(current_player_id, game_state: GameStateTarock):
    """

    :param current_player_id: the id of the player we want to construct the state for
    :param game_state: the current state of the game
    :return: vector of attributes vlaues

    GET_STATE_VERSION3_SOLO_SECOND =[
		["vrednost prve karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]],
		["zadnji player skrt barve", [0,1]],
		["zadnji player skrt tarokov", [0,1]]
	]
    """

    vector = []

    #pomozne spremenljivke
    prva_karta = game_state.stack[0]
    jz_skrt = None
    legalne_karte = game_state.legal_moves(prva_karta, game_state.player_hands[current_player_id])

    #vrednost prve karte
    vector.append(game_state.id_to_points[prva_karta])

    #a je prva karta tarok
    if game_state.isTarock(prva_karta):
        vector.append(1)
    else:
        vector.append(0)

    #a sm skrt te barve
    skrt = True
    for card in game_state.player_hands[current_player_id]:
        if game_state.is_same_color(card, game_state.stack[0]):
            skrt = False

    if skrt:
        vector.append(1)
    else:
        vector.append(0)

    #a lahko poberem z barvo
    #print(game_state.player_hands[current_player_id])
    #print(legalne_karte)
    if max(legalne_karte) > prva_karta and game_state.is_same_color(max(legalne_karte), prva_karta) and not game_state.isTarock(max(legalne_karte)):
        vector.append(1)
    else:
        vector.append(0)

    #a lahko poberem s tarokom
    if game_state.isTarock(max(legalne_karte)) and max(legalne_karte) > prva_karta:
        vector.append(1)
    else:
        vector.append(0)

    # nizki taroki
    if len({40, 41, 42, 43, 44, 45, 46, 47}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    # srednji taroki
    if len({48, 49, 50, 51, 52, 53}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    # visoki taroki
    if len({54, 55, 56, 57, 58, 59, 60, 61}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    # mam kralja te barve
    if (8 in legalne_karte and game_state.is_same_color(8, prva_karta)) or (
            18 in legalne_karte and game_state.is_same_color(18, prva_karta)) or (
            28 in legalne_karte and game_state.is_same_color(28, prva_karta)) or (
            38 in legalne_karte and game_state.is_same_color(38, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam damo te barve
    if (7 in legalne_karte and game_state.is_same_color(7, prva_karta)) or (
            17 in legalne_karte and game_state.is_same_color(17, prva_karta)) or (
            27 in legalne_karte and game_state.is_same_color(27, prva_karta)) or (
            37 in legalne_karte and game_state.is_same_color(37, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam kavala te barve
    if (6 in legalne_karte and game_state.is_same_color(6, prva_karta)) or (
            16 in legalne_karte and game_state.is_same_color(16, prva_karta)) or (
            26 in legalne_karte and game_state.is_same_color(26, prva_karta)) or (
            36 in legalne_karte and game_state.is_same_color(36, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam poba te barve
    if (5 in legalne_karte and game_state.is_same_color(5, prva_karta)) or (
            15 in legalne_karte and game_state.is_same_color(15, prva_karta)) or (
            25 in legalne_karte and game_state.is_same_color(25, prva_karta)) or (
            35 in legalne_karte and game_state.is_same_color(35, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam platlca te barve
    if len(set(legalne_karte).intersection(set(game_state.platelci))) >= 1 and game_state.is_same_color(
            list(set(legalne_karte).intersection(set(game_state.platelci)))[0], prva_karta):
        vector.append(1)
    else:
        vector.append(0)

    #zadnji player skrt te barve
    zadni_skrt = None
    if game_state.player_order[2] == game_state.players[0]:
        zadni_skrt = game_state.player1_skrt
    if game_state.player_order[2] == game_state.players[1]:
        zadni_skrt = game_state.player2_skrt
    if game_state.player_order[2] == game_state.players[2]:
        zadni_skrt = game_state.player3_skrt

    if zadni_skrt[game_state.stack_color]:
        vector.append(1)
    else:
        vector.append(0)

    #zadni player je skrt tarokov
    if zadni_skrt["tarock"]:
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version3_solo_third(current_player_id, game_state: GameStateTarock): 
    """

    :param current_player_id:
    :param game_state:
    :return:

    ["vrednost prve karte", [0,2,3,4,5]],
		["vrednost druge karte", [0,2,3,4,5]],
		["a je prva karta tarok", [0,1]],
		["a sm skrt te barve", [0,1]],
		["a lahko poberem z barvo", [0,1]],
		["a lahko poberem s tarokom", [0,1]],
		["nizki taroki", [0,1]],
		["srednji taroki", [0,1]],
		["visoki taroki", [0,1]],
		["mam kralja te barve", [0,1]],
		["mam damo te barve", [0,1]],
		["mam cavala te barve", [0,1]],
		["mam poba te barve", [0,1]],
		["mam platlca te barve", [0,1]]]

    """
    vector = []

    # pomozne spremenljivke
    prva_karta = game_state.stack[0]
    druga_karta = game_state.stack[1]
    jz_skrt = None
    legalne_karte = game_state.legal_moves(prva_karta, game_state.player_hands[current_player_id])

    # vrednost prve karte
    vector.append(game_state.id_to_points[prva_karta])

    # vrednost druge karte
    vector.append(game_state.id_to_points[druga_karta])

    # a je prva karta tarok
    if game_state.isTarock(prva_karta):
        vector.append(1)
    else:
        vector.append(0)

    # a sm skrt te barve
    skrt = True
    for card in game_state.player_hands[current_player_id]:
        if game_state.is_same_color(card, game_state.stack[0]):
            skrt = False

    if skrt:
        vector.append(1)
    else:
        vector.append(0)

    # a lahko poberem z barvo
    if max(legalne_karte) > prva_karta and game_state.is_same_color(max(legalne_karte),
                                                                    prva_karta) and not game_state.isTarock(
            max(legalne_karte)):
        vector.append(1)
    else:
        vector.append(0)

    # a lahko poberem s tarokom
    if game_state.isTarock(max(legalne_karte)) and max(legalne_karte) > prva_karta:
        vector.append(1)
    else:
        vector.append(0)

    # nizki taroki
    if len({40, 41, 42, 43, 44, 45, 46, 47}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    # srednji taroki
    if len({48, 49, 50, 51, 52, 53}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    # visoki taroki
    if len({54, 55, 56, 57, 58, 59, 60, 61}.intersection(set(game_state.player_hands[current_player_id]))) >= 1:
        vector.append(1)
    else:
        vector.append(0)

    # mam kralja te barve
    if (8 in legalne_karte and game_state.is_same_color(8, prva_karta)) or (18 in legalne_karte and game_state.is_same_color(18, prva_karta)) or (28 in legalne_karte and game_state.is_same_color(28, prva_karta)) or (38 in legalne_karte and game_state.is_same_color(38, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam damo te barve
    if (7 in legalne_karte and game_state.is_same_color(7, prva_karta)) or (17 in legalne_karte and game_state.is_same_color(17, prva_karta)) or (27 in legalne_karte and game_state.is_same_color(27, prva_karta)) or (37 in legalne_karte and game_state.is_same_color(37, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam kavala te barve
    if (6 in legalne_karte and game_state.is_same_color(6, prva_karta)) or (
                16 in legalne_karte and game_state.is_same_color(16, prva_karta)) or (
                26 in legalne_karte and game_state.is_same_color(26, prva_karta)) or (
                36 in legalne_karte and game_state.is_same_color(36, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam poba te barve
    if (5 in legalne_karte and game_state.is_same_color(5, prva_karta)) or (15 in legalne_karte and game_state.is_same_color(15, prva_karta)) or (25 in legalne_karte and game_state.is_same_color(25, prva_karta)) or (35 in legalne_karte and game_state.is_same_color(35, prva_karta)):
        vector.append(1)
    else:
        vector.append(0)

    # mam platlca te barve
    if len(set(legalne_karte).intersection(set(game_state.platelci))) >= 1 and game_state.is_same_color(list(set(legalne_karte).intersection(set(game_state.platelci)))[0], prva_karta):
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version3_duo_open(current_player_id, game_state: GameStateTarock):

    #vse isto kot solo open
    vector = list(get_state_version3_solo_open(current_player_id, game_state))

    #razen zadnji atribut, ki ti pove a je tvoj duo partner zadnji na vrsti
    if current_player_id == game_state.duo[0]:
        partner = game_state.duo[1]
    else:
        partner = game_state.duo[0]

    if game_state.player_order[2] == partner:
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version3_duo_second(current_player_id, game_state: GameStateTarock):
    vector = list(get_state_version3_solo_second(current_player_id, game_state))

    # razen zadnji atribut, ki ti pove a je tvoj duo partner naslednji ergo zadnji
    if current_player_id == game_state.duo[0]:
        partner = game_state.duo[1]
    else:
        partner = game_state.duo[0]

    if game_state.player_order[2] == partner:
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version3_duo_third(current_player_id, game_state: GameStateTarock):
    vector = list(get_state_version3_solo_third(current_player_id, game_state))

    #pogledam kdo je kolega
    if current_player_id == game_state.duo[0]:
        partner = game_state.duo[1]
    else:
        partner = game_state.duo[0]

    #pogledam a partner ze pobere
    if game_state.player_order[0] == partner:
        if game_state.winning_card_pair(game_state.stack[0], game_state.stack[1]):
            vector.append(0)
        else:
            vector.append(1)
    else:
        if game_state.winning_card_pair(game_state.stack[0], game_state.stack[1]):
            vector.append(1)
        else:
            vector.append(0)

    return tuple(vector)

def get_state_version4(id, gst: GameStateTarock):

    """
    probimo kok daleč lahko pridemo samo z n x n tabelco
    mogoče me ne sjebe memory error

    state je basically 0 1 2 za vsako karto v igri
    0 - ni je vec v igri
    1 - nimam je jz ampak je se v igri
    2 - jz jo mam
    :param id:
    :param gst:
    :return:
    """
    vector = []
    for card in gst.id_to_cards:
        if card in gst.played_cards:
            vector.append(0)
        else:
            if card not in gst.player_hands[id]:
                vector.append(1)
            else:
                vector.append(2)

    return tuple(vector)


def get_state_version5_solo_open(id, gst: GameStateTarock):
    """GET_STATE_VERSION5_SOLO_OPEN = [
        [["Kral herc"], [0, 1, 2]],
        [["Dama herc"], [0, 1, 2]],
        [["Kaval herc"], [0, 1, 2]],
        [["Pob herc"], [0, 1, 2]],
        [["Platlci herc"], [0, 1]],
        [["Stevilo hercev v igri"], [0, 1, 2, 3, 4, 5, 6, 7, 8]],
        [["2. player skrt"], [0, 1]],
        [["3. player skrt"], [0, 1]],
        [["Kral karo"], [0, 1, 2]],
        [["Dama karo"], [0, 1, 2]],
        [["Kaval karo"], [0, 1, 2]],
        [["Pob karo"], [0, 1, 2]],
        [["Platlci karo"], [0, 1]],
        [["Stevilo kar v igri"], [0, 1, 2, 3, 4, 5, 6, 7, 8]],
        [["2. player skrt"], [0, 1]],
        [["3. player skrt"], [0, 1]],
        [["Kral pik"], [0, 1, 2]],
        [["Dama pik"], [0, 1, 2]],
        [["Kaval pik"], [0, 1, 2]],
        [["Pob pik"], [0, 1, 2]],
        [["Platlci pik"], [0, 1]],
        [["Stevilo pikov v igri"], [0, 1, 2, 3, 4, 5, 6, 7, 8]],
        [["2. player skrt"], [0, 1]],
        [["3. player skrt"], [0, 1]],
        [["Kral kriz"], [0, 1, 2]],
        [["Dama kriz"], [0, 1, 2]],
        [["Kaval kriz"], [0, 1, 2]],
        [["Pob kriz"], [0, 1, 2]],
        [["Platlci kriz"], [0, 1]],
        [["Stevilo krizev v igri"], [0, 1, 2, 3, 4, 5, 6, 7, 8]],
        [["2. player skrt"], [0, 1]],
        [["3. player skrt"], [0, 1]],
        [["škis"], [0, 1, 2]],
        [["mond"], [0, 1, 2]],
        [["pagat"], [0, 1, 2]],
        [["II - VII"], [0, 1, 2]],
        [["VIII - XV"], [0, 1, 2]],
        [["XVI - XX"], [0, 1, 2]]]

        0 - ni v igri, 1 - je  v igri nimam jz, 2 mam jz
        0 - ni v igri, 1 - je v igri

    """

    vector = []

    #herci
    for x in [8, 7, 6, 5]:
        if x in gst.player_hands[id]:
            vector.append(2)
        else:
            if x in gst.played_cards:
                vector.append(0)
            else:
                vector.append(1)


    platlci = False
    for x in [4, 3, 2, 1]:
        if x not in gst.played_cards:
            platlci = True

    if platlci:
        vector.append(1)
    else:
        vector.append(0)


    #stevilo hercev v igri
    number = 8
    for x in gst.played_cards:
        if gst.isHeart(x):
            number -= 1
    vector.append(number)

    if gst.players_skrti[gst.player_order[1]]["heart"]:
        vector.append(1)
    else:
        vector.append(0)
    if gst.players_skrti[gst.player_order[2]]["heart"]:
        vector.append(1)
    else:
        vector.append(0)

    # kare
    for x in [18, 17, 16, 15]:
        if x in gst.player_hands[id]:
            vector.append(2)
        else:
            if x in gst.played_cards:
                vector.append(0)
            else:
                vector.append(1)

    platlci = False
    for x in [14, 13, 12, 11]:
        if x not in gst.played_cards:
            platlci = True

    if platlci:
        vector.append(1)
    else:
        vector.append(0)

    # stevilo kar v igri
    number = 8
    for x in gst.played_cards:
        if gst.isDiamond(x):
            number -= 1
    vector.append(number)

    if gst.players_skrti[gst.player_order[1]]["diamond"]:
        vector.append(1)
    else:
        vector.append(0)

    if gst.players_skrti[gst.player_order[2]]["diamond"]:
        vector.append(1)
    else:
        vector.append(0)

    # piki
    for x in [28, 27, 26, 25]:
        if x in gst.player_hands[id]:
            vector.append(2)
        else:
            if x in gst.played_cards:
                vector.append(0)
            else:
                vector.append(1)

    platlci = False
    for x in [24, 23, 22, 21]:
        if x not in gst.played_cards:
            platlci = True

    if platlci:
        vector.append(1)
    else:
        vector.append(0)

    # stevilo pikov v igri
    number = 8
    for x in gst.played_cards:
        if gst.isSpade(x):
            number -= 1
    vector.append(number)

    if gst.players_skrti[gst.player_order[1]]["spade"]:
        vector.append(1)
    else:
        vector.append(0)

    if gst.players_skrti[gst.player_order[2]]["spade"]:
        vector.append(1)
    else:
        vector.append(0)

    # krizi
    for x in [38, 37, 36, 35]:
        if x in gst.player_hands[id]:
            vector.append(2)
        else:
            if x in gst.played_cards:
                vector.append(0)
            else:
                vector.append(1)

    platlci = False
    for x in [34, 33, 32, 31]:
        if x not in gst.played_cards:
            platlci = True

    if platlci:
        vector.append(1)
    else:
        vector.append(0)

    number = 8
    for x in gst.played_cards:
        if gst.isClub(x):
            number -= 1
    vector.append(number)

    if gst.players_skrti[gst.player_order[1]]["club"]:
        vector.append(1)
    else:
        vector.append(0)

    if gst.players_skrti[gst.player_order[2]]["club"]:
        vector.append(1)
    else:
        vector.append(0)


    if 61 in gst.played_cards:
        vector.append(0)
    else:
        if 61 in gst.player_hands[id]:
            vector.append(2)
        else:
            vector.append(1)

    if 60 in gst.played_cards:
        vector.append(0)
    else:
        if 60 in gst.player_hands[id]:
            vector.append(2)
        else:
            vector.append(1)

    if 40 in gst.played_cards:
        vector.append(0)
    else:
        if 40 in gst.player_hands[id]:
            vector.append(2)
        else:
            vector.append(1)

    nizki_taroki = [41, 42, 43, 44, 45, 46]
    srednji_taroki = [47,48,49, 50, 51, 52, 53, 54]
    visoki_taroki = [55, 56, 57, 58, 59]

    nizki_uzuni = 0
    nizki_not = 0
    nizki_mi = 0
    for x in nizki_taroki:
        if x in gst.played_cards:
            nizki_uzuni += 1
        if x in gst.player_hands[id]:
            nizki_mi += 1
        if x not in gst.played_cards and x not in gst.player_hands[id]:
            nizki_not += 1

    nizkost = list(sorted([(0, nizki_uzuni), (1, nizki_not), (2, nizki_mi)], key=lambda x: x[1]))[-1]

    vector.append(nizkost[0])

    srednji_uzuni = 0
    srednji_not = 0
    srednji_mi = 0
    for x in srednji_taroki:
        if x in gst.played_cards:
            srednji_uzuni += 1
        if x in gst.player_hands[id]:
            srednji_mi += 1
        if x not in gst.played_cards and x not in gst.player_hands[id]:
            srednji_not += 1

    nizkost = list(sorted([(0, srednji_uzuni), (1, srednji_not), (2, srednji_mi)], key=lambda x: x[1]))[-1]

    vector.append(nizkost[0])

    visoki_uzuni = 0
    visoki_not = 0
    visoki_mi = 0
    for x in visoki_taroki:
        if x in gst.played_cards:
            visoki_uzuni += 1
        if x in gst.player_hands[id]:
            visoki_mi += 1
        if x not in gst.played_cards and x not in gst.player_hands[id]:
            visoki_not += 1

    nizkost = list(sorted([(0, visoki_uzuni), (1, visoki_not), (2, visoki_mi)], key=lambda x: x[1]))[-1]

    vector.append(nizkost[0])

    return tuple(vector)

def get_state_version5_solo_second(id, gst: GameStateTarock):
    """GET_STATE_VERSION5_SOLO_SECOND = [
        [["Jz skrt barve"], [0, 1]],
        [["Lahko poberem"], [0, 1]],
        [["Kralj barve stacka"], [0, 1, 2]],
        [["Dama barve stacka"], [0, 1, 2]],
        [["Kaval barve stacka"], [0, 1, 2]],
        [["Pob barve stacka"], [0, 1, 2]],
        [["Max platlc barve stacka"], [0, 1, 2]],
        [["top mid platlc barve stacka"], [0, 1, 2]],
        [["bot mid barve stacka"], [0, 1, 2]],
        [["Min platlc barve stacka"], [0, 1, 2]],
        [["koliko tarokov se v igri"], list(range(23))],
        [["zadnji player skrt barve"], [0, 1]]
    ]"""

    vector = []

    if gst.isHeart(gst.stack[0]):
        barve = [1,2,3,4,5,6,7,8]
        barva = "heart"
    if gst.isDiamond(gst.stack[0]):
        barve = [11,12,13,14,15,16,17,18]
        barva = "diamond"
    if gst.isSpade(gst.stack[0]):
        barve = [21, 22, 23, 24, 25, 26, 27, 28]
        barva = "spade"
    if gst.isClub(gst.stack[0]):
        barve = [31, 32, 33, 34, 35, 36, 37, 38]
        barva = "club"

    if gst.isTarock(gst.stack[0]):
        barve = list(range(40, 62))
        barva = "tarock"

    #jz skrt barve
    skrt = True
    for x in barve:
        if x in gst.player_hands[id]:
            skrt = False

    if skrt:
        vector.append(1)
    else:
        vector.append(0)

    #lahko poberem
    if not gst.can_pickup_stack(gst.stack, gst.player_hands[id]):
        vector.append(0)
    else:
        vector.append(1)

    if barva != "tarock":
        #kral te barve
        if barve[-1] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-1] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        #dama te barve
        if barve[-2] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-2] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        #kaval te barve
        if barve[-3] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-3] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        #pob te barve
        if barve[-4] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-4] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        #max platlc te barve
        if barve[-5] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-5] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)


        #top mid platlc te barve
        if barve[-6] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-6] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # top mid platlc te barve
        if barve[-7] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-7] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # min platlc te barve
        if barve[-8] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-8] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)
    else:
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)

    number_of_tarocks = 22
    for x in gst.played_cards:
        if gst.isTarock(x):
            number_of_tarocks -= 1

    vector.append(number_of_tarocks)

    if gst.players_skrti[gst.player_order[2]][barva]:
        vector.append(1)
    else:
        vector.append(0)

    vector.append(gst.id_to_points[gst.stack[0]])

    return tuple(vector)

def get_state_version5_solo_third(id, gst: GameStateTarock):
    """GET_STATE_VERSION5_SOLO_THIRD = [
        [["vrednost prve karte"], [0, 2, 3, 4, 5]],
        [["vrednost druge karte"], [0, 2, 3, 4, 5]],
        [["Jz skrt barve"], [0, 1]],
        [["Lahko poberem"], [0, 1]],
        [["Kralj barve stacka"], [0, 1, 2]],
        [["Dama barve stacka"], [0, 1, 2]],
        [["Kaval barve stacka"], [0, 1, 2]],
        [["Pob barve stacka"], [0, 1, 2]],
        [["Max platlc barve stacka"], [0, 1, 2]],
        [["top mid platlc barve stacka"], [0, 1, 2]],
        [["bot mid barve stacka"], [0, 1, 2]],
        [["Min platlc barve stacka"], [0, 1, 2]],
        [["koliko tarokov se v igri"], list(range(23))],

    ]"""

    vector = []

    vector.append(gst.id_to_points[gst.stack[0]])
    vector.append(gst.id_to_points[gst.stack[1]])

    if gst.isHeart(gst.stack[0]):
        barve = [1, 2, 3, 4, 5, 6, 7, 8]
        barva = "heart"
    if gst.isDiamond(gst.stack[0]):
        barve = [11, 12, 13, 14, 15, 16, 17, 18]
        barva = "diamond"
    if gst.isSpade(gst.stack[0]):
        barve = [21, 22, 23, 24, 25, 26, 27, 28]
        barva = "spade"
    if gst.isClub(gst.stack[0]):
        barve = [31, 32, 33, 34, 35, 36, 37, 38]
        barva = "club"

    if gst.isTarock(gst.stack[0]):
        barve = list(range(40, 62))
        barva = "tarock"

    # jz skrt barve
    skrt = True
    for x in barve:
        if x in gst.player_hands[id]:
            skrt = False

    if skrt:
        vector.append(1)
    else:
        vector.append(0)

    # lahko poberem
    if not gst.can_pickup_stack(gst.stack, gst.player_hands[id]):
        vector.append(0)
    else:
        vector.append(1)

    if barva != "tarock":
        # kral te barve
        if barve[-1] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-1] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # dama te barve
        if barve[-2] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-2] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # kaval te barve
        if barve[-3] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-3] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # pob te barve
        if barve[-4] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-4] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # max platlc te barve
        if barve[-5] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-5] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # top mid platlc te barve
        if barve[-6] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-6] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # top mid platlc te barve
        if barve[-7] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-7] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)

        # min platlc te barve
        if barve[-8] in gst.played_cards:
            vector.append(0)
        else:
            if barve[-8] in gst.player_hands[id]:
                vector.append(2)
            else:
                vector.append(1)
    else:
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)
        vector.append(0)

    number_of_tarocks = 22
    for x in gst.played_cards:
        if gst.isTarock(x):
            number_of_tarocks -= 1

    vector.append(number_of_tarocks)

    return tuple(vector)

def get_state_version5_duo_open(id, gst: GameStateTarock):
    vector = list(get_state_version5_solo_open(id, gst))

    #dodamo se ce je teammate nasledni
    #1 je true, 0 je false
    teammate = gst.duo[1] if gst.duo[0] == id else gst.duo[0]

    if gst.player_order[1] == teammate:
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version5_duo_second(id, gst: GameStateTarock):
    vector = list(get_state_version5_solo_second(id, gst))

    # dodamo se ce je teammate nasledni
    # 1 je true, 0 je false
    teammate = gst.duo[1] if gst.duo[0] == id else gst.duo[0]

    if gst.player_order[2] == teammate:
        vector.append(1)
    else:
        vector.append(0)

    return tuple(vector)

def get_state_version5_duo_third(id, gst: GameStateTarock):
    vector = list(get_state_version5_solo_third(id, gst))

    #preverim se ce moj teammate ze pobere
    teammate = gst.duo[1] if gst.duo[0] == id else gst.duo[0]

    #preverim ce teammate ze pobere
    # returns true if c2 beats c1
    if gst.winning_card_pair(gst.stack[0], gst.stack[1]):
        if gst.player_order[1] == teammate:
            vector.append(1)
        else:
            vector.append(0)
    else:
        if gst.player_order[1] == teammate:
            vector.append(0)
        else:
            vector.append(1)

    return tuple(vector)

if __name__ == "__main__":
    print("Hello world!")