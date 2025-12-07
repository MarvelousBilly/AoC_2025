import re
from stopwatch import Stopwatch

def part1(f):
    def stringReplace(string, i):
        return string[:i] + "|" + string[i+1:]
    count = 0
    lines = [line.strip() for line in f]
    
    lines[1] = stringReplace(lines[1], lines[0].find("S"))

    for i in range(2, len(lines)):
        for char in range(0,len(lines[i])):
            if(lines[i-1][char] == "|"):
                if(lines[i][char] == "^"):
                    lines[i] = stringReplace(lines[i], char - 1)
                    lines[i] = stringReplace(lines[i], char + 1) # there's never a set of ^^ next to each other :)
                    count += 1
                else:
                    lines[i] = stringReplace(lines[i], char)    
    return count

def part2(f):    
    grid = [list(line.strip()) for line in f]
    
    for i in range(len(grid) - 1, 1, -1): #bottom up, replace the ^s with the number.
        #generate the number from grabbing each index to the left and right, and go down until you see a number or nothing. if you see a number, add it to the current number. if you see nothing, its just adding 1
        
        for char in range(0, len(grid[i])): #can simplify to using .find but eh this works
            if(grid[i][char] == "^"):
                counts = [1,1]
                for down in range(i, len(grid), 1): #start at current position +- 1, and look downwards until you see something
                    for LR,x in enumerate([-1, 1]): #check left and right
                        if(grid[down][char + x] != "."): #if its a number
                            counts[LR] = max(counts[LR], grid[down][char + x]) #grab the max number (and then ideally stop checking downwards but if i take max that works too, just a bit slower)
                        
                newChar = counts[0] + counts[1]
                grid[i][char] = newChar
                
    count = grid[2][grid[0].index("S")]

    return count


with open("input.txt") as f:
    stopwatch = Stopwatch()

    stopwatch.start()
    num = part1(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == 1649)
    
    f.seek(0)
    stopwatch.reset()
    
    stopwatch.start()
    num = part2(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num < 796079939823479)