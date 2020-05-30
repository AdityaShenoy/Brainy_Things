import curses
import time

scr = curses.initscr()

curses.curs_set(0)
curses.noecho()
curses.cbreak()
scr.keypad(True)

scr.addstr(5, 5, 'Hello')
scr.refresh()
time.sleep(5)

curses.curs_set(1)
curses.echo()
curses.nocbreak()
scr.keypad(False)

curses.endwin()