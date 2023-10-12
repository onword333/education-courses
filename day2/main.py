import gymnasium as gm
from gymnasium.utils.play import play

env = gm.make('ALE/MsPacman-v5', render_mode='rgb_array')
#play(env, zoom = 2, keys_to_action = {'w': 1, 's': 4, 'a': 3, 'd': 2})
print(env.action_space)

# observesion - наблюдения
observesion, info = env.reset()

print(len(observesion[0]))
