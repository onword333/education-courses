import gymnasium as gm
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import datetime as dt
import json


keys_to_action = {
  KeyCode.from_char('w'): 1, 
  KeyCode.from_char('s'): 4, 
  KeyCode.from_char('a'): 3, 
  KeyCode.from_char('d'): 2
}

# словарь состояний кнопок, будем хранить нажаты ли кнопки
keys_pressed = {}

def on_press(key):  
  keys_pressed[key] = True

def on_release(key):
  keys_pressed[key] = False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()


env = gm.make('ALE/MsPacman-ram-v5', render_mode='human')
observesion, info = env.reset()

# массив для сохранения текущего состояние игры 
# для дальнейшего обучения нашей модели
saved_data = []

while not keys_pressed.get(Key.esc):
  observesion, info = env.reset()
  observesion, reward, terminated, truncated, info = env.step(0)

  while not terminated and not truncated:
    if keys_pressed.get(Key.esc):
      break
    
    action = 0
    for key in keys_to_action:      
      if keys_pressed.get(key):
        action = keys_to_action[key]

    next_observesion, reward, terminated, truncated, info = env.step(action)

    # сохраним текущее состояние игры
    # observesion нужно брать предыдущий т.к. reward нам возвращают за пред. действие
    saved_data.append([[int(var) for var in observesion], int(action)])
    observesion = next_observesion

print('expert recoredr, сохранение')
filename = f'states/expert_{dt.datetime.now().strftime("%Y-%m-%dT%H-%S")}.txt'

with open(filename, 'w') as file:
  file.write(json.dumps(saved_data))

print('expert recoredr, сохранено')  
#45:03
env.close()