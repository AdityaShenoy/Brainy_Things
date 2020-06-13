import pyautogui as pag
import time
import shutil
import os

NUM_IMAGES = 100
IMAGE_COORD = (1495, 182)
SAVE_COORD = (1560, 460)
NEXT_COORD = (1830, 180)
LOAD_TIME = 5
SAVE_URL = 'C:\\Users\\admin\\Desktop\\google_images'

if os.path.exists(SAVE_URL):
  shutil.rmtree(SAVE_URL)
os.mkdir(SAVE_URL)

time.sleep(5)

for i in range(NUM_IMAGES):

  pag.rightClick(IMAGE_COORD)
  time.sleep(1)

  pag.click(SAVE_COORD)
  time.sleep(LOAD_TIME)

  pag.typewrite(f'{i}')
  time.sleep(1)

  pag.hotkey('ctrl', 'l')
  time.sleep(1)

  pag.typewrite(SAVE_URL)
  time.sleep(1)

  pag.hotkey('alt', 's')
  time.sleep(1)

  pag.press('esc')
  time.sleep(1)

  pag.click(NEXT_COORD)
  time.sleep(1)