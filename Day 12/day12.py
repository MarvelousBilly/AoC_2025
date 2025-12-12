import math
from stopwatch import Stopwatch
from functools import lru_cache
from tqdm import tqdm
    
def generateGraph(f):
    stopwatch = Stopwatch()
    stopwatch.start()
    data = [[l.strip().split(": ")[0], l.strip().split(": ")[1].split(" ")] for l in f]
    for d in data:
        graphDict.setdefault(d[0], graph(d[0])).add(d[1])
    stopwatch.stop()
    print(stopwatch.report())
    
        
def part1(f):
    boxCount = [0] * 6
    lines = [l.strip() for l in f]
    
    cnt = 0
    for ln, line in enumerate(lines):
        if ln < 30:
            if(ln % 5 == 4):
                box = "".join(lines[(ln // 5) * 5:((ln+1) // 5) * 5]) #could've hardcoded this but i'm this far in you think im hardcoding (aside from the linecounts ignore those)
                boxCount[ln // 5] = box.count("#")
                
        else: #how tall the boxes are in inputs
            size = int(line.split(":")[0].split("x")[0]) * int(line.split(":")[0].split("x")[1]) #what on EARTH is this btw. wrote it to just see if the idea was right (it was) but damn this sucks
            boxes = line.split(": ")[1].strip().split(" ") #barf

            total = 0
            for i, num in enumerate(boxes):
                total += boxCount[i] * int(num)
                
            if(size >= total):
                cnt += 1
    
    
    return cnt

def run(part, f, example, exNum, ptNum):
    stopwatch = Stopwatch()
    stopwatch.start()
    num = part(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (exNum if example else ptNum))

example = False
with open("example.txt" if example else "input.txt") as f:
    run(part1, f, example, 2, 546) #lmao this literally doesn't work for the example the damn troll
