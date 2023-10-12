import gymnasium as gm

env = gm.make('ALE/MsPacman-v5', render_mode='human')
observesion, info = env.reset()

print(observesion, info)

while True:
  try:
    action = env.action_space.sample()
    observesion, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
      observesion, info = env.reset()  
  except KeyboardInterrupt:
    break
  
#45:03
env.close()
