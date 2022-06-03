import sys 
import time 
from pynput.keyboard import Listener, Key, Controller

ONE_QUARTER = 0.1 / 4

text = ''

keyboard = Controller()

def fish(sleep_time):
  keyboard.press(Key.space)
  time.sleep(sleep_time)
  keyboard.release(Key.space)

def convert_key(key):
  try:
    if key.char == '.' and '.' not in text:
      return key.char 
  except:
    return None

  try:
    number = int(key.char)
    return key.char 
  except:
    return None

def on_pressed(key):
  global text 
  if key == Key.esc:
    sys.exit()

  try:
    value = convert_key(key)
    if value is not None:
      text += value
    elif key == Key.up:
      sleep_time = 0.2 + 0.1 * float(text)
      print(f'fishing for {sleep_time} seconds')
      fish(sleep_time)
      text = ''
  except Exception as e:
   # yummy
  #  print(e)
    pass

with Listener(on_press=on_pressed) as listener:
  listener.join()