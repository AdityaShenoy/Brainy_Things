import pyautogui as pag
import time
import shutil
import os

FOLDER_PATH = 'C:\\Users\\admin\\Desktop\\google_images'

if os.path.exists(FOLDER_PATH):
  shutil.rmtree(FOLDER_PATH)
  time.sleep(1)
os.mkdir(FOLDER_PATH)

time.sleep(5)
for i in range(50):
  pag.rightClick((1485, 250))
  time.sleep(1)
  pag.click((1515, 520))
  time.sleep(10)
  pag.typewrite(f'{i}')
  time.sleep(1)
  pag.hotkey('ctrl', 'l')
  time.sleep(1)
  pag.typewrite(FOLDER_PATH)
  time.sleep(1)
  pag.hotkey('alt', 's')
  time.sleep(1)
  pag.press('esc')
  time.sleep(1)
  pag.click((1830, 180))
  time.sleep(1)