# -*- coding: utf-8 -*-

"""Main module."""
import sys
import re
import urllib.request
import time

class LED_Grid():
    '''Class defined for the LED board'''
    def __init__ (self,L):
        self.grid = [[False]*L for _ in range(L)]
        self.size=L

# this function turns a rectangle of light, topleft LED to btmRight
    def turn_on(self, x1,y1,x2,y2):
        if x1 <= x2 and y1<= y2:
            for i in range(x1,x2+1):
                for j in range (y1, y2+1):
                    self.grid[i][j] = True

# turn off selected lights within the grid
    def turn_off(self, x1,y1,x2,y2):
        if x1 <= x2 and y1 <= y2:
            for i in range(x1,x2+1):
                for j in range (y1, y2+1):
                    self.grid[i][j] = False

# switch lights within rectangle one to off or vice-versa
    def switch(self, x1,y1,x2,y2):
        if x1<=x2 and y1 <=y2:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if self.grid[i][j]==True:
                        self.grid[i][j]=False
                    else:
                        self.grid[i][j]=True
