

import random
import sys

class FastRain():

    def __init__(self, width=6, height=53, rainMult=500):
        self.width = width
        self.height = height
        self.rainMult = rainMult
        self.rain = [[16] * width for i in range(height)]
        self.count0 = 3
        self.count1 = 750


    def startRain(self):        
        # create a list that will start new rain 
        rainStart = []
        for i in range(self.width):
            start = random.randint(1, (self.rainMult * self.count0))
            # decrement count to simulate the rain starting 
            if (self.count1 == 1): 
                if (self.count0 > 1):
                    self.count0 -= 1
                    self.count1 += 750
            else:
                self.count1 -= 1

            # insert rainfall
            if (start == 1):
                rainStart.append(1)
            else:
                rainStart.append(16)
    
        return rainStart


    def insertRainStart(self, rainStart):
        # copy rainstart onto rain matrix 
        for i in range(len(rainStart)):
            if (self.rain[0][i] > rainStart[i]):
                self.rain[0][i] = rainStart[i]


    def update(self):
        # iterate through the board and update all indeces
        for y in range(3, self.height, 3):
            for x in range(self.width):            
                if (self.rain[y - 3][x] == 1):
                    self.rain[y][x] = 0
                    self.rain[y - 1][x] = 0
                    self.rain[y - 2][x] = 0

        for y in range(self.height):
            for x in range(self.width):
                if (self.rain[y][x] < 16):
                    self.rain[y][x] += 1    

        # insert new rain pattern
        rainStart = self.startRain()
        self.insertRainStart(rainStart)        





