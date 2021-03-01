# -*- coding: utf-8 -*-
"""ddpg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xBCeDWXgF0esUCjdOZhmdDcu7JM6PZhL
"""

import argparse
import collections
import os

import numpy as np
import torch

from gym_torcs import TorcsEnv
from sample_agent import \
    Agent  # Temp - Only to allow one to play game. This should be replaced by A2C eventually

# Global configuration variables
vision = False

# Generate a Torcs environment
env = TorcsEnv(vision=vision, throttle=False)
agent = Agent(1)  # steering only

def get_observations():
    episode_count = 10
    max_steps = 50
    reward = 0
    done = False
    step = 0

    print("TORCS Experiment Start.")
    for i in range(episode_count):
        print(f"Starting episode : {i}")

        if np.mod(i, 3) == 0:
            # Sometimes you need to relaunch TORCS because of the memory leak error
            ob = env.reset(relaunch=True)
        else:
            ob = env.reset()

        total_reward = 0.
        for j in range(max_steps): #There are the number of 'steps' the car will take
            action = agent.act(ob, reward, done, vision)

            ob, reward, done, _ = env.step(action)
            #print(ob)
            total_reward += reward

            step += 1
            if done:
                break

        print("TOTAL REWARD @ " + str(i) +" -th Episode  :  " + str(total_reward))
        print("Total Step: " + str(step))
        print("")

    env.end()  # This is for shutting down TORCS
    print("Finish.")

get_observations()
