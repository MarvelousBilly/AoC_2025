import re
import math
import numpy as np

def part1(f):
    total = 0
    for line in f:
        line = line.strip()
        
        index1 = int(np.argmax(list(line[:-1]))) + 1
        index2 = int(np.argmax(list(line[index1:]))) + index1
        
        total += int(line[index1 - 1]) * 10 + int(line[index2])
        
    return total

def part2(f):
    total = 0
    for line in f:
        line = line.strip()
        number = 0
        prevIndex = 0
        for x in range(11, -1, -1):
            slice_ = line[prevIndex:(None if x == 0 else -x)] #if x = 0, it has to be treated as None so the loop works correctly
            index = int(np.argmax(list(slice_))) + prevIndex
            number = int(line[index]) + 10 * number
            prevIndex = index + 1
        total += number
    return total


with open("input.txt") as f:
    num = part1(f)
    print(num)
    assert(num == 17493)
    
    f.seek(0)
    
    num = part2(f)
    print(num)
    assert(num == 173685428989126)

