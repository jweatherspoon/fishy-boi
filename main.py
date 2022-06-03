import sys 
import time 
from pynput.keyboard import Listener, Key, Controller

keyboard = Controller()

def on_pressed(key):
  if key == Key.esc:
    sys.exit()
    
  try:
    number = int(key.char)
    if number >= 0 and number <= 9:
      keyboard.press(Key.space)
      time.sleep(0.1 * number)
      keyboard.release(Key.space)
  except:
   # yummy
   pass

with Listener(on_press=on_pressed) as listener:
  listener.join()