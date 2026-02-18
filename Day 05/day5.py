import sys
sys.path.insert(0, "../")
from AOC import *

def setupIDs(f):
    FRESH = []
    IDS = []
    adding = 0 #0 = fresh, 1 = ids
    for line in f:
        if (line == "\n"):
            adding = 1
        elif (adding == 0) :
            FRESH.append(line.strip())
        else:
            IDS.append(line.strip())
    return FRESH, IDS

def part1(f):
    FRESH, IDS = setupIDs(f)
    
    count = 0
    for ID in IDS:
        for freshRange in FRESH:
            lower = int(freshRange.split("-")[0])
            upper = int(freshRange.split("-")[1])
            if(int(ID) >= lower and int(ID) <= upper):
                count += 1
                break
    return count

def part2(f):
    FRESH, _ = setupIDs(f)
    FRESH = sorted(FRESH, key=lambda x: int(x.split("-")[0]))
    
    i = 0
    while(i < len(FRESH) - 1): #rewrite the ranges to remove duplicates
        upperCurr = int(FRESH[i].split("-")[1])     #lower bound of current
        lowerNext = int(FRESH[i + 1].split("-")[0]) #upper bound of next
        
        if(lowerNext <= upperCurr):
            newlower = upperCurr + 1
            newUpper = int(FRESH[i + 1].split("-")[1])
            if(newlower <= newUpper): #if this range still makes sense, such that the lower bound is less than OR EQUAL to the upper.
                FRESH[i + 1] = str(newlower) + "-" + str(newUpper) #change lower to be one larger than upper to stop double counting, only if the new range actually makes sense
            else:
                FRESH.remove(FRESH[i + 1]) #remove it if it doesn't. 
                i -= 1 #would love to use C style for loops but i dont think python does those?
        i += 1
        
    count = 0
    for freshRange in FRESH:
            lower = int(freshRange.split("-")[0])
            upper = int(freshRange.split("-")[1])
            count += upper - lower + 1
    return count


example = False
with open("example.txt" if example else "input.txt") as f:
    #run(func, file, part#, boolean, answer to example, answer to actual problem)
    run(part1, f, 1, example,    exampleAnswer=4,  inputAnswer=525)
    run(part2, f, 2, example,    exampleAnswer=20, inputAnswer=333892124923577)