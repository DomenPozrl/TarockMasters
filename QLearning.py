import pickle
import random

class QLearning:


    #0.1, 0.1, 0.2
    def __init__(self, gamma, alpha, eps):
        self.gamma = gamma
        self.alpha = alpha
        self.eps = eps



    def choose_action_testing(self, pairs):
        action_names = [name for _, _, _, name in pairs]
        num_of_possible_actions = sum([1 for par in pairs if par[1]])
        possible = [par for par in pairs if par[1]]

        if not possible:
            for par in pairs:

                if par[2] != None:
                    return par[2], action_names.index(par[3]), num_of_possible_actions/len(action_names)

        pairs = reversed(sorted(pairs))
        for par in pairs:
            if par[1]:
                return par[2], action_names.index(par[3]), num_of_possible_actions / len(action_names)

        for par in pairs:

            if par[2] != None:
                return par[2], action_names.index(par[3]), num_of_possible_actions / len(action_names)


    def choose_action(self, pairs):
        """

        :param pairs: the return object of the action_functions
        :return: the pair chosen card, the action index and the number of actions that were even possible

        exploration vs exploitation is implemented

        """

        action_names = [name for _, _, _, name in pairs]
        num_of_possible_actions = sum([1 for par in pairs if par[1]])
        possible = [par for par in pairs if par[1]]
        if not possible:
            for par in pairs:

                if par[2] != None:
                    return par[2], action_names.index(par[3]), num_of_possible_actions/len(action_names)

        if random.random() > self.eps:

            pairs = list(reversed(sorted(pairs, key=lambda  x: x[0])))
            for par in pairs:
                if par[1]:
                    return par[2], action_names.index(par[3]), num_of_possible_actions/len(action_names)

            for par in pairs:

                if par[2] != None:
                    return par[2], action_names.index(par[3]), num_of_possible_actions/len(action_names)
        else:

            izbira = random.choice(possible)
            return izbira[2], action_names.index(izbira[3]), num_of_possible_actions/len(action_names)



    #table in the shape of dict => {state: [*reward vector*]}
    def update_table(self, table, state, action_index, reward):
        table[state][action_index] += self.alpha * reward
        return table

    def update_table2(self, table1, table2, state1, state2, action_index1, reward, player2_is_partner):
        if player2_is_partner:
            if state2 in table2:
                table1[state1][action_index1] += self.alpha * (reward + self.gamma * max(table2[state2]) - table1[state1][action_index1])
            else:
                table1[state1][action_index1] += self.alpha * (reward + self.gamma * 0)

        else:
            if state2 in table2:
                table1[state1][action_index1] += self.alpha * (reward - self.gamma * max(table2[state2]) - table1[state1][action_index1])
            else:
                table1[state1][action_index1] += self.alpha * (reward + self.gamma * 0)
        return table1

    def pickle_table(self, table, file_name):
        file = open(file_name, "wb")
        pickle.dump(table, file)
        file.close()

    def unpickle_table(self, file_name):
        file = open(file_name, "rb")
        table = pickle.load(file)
        file.close()
        return table
