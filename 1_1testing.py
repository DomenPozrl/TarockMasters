from variables1_1 import *
import random
from QLearning import QLearning
from write_results import write_results
tb = TarockBasics()
qlearning = QLearning(0.1, 0.1, 0.1)

def play_one_game(p1, p2, p3, talon, ps, sp, duo, strats):
    
    msa = MilestoneAgents(p1, p2, p3, [1,2,3], solo, duo)
    msa.update_state_talon(talon)
    points = {1: 0, 2: 0, 3: 0}
    
    while msa.player1_cards:
        
        first = msa.starting_player
        second = msa.second_player
        third = msa.third_player


        if strats[first] == "me":
            card1 = get_solo_first_card_1_1(msa, first, qlearning)
        elif strats[first] == "LWW":
            card1 = msa.locally_worst_worst_agent(first)
        elif strats[first] == "LW":
            card1 = msa.locally_worst_agent(first)
        elif strats[first] == "random":
            card1 = msa.random_agent(first)
        elif strats[first] == "LB":
            card1 = msa.locally_best_agent(first)
        elif strats[first] == "LBB":
            card1 = msa.locally_best_best_agent(first)
        else:
            raise NotImplemented
        
        msa.update_state(card1, first)


        if strats[second] == "me":
            card2 = get_solo_second_card_1_1(msa, second, qlearning)
        elif strats[second] == "LWW":
            card2 = msa.locally_worst_worst_agent(second)
        elif strats[second] == "LW":
            card2 = msa.locally_worst_agent(second)
        elif strats[second] == "random":
            card2 = msa.random_agent(second)
        elif strats[second] == "LB":
            card2 = msa.locally_best_agent(second)
        elif strats[second] == "LBB":
            card2 = msa.locally_best_best_agent(second)
        else:
            raise NotImplemented

        msa.update_state(card2, second)


        if strats[third] == "me":
            card3 = get_solo_second_card_1_1(msa, third, qlearning)
        elif strats[third] == "LWW":
            card3 = msa.locally_worst_worst_agent(third)
        elif strats[third] == "LW":
            card3 = msa.locally_worst_agent(third)
        elif strats[third] == "random":
            card3 = msa.random_agent(third)
        elif strats[third] == "LB":
            card3 = msa.locally_best_agent(third)
        elif strats[third] == "LBB":
            card3 = msa.locally_best_best_agent(third)
        else:
            raise NotImplemented
        
        msa.update_state(card3, third)

        winner = msa.current_winning_player
        points[winner] += msa.eval_stack(msa.stack)
        
        msa.clear_state()
    
    points["talon"] = msa.eval_stack([talon[0], talon[1], talon[2]]) + msa.eval_stack([talon[3], talon[4], talon[5]])
    
    return points, msa.discard, msa.player_hands_copy
"""
PRELIMINARY RESULTS 1_1_rwf1_qf1:
10 games: {1: 15.4, 2: 25.0, 3: 21.6, 'talon': 8.0}
50 games: {1: 18.76, 2: 21.6, 3: 22.68, 'talon': 6.96}
100 games: {1: 19.6, 2: 21.82, 3: 20.94, 'talon': 7.64}
500 games: {1: 19.16, 2: 21.776, 3: 21.11, 'talon': 7.954}
1000 games: {1: 18.646, 2: 21.553, 3: 22.124, 'talon': 7.677}
5000 games: {1: 19.0454, 2: 21.91, 3: 21.2718, 'talon': 7.7728}
10000 games: {1: 18.9777, 2: 21.8399, 3: 21.3738, 'talon': 7.8086}
15000 games: {1: 19.15426666666667, 2: 21.943266666666666, 3: 21.108933333333333, 'talon': 7.793533333333333}
100000 games: {1: 19.10878, 2: 21.89541, 3: 21.22581, 'talon': 7.77}

basically the same result, lets check how low we can go

"""
if __name__ == "__main__":
    #opponent = "LB"
    num_games = 15000
    
    for opponent in ["LWW", "LW", "random", "LB", "LBB"]:
        overall_points = {1: [], 2: [], 3: [], "talon": []}
        discards = []
        duos = []
        players_hands = []    
        
        model, rwf, qf = check_and_report_filenames()
        player = model + "_" + rwf + "_" + qf
        
        
        for i in range(num_games):
            if (i / num_games) in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
                print(i)
            p1, p2, p3, talon = tb.deal_cards()
            solo = random.choice([1,2,3])
            duo = [x for x in [1,2,3] if x != solo]
            strats = {1:"me", 2: opponent, 3: opponent}
            points, discard, hands = play_one_game(p1, p2, p3, talon, [1,2,3], solo, duo, strats)
            
            
            discards.append(discard)
            duos.append(duo)
            players_hands.append(hands)

            for key in points:
                overall_points[key].append(points[key])

        avg_points = {key: sum(overall_points[key])/len(overall_points[key]) for key in overall_points}
        
        results = {"overall points": overall_points, "discards": discards, "duos": duos, "player hands": players_hands, "avg points": avg_points}
        write_results(model, rwf, qf, opponent, results)
        print(player, opponent, opponent)
        print(avg_points)

    