import retro
import random
import pickle
from toolbox import printsaved, randomActionFeeder, printButtons

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
    with open('winner.pkl', 'rb') as f:
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
        printButtons()
        print(saved_actions[i])
        print(i)
        print(rew)
        print(info['x'])
        i += 1
        env.render()
        if info['death'] == 0:
            print(info['death'])
            done = True
        if done:
            running = False
            obs = env.reset()
    env.close()


def runToLearn():
    learning = True
    while learning:
        done = False
        saved_random_actions = randomActionFeeder(700)
        env = retro.make(game='SuperMarioWorld-Snes')
        obs = env.reset()
        try:
            with open('mysaved/saved_actions.pkl', 'rb') as f:
                saved_actions = pickle.load(f)
        except:
            saved_actions = randomActionFeeder(300)
        i = 0
        running = True
        while not done:

            # obs, rew, done, info = env.step(env.action_space.sample())

            obs, rew, done, info = env.step(saved_actions[i])
            print(rew)
            i += 1
            env.render()

            if i == len(saved_actions)-2:
                i = 0
                while not done:
                    obs, rew, done, info = env.step(saved_random_actions[i])
                    print(saved_random_actions[i])
                    print(i)
                    print(rew)
                    print(info['x'])
                    i += 1
                    env.render()
                    if i >= len(saved_random_actions):
                        done = True
                    if info['death'] == 0:
                        print(info['death'])
                        saved_random_actions = saved_random_actions[0: i-10]
                        done = True
                    if done:
                        try:
                            saved_actions[-2] = float(saved_actions[-2])
                        except:
                            saved_actions.append(rew)
                            saved_actions.append(info['x'])

                        if info['x'] > saved_actions[-1]:
                            if rew > saved_actions[-2]:
                                saved_actions.append(saved_random_actions)
                                saved_actions.append(rew)
                                saved_actions.append(info['x'])
                                with open('mysaved/saved_actions.pkl', 'wb') as f:
                                    pickle.dump(saved_actions, f)
                        running = False
                        obs = env.reset()
        obs = env.close()


        '''if info['death'] == 0:
            print(info['death'])
            done = True
        if done:
            running = False
            obs = env.reset()'''
    #env.close()


def main():
    run_saved()


if __name__ == "__main__":
    main()