import sys
sys.path.insert(0, "../")
from AOC import *

import re

def Step(data):
    total = 0
    sizex = len(data[0])
    sizey = len(data)
    
    newData = data[:]
    adj = [(-1,-1), (0, -1), (1, -1),
           (-1, 0),          (1,  0),
           (-1, 1), (0,  1), (1,  1)]
    
    for x in range(0, sizex):
        for y in range(0, sizey):
            if(data[x][y] == "@"):
                count = 0
                for xoff,yoff in adj:
                    xoff += x
                    yoff += y
                    count += 1 if ((sizex > xoff >= 0 and sizey > yoff >= 0) and (data[xoff][yoff] == "@")) else 0

                if(count < 4):
                    newData[x] = newData[x][:y] + "X" + newData[x][y+1:]
                    total += 1
                    
    return total, newData

def part1(data):
    data = f.read().split("\n")
    total, _ = Step(data)
    return total

def part2(data):
    data = f.read().split("\n")
    def replaceX(data): #replace all "X" in a list of strings with "."
        for i, line in enumerate(data):
            data[i] = re.sub("X", ".", line)
        return data
    
    count = 0
    step = 0
    
    while(True):
        amt,data = Step(data)
        if(amt == 0):
            break
        
        ### uncomment these to see the step by step :)
        #step+=1
        #print(f"Step {step}:")
        #print("\n".join(data))
        #print(f"Removed {amt} boxes!")
        #print()
        
        data = replaceX(data)
        count += amt
        
    return count


example = False
with open("example.txt" if example else "input.txt") as f:
    #run(func, file, part#, boolean, answer to example, answer to actual problem)
    run(part1, f, 1, example,    exampleAnswer=13, inputAnswer=1626)
    run(part2, f, 2, example,    exampleAnswer=43, inputAnswer=9173)