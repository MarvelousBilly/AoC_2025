import re
import math

def checkRelative(xoff, yoff, sizex, sizey, data):
    return 1 if (not (xoff < 0 or yoff < 0 or xoff > sizex-1 or yoff > sizey-1) and (data[xoff][yoff] == "@")) else 0

def part1(data):
    total = 0
    sizex = len(data[0]) - 1
    sizey = len(data) - 1
    
    newData = data[:]
    adj = [(-1,-1), (0, -1), (1, -1),
           (-1, 0),          (1,  0),
           (-1, 1), (0,  1), (1,  1)]
    
    for x in range(0, sizex + 1):
        for y in range(0, sizey + 1):
            count = 0
            if(data[x][y] == "@"):
                for xoff,yoff in adj:
                    xoff += x
                    yoff += y
                    count += 1 if (not (xoff < 0 or yoff < 0 or xoff > sizex or yoff > sizey) and (data[xoff][yoff] == "@")) else 0

                if(count < 4):
                    newData[x] = newData[x][:y] + "X" + newData[x][y+1:]
                    total += 1
                
    
    return total, newData

def part2(data):
    def replaceX(data): #replace all "X" in a list of strings with "."
        newData = data
        for i, line in enumerate(data):
            newData[i] = re.sub("X", ".", line)
        return newData
    
    count = 0
    step = 0    
    while(True):
        step+=1
        amt,data = part1(data)
        if(amt == 0):
            break
        
        #uncomment these to see the step by step :)
        #print(f"Step {step}:")
        #print("\n".join(data))
        #print(f"Removed {amt} boxes!")
        #print()
        
        data = replaceX(data)
        count += amt
        
    return count


with open("input.txt") as f:
    data = f.read()
    data = data.split("\n")
    
    num,_ = part1(data)
    print(num)
    assert(num == 1626)
    
    f.seek(0)
    
    num = part2(data)
    print(num)
    assert(num == 9173)