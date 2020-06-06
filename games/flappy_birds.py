import curses
from curses.textpad import rectangle
import time
import random

def main(scr):
  curses.curs_set(0)
  scr.nodelay(1)
  scr.timeout(150)

  height, width = scr.getmaxyx()

  MARGIN = 3
  GAP_WIDTH = 3
  INTER_GAP_WIDTH = 15

  pipe = []
  x = width // 2
  while x < width - MARGIN:
    gap_start = random.randint(MARGIN + 1, height - MARGIN - GAP_WIDTH)
    pipe.append((x, gap_start))
    x += INTER_GAP_WIDTH

  rectangle(scr, MARGIN, MARGIN, height - MARGIN, width - MARGIN)
  
  flappy_bird = '@'
  flappy_y, flappy_x = height // 2, width // 4

  while True:

    for x, gap_start in pipe:
      for y in range(MARGIN + 1, height - MARGIN):
        if y not in range(gap_start, gap_start + GAP_WIDTH):
          scr.addstr(y, x, '|')

    scr.addstr(flappy_y, flappy_x, flappy_bird)
    scr.refresh()
    key = scr.getch()
    if key == 27: # Esc
      break
    scr.addstr(flappy_y, flappy_x, ' ')
    if key == curses.KEY_UP:
      flappy_y -= 1
    else:
      flappy_y += 1
    

curses.wrapper(main)