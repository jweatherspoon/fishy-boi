import sys 
import time 
from pynput.keyboard import Listener, Key, Controller

ONE_QUARTER = 0.1 / 4

keyboard = Controller()

def on_pressed(key):
  if key == Key.esc:
    sys.exit()

  try:
    number = int(key.char)
    if number >= 0 and number <= 9:
      sleep_time = 0.1 * number 
      if keyboard.alt_pressed:
        sleep_time += ONE_QUARTER
      elif keyboard.shift_pressed:
        sleep_time += ONE_QUARTER * 2
      elif keyboard.ctrl_pressed:
        sleep_time += ONE_QUARTER * 3

      keyboard.press(Key.space)
      time.sleep(sleep_time)
      keyboard.release(Key.space)
  except:
   # yummy
   pass

with Listener(on_press=on_pressed) as listener:
  listener.join()