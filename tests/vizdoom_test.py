import vizdoom
import unittest
import time
import random
import os, sys
par_dir = os.pardir
for i in range(1):
    par_dir = os.path.join(os.pardir, par_dir)

curr_path = os.path.abspath(__file__)
root_path = os.path.abspath(os.path.join(curr_path, par_dir))
print("Path {} has been added to the python path".format(root_path))
sys.path.append(str(root_path))



class TestVizDoom(unittest.TestCase):

    def test_game(self):

        game = vizdoom.DoomGame()
        game.load_config(os.path.join(root_path, "scenarios/basic.cfg"))
        game.init()

        shoot = [0, 0, 1]
        left = [1, 0, 0]
        right = [0, 1, 0]
        actions = [shoot, left, right]

        episodes = 10
        for i in range(episodes):
            game.new_episode()
            while not game.is_episode_finished():
                state = game.get_state()
                img = state.screen_buffer
                print(f'type of img is {type(img)}')
                misc = state.game_variables
                print(f'Game variables {misc}')
                reward = game.make_action(random.choice(actions))
                print(f"\treward: {reward}")
                time.sleep(0.02)
            print(f"Result: {game.get_total_reward()}")
            time.sleep(2)
