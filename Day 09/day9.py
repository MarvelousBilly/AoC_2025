import math
from stopwatch import Stopwatch
from tqdm import tqdm
from shapely.geometry import LineString, Point, Polygon

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
    def getPoints(geom):
        if geom.geom_type == "LineString":
            return list(geom.coords)
        elif geom.geom_type == "MultiPoint":
            return [tuple(p.coords[0]) for p in geom.geoms]
        
    def test(a, b, areas):

        return areas

        
    boxes = [[int(coord) for coord in box.strip().split(",")] for box in f]
    lenData = len(boxes)
    areas = [] * lenData
    
    poly = Polygon(boxes)
    polyExt = LineString(list(poly.exterior.coords))
        
    largestArea = 0

    for a in tqdm(range(0, lenData)):
        pointA = Point(boxes[a][0], boxes[a][1])
        for b in range(a + 1, lenData): #find the smallest distance such that both diagonal lines lie entirely within the polygon, and don't intersect any edges
            pointB = Point(boxes[b][0], boxes[b][1])
            pointC = Point(boxes[a][0], boxes[b][1])
            pointD = Point(boxes[b][0], boxes[a][1])
            
            diag1 = LineString([pointA, pointB])
            diag2 = LineString([pointC, pointD])
            
            inters1 = polyExt.intersection(diag1)
            
            if(len(getPoints(inters1)) == 2): #it only touches the polygons at the verticies
                checkPoint1 = diag1.interpolate(diag1.length * 0.001)
                if poly.contains(checkPoint1):
                    #if the intersections are just the original points (lie on the polygon?) or
                    checkPointC = diag2.interpolate(diag2.length * 0.001) #right next to C
                    checkPointD = diag2.interpolate(diag2.length * 0.999) #right next to D
                    if(poly.contains(checkPointC) and poly.contains(checkPointD)):
                        #print(f"The rectangle ({a}, {b}) completely lies within the polygon.")
                        areas.append((area(boxes[a], boxes[b]), [a, b]))
               
    areas = sorted(areas, key=lambda x: x[0], reverse=True)

    return areas[0][0]


example = False
with open("example.txt" if example else "input.txt") as f:
    stopwatch = Stopwatch()

    stopwatch.start()
    num = part1(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (50 if example else 4790063600))
    
    f.seek(0)
    stopwatch.reset()
    
    stopwatch.start()
    num = part2(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    if(example):
        assert(num == 24)
    else:
        assert (num == 1516172795)
    #assert(num == (24 if example else 6095621910))