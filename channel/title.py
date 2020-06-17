import curses
from time import sleep

# ogre
brainy_things = r'''   ___           _               _____ _     _                 
  / __\_ __ __ _(_)_ __  _   _  /__   \ |__ (_)_ __   __ _ ___ 
 /__\// '__/ _` | | '_ \| | | |   / /\/ '_ \| | '_ \ / _` / __|
/ \/  \ | | (_| | | | | | |_| |  / /  | | | | | | | | (_| \__ \
\_____/_|  \__,_|_|_| |_|\__, |  \/   |_| |_|_|_| |_|\__, |___/
                         |___/                       |___/     '''

# smslant
# title = r'''   _____ __                          _   _  __           __             
#   / __(_) /  ___  ___  ___ _________(_) / |/ /_ ____ _  / /  ___ _______
#  / _// / _ \/ _ \/ _ \/ _ `/ __/ __/ / /    / // /  ' \/ _ \/ -_) __(_-<
# /_/ /_/_.__/\___/_//_/\_,_/\__/\__/_/ /_/|_/\_,_/_/_/_/_.__/\__/_/ /___/'''

title = r'''   ______                      ___  _        __  
  / __/ /__ ____  ___  __ __  / _ )(_)______/ /__
 / _// / _ `/ _ \/ _ \/ // / / _  / / __/ _  (_-<
/_/ /_/\_,_/ .__/ .__/\_, / /____/_/_/  \_,_/___/
          /_/  /_/   /___/                       '''

def main(scr):
  curses.curs_set(0)
  h, w = scr.getmaxyx()
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
  
  clear = scr.clear
  refresh = scr.refresh
  getch = scr.getch
  on = lambda x: scr.attron(curses.color_pair(x))
  off = lambda x: scr.attroff(curses.color_pair(x))
  add = lambda y, x, s: scr.addstr(y, x, s)
  
  def center_coords(text_height, text_width):
    if type(text_height) is not int:
      text_height = len(text_height)
    if type(text_width) is not int:
      text_width = len(text_width)
    return (h - text_height) // 2, (w - text_width) // 2
    
  def print_left_to_right(msg, color_pair):
    on(color_pair)
    msg_lines = msg.split('\n')
    y, x = center_coords(msg_lines, msg_lines[0])
    for ix, chars in enumerate(zip(*msg_lines)):
      for iy, char in enumerate(chars):
        add(y + iy, x + ix, char)
      refresh()
      sleep(0.01)
    off(color_pair)

  print_left_to_right(brainy_things, 1)
  # sleep(5)
  getch()
  
  clear()
  print_left_to_right(title, 2)
  # sleep(5)
  getch()

curses.wrapper(main)