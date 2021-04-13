import retro
import random
import pickle
from toolbox import printsaved, randomActionFeeder
def runStraight():
    env = retro.make(game='SuperMarioWorld-Snes')
    obs = env.reset()
    saved_actions = []
    running = True
    while running:
        action = random.choice([[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1]])
        saved_actions.append(action)

        #obs, rew, done, info = env.step(env.action_space.sample())
        obs, rew, done, info = env.step(action)
        #print(info)
        #print(rew)
        env.render()
        if info['death']== 0:
            print(info['death'])
            done = True
        if done:
            with open('mysaved/saved_actions.pkl', 'wb') as f:
                pickle.dump(saved_actions, f)
            running = False
            obs = env.reset()

    env.close()

def run_saved():
    env = retro.make(game='SuperMarioWorld-Snes')
    obs = env.reset()
    with open('mysaved/saved_actions.pkl', 'rb') as f:
        saved_actions = pickle.load(f)
    i = 0
    running = True
    while running:

        # obs, rew, done, info = env.step(env.action_space.sample())

        obs, rew, done, info = env.step(saved_actions[i])
        print(rew)
        i += 1
        env.render()
        if info['death']== 0:
            print(info['death'])
            done = True
        if done:
            running = False
            obs = env.reset()
    env.close()

def runRandom():
    env = retro.make(game='SuperMarioWorld-Snes')
    obs = env.reset()
    saved_actions = randomActionFeeder(700)
    i = 0
    running = True
    while running:

        # obs, rew, done, info = env.step(env.action_space.sample())

        obs, rew, done, info = env.step(saved_actions[i])
        print(saved_actions[i])
        print(i)
        print(rew)
        i += 1
        env.render()
        if info['death'] == 0:
            print(info['death'])
            done = True
        if done:
            running = False
            obs = env.reset()
    env.close()

def main():

    print(retro.data.list_games())
    #printsaved()
    runRandom()
    #run_saved()
    #run_random()

if __name__ == "__main__":
    main()