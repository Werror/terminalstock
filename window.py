#!/usr/bin/env python3.4

print ("hello")

import operator
import curses
from curses import wrapper
from yahoo_finance import Share

from stockList import stockList



__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))

def setupScreen(screen):
    # Clear screen
    screen.clear()

    scrRatio = determineAspectRatio(screen)
    height,width = screen.getmaxyx()

# title window
    #win = curses.newwin(height, width, begin_y, begin_x)
    titleWinHeight = 1
    titleWin = curses.newwin(titleWinHeight, 0, 0, 0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    titleWin.bkgd(" ", curses.color_pair(1))
    titleWinHeight,titleWinWidth = titleWin.getmaxyx()
    titleStr = "TeminalStock Ver " + __version__
    titleWin.addstr(0, int(titleWinWidth/2 - len(titleStr)/2), titleStr)

# left window
    #win = curses.newwin(height, width, begin_y, begin_x)
    leftWinWidth = int(3*width/10)
    leftWin = curses.newwin(0, leftWinWidth, titleWinHeight, 0)
    leftWin.box()

    stockListDisplay = stockList(leftWin, ["YHOO", "APLE", "APLL", "GOOG"])
    stockListDisplay.fetchData();
    stockListDisplay.display();

# righttop window
    righttopWinHeight = int(4.5*height/10)
    righttopWin = curses.newwin(righttopWinHeight, 0, titleWinHeight, leftWinWidth)
    righttopWin.box()

# rightmid window
    rightmidWinHeight = int(3.5*height/10)
    rightmidWin = curses.newwin(rightmidWinHeight, 0, titleWinHeight + righttopWinHeight, leftWinWidth)
    rightmidWin.box()

# rightbot window
    rightbotWin = curses.newwin(0, 0, titleWinHeight + righttopWinHeight + rightmidWinHeight, leftWinWidth)
    rightbotWin.box()
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE)
    rightbotWin.bkgd("x", curses.color_pair(2))

    # This raises ZeroDivisionError when i == 10.
    #for i in range(0, 11):
        #v = i+1
        #screen.addstr(2*i, 0, '10 divided by {} is {}'.format(v, 10/v))

    screen.refresh()
    titleWin.refresh()
    leftWin.refresh()
    righttopWin.refresh()
    rightmidWin.refresh()
    rightbotWin.refresh()
    screen.getkey()

def determineAspectRatio(screen):
    ratio4x3 = 4/3
    ratio3x4 = 3/4
    ratio1x1 = 1
    ratio16x9 = 16/9
    ratio9x16 = 9/16

# https://docs.python.org/3/library/enum.html should be used
    x = {1:ratio4x3, 2:ratio3x4, 3:ratio1x1, 4:ratio16x9, 5:ratio9x16}
    ratioList = sorted(x.items(), key=operator.itemgetter(1))

    height,width = screen.getmaxyx()
    currentScreenRatio = 1#width/height

    for (screenId, ratio) in ratioList:
        if (currentScreenRatio == ratio):
            return screenId

def main(stdscr):
    setupScreen(stdscr)

if __name__ == "__main__":
    wrapper(main)
