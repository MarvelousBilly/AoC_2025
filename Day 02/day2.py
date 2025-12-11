import re
import math

def part1(f, r = r"^(.+)\1$"):
    total = 0
    strings = f.read().split(",")
    for IDRange in strings:
        lower = int(IDRange.split("-")[0])
        upper = int(IDRange.split("-")[1])
        for x in range(lower, upper + 1):
            #slow but i really don't know of a more elegant way to solve this than a silly little regex.
            #the only real optimization would be skipping numbers that couldn't be invalid but that would be a LOT more code lmao
            matches = re.findall(r, str(x)) 
            if(matches != []):
                total += x
    return total

def part2(f):
    return part1(f, r"^(.+)\1+$") #the ONLY difference is that there can be two OR MORE of the duplicate string (which is really easy in regex)

with open("input.txt") as f:
    num = part1(f)
    print(num)
    assert(num == 56660955519)
    
    f.seek(0)
    
    num = part2(f)
    print(num)
    assert(num == 79183223243)
