import sys
sys.path.insert(0, "../")
from AOC import *

from tqdm import tqdm
from shapely.geometry import LineString, Point, Polygon, box
from shapely.prepared import prep

#maybe todo optimization: sort by x position, and go down that list grabbing distances, but as soon as the distance to the x position is greater than the smallest youve seen so far, exit out early and return that smallest distance
def part1(f):
    def area(a, b): #two arrays
         return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
    
    boxes = [[int(coord) for coord in box.strip().split(",")] for box in f]
    lenData = len(boxes)
    
    largestArea = 0
    for boxIndex in range(0, lenData):
        for otherBox in range(boxIndex + 1, lenData): #find the smallest distance
            largestArea = max(largestArea, area(boxes[boxIndex], boxes[otherBox]))
    
    return largestArea

def part2(f):
    def area(a, b): #two arrays
         return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        
    boxes = [[int(coord) for coord in box.strip().split(",")] for box in f]
    lenData = len(boxes)
    
    poly = Polygon(boxes)
    prepared_poly = prep(poly)
    
    largestArea = 0

    for a in range(lenData):
        for b in range(a + 1, lenData): #find the largest box that fits entirely within the polygon
            
            boxArea = area(boxes[a], boxes[b])
            if (boxArea) > largestArea: #only do this one if it could be larger
                
                minx = min(boxes[a][0], boxes[b][0])
                maxx = max(boxes[a][0], boxes[b][0])
                miny = min(boxes[a][1], boxes[b][1])
                maxy = max(boxes[a][1], boxes[b][1])
                rect = box(minx, miny, maxx, maxy)

                if prepared_poly.covers(rect):
                    largestArea = max(boxArea, largestArea)
                    
    return largestArea


example = False
with open("example.txt" if example else "input.txt") as f:
    #run(func, file, part#, boolean, answer to example, answer to actual problem)
    run(part1, f, 1, example,    exampleAnswer=50, inputAnswer=4790063600)
    run(part2, f, 2, example,    exampleAnswer=24, inputAnswer=1516172795)