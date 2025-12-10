import math
from stopwatch import Stopwatch


#maybe todo optimization: sort by x position, and go down that list grabbing distances, but as soon as the distance to the x position is greater than the smallest youve seen so far, exit out early and return that smallest distance
def part1(f, c, Part2):
    def distance(a, b): #two arrays
        return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2) #wow
    
    boxes = [[int(coord) for coord in box.strip().split(",")] for box in f]
    lenData = len(boxes)
    distances = [] * lenData
    
    for boxIndex in range(0, lenData):
        for otherBox in range(boxIndex + 1, lenData): #find the smallest distance
            distances.append((distance(boxes[boxIndex], boxes[otherBox]), [boxIndex, otherBox]))          
    distances = sorted(distances, key=lambda x: x[0])
        
    circuits = []
    totalWires = 0
    for d in distances: #loop through from smallest to largest        
        pair = d[1] #box a and box b
            
        target = [-1, -1]
        for searchIndex, circ in enumerate(circuits):
            in0 = pair[0] in circ
            in1 = pair[1] in circ
            if in0:
                target[0] = searchIndex
            if in1:
                target[1] = searchIndex
                
        t0 = target[0] == -1
        t1 = target[1] == -1
        
        if(t0 and t1):                                        #neither end was found
            circuits.append(pair)                             # add to ciruit list straight up
            
        elif((t0 and not t1) or (not t0 and t1)):             #one end was found
            if(t0):
                circuits[max(target)].append(pair[0])
            if(t1):
                circuits[max(target)].append(pair[1])
                
        elif(not t0 and not t1) and (target[0] != target[1]): #both ends were found and different
            circuits[target[0]] += circuits[target[1]]
            circuits.remove(circuits[target[1]])
            
        if(not Part2):
            totalWires += 1
            if(totalWires >= c): #only do 10, or 1000
                break
        else:
            if(len(circuits[0]) == lenData): #once they've merged
                break
                
    total = 0
    if(not Part2):
        circuits = sorted(circuits, key=len, reverse=True)
        total = len(circuits[0]) * len(circuits[1]) * len(circuits[2]) #multiply the 3 largest        
    else:
        total = boxes[pair[0]][0] * boxes[pair[1]][0] #multiply the x coords of the last two to connect
    
    return total

def part2(f):
    return part1(f, 10, True) #lmao just do part 1 but sliiiightly different


example = False
with open("example.txt" if example else "input.txt") as f:
    stopwatch = Stopwatch()

    stopwatch.start()
    num = part1(f, 10 if example else 1000, False) #conditional formula for example War
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (40 if example else 153328))
    
    f.seek(0)
    stopwatch.reset()
    
    stopwatch.start()
    num = part2(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (25272 if example else 6095621910))
