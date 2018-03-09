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

'''
    Auxilary functions

'''
# this function takes in the URL or text file as command line argument
def read_file(link):
    pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if pattern.match(link):
        req=urllib.request.urlopen(link)
        buffer=req.read().decode('utf-8')
    else:
        buffer=open(link,'r').read()
    return buffer


# use regEx to split up the inputed lines into 5 variables
def get_cmd(line,L):
    pattern2 = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    regclean = pattern2.match(line)
    if regclean != None:
        cmd,x1,y1,x2,y2 = regclean.groups()
        x1,y1,x2,y2 = int(x1), int(y1), int(x2), int(y2)
        if x1<0: x1=0
        if y1<0: y1=0
        if x2>=L: x2=L-1
        if y2>=L: y2=L-1
        return cmd, x1, y1, x2, y2
    else:
        return None, None, None, None, None
