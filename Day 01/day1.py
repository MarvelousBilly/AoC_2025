import sys
sys.path.insert(0, "../")
from AOC import *

import math

def part1(f):
    total = 0
    dial = 50
    for line in f:
        direction = -1 if "L" == line[0] else 1
        amt = int(line[1:])
        dial = (dial + direction * amt) % 100
        if(dial == 0): #if the dial is zero, and the turn is 1-99, it can NEVER increase the count
            total += 1
            
    return total

def part2(f):
    total = 0
    dial = 50
    for line in f:
        direction = -1 if "L" == line[0] else 1
        amt = int(line[1:])
        
        total += math.floor(amt / 100) #shrink the rotations to only up to 99, but add the extras to the count
        amt = amt % 100
        
        totalRots = (dial + direction * amt) #final rotation position (before range change to 0-99)
        newDial = totalRots % 100
        if(dial != 0 and newDial != totalRots or newDial == 0): #if the dial is zero, and the turn is 1-99, it can NEVER increase the count
            total += 1
        dial = newDial
        
    return total


example = False
with open("example.txt" if example else "input.txt") as f:
    #run(func, file, part#, boolean, answer to example, answer to actual problem)
    run(part1, f, 1, example,    exampleAnswer=3, inputAnswer=1055)
    run(part2, f, 2, example,    exampleAnswer=6, inputAnswer=6386)