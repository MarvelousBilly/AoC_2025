import math
from stopwatch import Stopwatch
from z3 import *
import time

def part1(f):
    total = 0
    for line in f:
        lightNeed = line[1:line.find("]")].replace(".", "0").replace("#", "1")
        buttons = [l[0:l.find(")")] for l in line.split("(")[1:]]

        switching = [0] * len(buttons)
        for i, button in enumerate(buttons):
            for switch in button.split(","):
                switching[i] |= (1 << int(switch))
                
        minPresses = 9999
        for x in range(0, 1 << len(switching)): #check every combination of buttons
            X = format(x, f"0{len(switching)}b")
            attempt = 0
            for char in range(0, len(switching)): #just the numbers
                if(X[char] == "1"):
                    attempt ^= switching[char]
            result = format(attempt, f'0{len(lightNeed)}b')
            if(result == lightNeed[::-1]):
                minPresses = min(minPresses, X.count("1"))
                
        total += minPresses
    return total

def part2(f):
    total = 0
    
    for line in f:
        line = line.strip()
        o = Optimize()

        buttons = [l[0:l.find(")")].split(",") for l in line.split("(")[1:]]
        joltage = line[line.find("{")+1:-1].split(",")
        
        xs = [Int(f"x{i}") for i in range(len(buttons))]
        for x in xs:
            o.add(x >= 0) #make sure those are consistent

        for i, jolt in enumerate(joltage):
            buttonsPerJoltage = []
            for j, button in enumerate(buttons):
                for switch in button:
                    if int(switch) == i:
                        buttonsPerJoltage.append(j)
            o.add(Sum([xs[i] for i in buttonsPerJoltage]) == jolt)
        
        o.minimize(Sum(xs))
        
        if(o.check() == sat):
            m = o.model()
            minButtons = sum([m[x].as_long() for x in xs])
            total += minButtons
        else:
            raise Exception("No solution")
            
    return total


example = False
with open("example.txt" if example else "input.txt") as f:
    stopwatch = Stopwatch()

    stopwatch.start()
    num = part1(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (7 if example else 466))
    
    f.seek(0)
    stopwatch.reset()
    
    stopwatch.start()
    num = part2(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (33 if example else 17214))