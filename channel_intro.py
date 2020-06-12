import time
import curses
s = 'if programming is hard or boring:\n' \
    '  return simple(programming) and fun(programming)'

def main(scr):

  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
  y, x = scr.getmaxyx()[0] // 2, 0

  scr.attron(curses.color_pair(1))
  for c in 'if ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  scr.attroff(curses.color_pair(1))

  for c in 'programming ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1

  scr.attron(curses.color_pair(1))
  for c in 'is ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  scr.attroff(curses.color_pair(1))

  for c in 'hard ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1

  scr.attron(curses.color_pair(1))
  for c in 'or ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  scr.attroff(curses.color_pair(1))

  for c in 'boring:':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  
  y, x = y + 1, 0

  scr.attron(curses.color_pair(1))
  for c in '  return ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  scr.attroff(curses.color_pair(1))

  for c in 'simple(programming) ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1

  scr.attron(curses.color_pair(1))
  for c in 'and ':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  scr.attroff(curses.color_pair(1))

  for c in 'fun(programming)':
    scr.addstr(y, x, c)
    scr.refresh()
    time.sleep(0.1)
    x += 1
  
  time.sleep(3)

curses.wrapper(main)