import re
from stopwatch import Stopwatch

def part1(data):
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

def part2(data):
    def replaceX(data): #replace all "X" in a list of strings with "."
        for i, line in enumerate(data):
            data[i] = re.sub("X", ".", line)
        return data
    
    count = 0
    step = 0
    
    while(True):
        amt,data = part1(data)
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


with open("input.txt") as f:
    stopwatch = Stopwatch()

    data = f.read()
    data = data.split("\n")

    stopwatch.start()
    num,_ = part1(data)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == 1626)
    
    f.seek(0)
    stopwatch.reset()
    
    stopwatch.start()
    num = part2(data)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == 9173)