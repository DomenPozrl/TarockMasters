import pickle

def write_results(model, rwf, qf, opponent, results):
    file = open("Results\\" + model + "\\" + rwf + "\\" + qf + "\\"+ model + " " + opponent + " " + opponent + ".pickle", "wb")
    pickle.dump(results, file)
    file.close()