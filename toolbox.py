import pickle
import random
def printsaved():
    with open('mysaved/saved_actions.pkl', 'rb') as f:
        saved_actions = pickle.load(f)
    for l in saved_actions:
        print(l)
    print(len(saved_actions))

def randomActionFeeder(amount):
    saved_actions = []
    action = []
    for a in range(amount):
        for i in range(8):
            action.append(random.choice([1, 0]))
        saved_actions.append(action)
        action = []
    return saved_actions
    #saved_actions.append(action)
    #action = random.choice([[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1]])
    #saved_actions.append(action)
