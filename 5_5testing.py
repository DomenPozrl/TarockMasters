from variables5_5 import *
import random
from QLearning import QLearning
from write_results import write_results

print("Done with importing")

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
            if first not in msa.duo:
                card1 = get_solo_first_card_5_5(msa, first, qlearning)
            else:
                card1 = get_duo_first_card_5_5(msa, first, qlearning)
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
            raise NotImplementedError
        
        msa.update_state(card1, first)

        if strats[second] == "me":
            if second not in msa.duo:
                card2 = get_solo_second_card_5_5(msa, second, qlearning)
            else:
                card2 = get_duo_second_card_5_5(msa, second, qlearning)
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
            raise NotImplementedError

        msa.update_state(card2, second)
        
        if strats[third] == "me":
            if third in msa.duo:
                card3 = get_solo_third_card_5_5(msa, third, qlearning)
            else:
                card3 = get_duo_third_card_5_5(msa, third, qlearning)
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
        
        msa.update_state(card3, third)

        winner = msa.current_winning_player
        points[winner] += msa.eval_stack(msa.stack)
        
        msa.clear_state()
    
    points["talon"] = msa.eval_stack([talon[0], talon[1], talon[2]]) + msa.eval_stack([talon[3], talon[4], talon[5]])
    
    return points, msa.discard, msa.player_hands_copy


if __name__ == "__main__":
    num_games = 15000
    
    for opponent in ["LWW", "LW", "random", "LB", "LBB"]:
        
        discards = []
        duos = []
        player_hands = []
        overall_points = {1: [], 2: [], 3: [], "talon": []}

        model, rwf, qf = check_and_report_filenames()
        player = model + "_" + rwf + "_" + qf

        print(player, opponent, opponent)

        for i in range(num_games):
            
            if (i / num_games) in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
                print(i)

            p1, p2, p3, talon = tb.deal_cards()
            solo = random.choice([1,2,3])
            duo = [x for x in [1,2,3] if x != solo]
            strats = {1: "me", 2: opponent, 3: opponent}
            points, discard, hands = play_one_game(p1, p2, p3, talon, [1,2,3], solo, duo, strats)

            for key in points:
                overall_points[key].append(points[key])
            
            discards.append(discard)
            duos.append(duo)
            player_hands.append(hands)
        
        avg_points = {key: sum(overall_points[key])/len(overall_points[key]) for key in overall_points}
        results = {"overall points": overall_points, "discards": discards, "duos": duos, "player hands": player_hands, "avg points": avg_points}
        write_results(model, rwf, qf, opponent, results)
        
        print(avg_points)

