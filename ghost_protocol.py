#!env/bin/python3
"""Similate user at computer."""

import time
import random
import pyautogui as g

g.PAUSE = 1
g.FAILSAFE = True

X_MAX = g.size()[0]
Y_MAX = g.size()[1]

window_shift = True  # Move mouse or change windows

try:
  while True:
    x = random.randint(10, X_MAX - 10)
    y = random.randint(10, Y_MAX - 10)
    seconds = random.randint(1, 5)
    window_shift = random.choice([True, False])

    if window_shift:
      # Same as g.hotkey('alt', 'tab') but random times
      g.keyDown('alt')
      for w in range(random.randint(1, 5)):
        g.press('tab')

      g.keyUp('alt')
      #g.keyUp('tab')

    g.moveTo(x, y, duration=2)
    time.sleep(seconds)

except KeyboardInterrupt:
  print('EXITING PROGRAM')

