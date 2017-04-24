#!/usr/bin/env python3.4

import curses
from yahoo_finance import Share

class stockList(object):
    def __init__(self, window, symbolList):
        self.window = window
        self.symbolList = symbolList
        self.shareObjList = []

    def fetchData(self):
        for symbol in self.symbolList:
            symbolObj = Share(symbol)
            self.shareObjList.append(symbolObj)

    def display(self):
        for i in range(len(self.symbolList)):
            displayStr = '{}:{}'.format(self.symbolList[i], self.shareObjList[i].get_price())
            self.window.addstr(i+1, 1, displayStr)

