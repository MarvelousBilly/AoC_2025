import math
from stopwatch import Stopwatch
from functools import lru_cache
from tqdm import tqdm

class graph():
    def __init__(self, name):
        self.points = []
        self.name = name
    
    def add(self, nextTrees):
        for d in nextTrees:
            try:
                self.points.append(graphDict[d]) #attach the previous tree to this one
            except:
                newGraph = graph(d)
                graphDict[d] = newGraph
                self.points.append(newGraph) #make a new tree
                
    def traverse1(self):
        count = 0
        for p in self.points:
            count += p.traverse1()
        if(self.name == "out"):
            count = 1
        return count
    
    def reverseEdges(self, rev, seen = None):
        if(seen is None):
            seen = set()
        if(self.name in seen):
            return rev
        seen.add(self.name)
            
        for node in self.points:                  #for every sub-node
            rev.setdefault(node.name, [])         #make an entry in the rev dict if possible
            if(self.name not in rev[node.name]):
                rev[node.name].append(self.name)  #append the current node to that dict 
            
            node.reverseEdges(rev, seen)
        return rev
        
    def reverseSearch(self, rev):
        reachable = set() #all nodes that can reach this node (self), up to svr
        seen = set() #all nodes that you've seen
        
        def DFS(node):
            if(node.name in seen): #have we done this ?
                return #dont !
            seen.add(node.name) #now we're doing it !
            for up in rev[node.name]:
                reachable.add(up)
                if up == "svr": #top of graph
                    continue
                DFS(graphDict[up])
        
        DFS(self)
        reachable.add(self.name)
        return reachable
        
    
    def traverse2(self, fftReach, dacReach):
        # so. TIL. the inputs are simple enough to not need any fancy shit. you can literally just DFS with memoization and THATS GOOD ENOUGH
        # god why is this day 11
        # anyway i'm keeping the reversed graph pruning idea even though its a bit slower because its cool and i can look at it later if i need to
        
        @lru_cache(None) #memoization or something
        def DFS(nodeName, reachedFFT = False, reachedDAC = False):
            total = 0
        
            if(nodeName == "fft"):
                reachedFFT = True
            elif(nodeName == "dac"):
                reachedDAC = True
            elif(nodeName == "out"): #if reached end, you mustve passed through both nodes :)
                return reachedFFT and reachedDAC

            for p in graphDict[nodeName].points:
                if((p.name in fftReach or reachedFFT) and (p.name in dacReach or reachedDAC)): #if p can possibly reach fft AND dac, or has already (cool pruning bit that isnt needed)
                    total += DFS(p.name, reachedFFT, reachedDAC) #recurse through this node. if it reached out, that means it must've passed through both
                    
            return total
        
        return DFS(self.name)
    
def generateGraph(f):
    stopwatch = Stopwatch()
    stopwatch.start()
    data = [[l.strip().split(": ")[0], l.strip().split(": ")[1].split(" ")] for l in f]
    for d in data:
        graphDict.setdefault(d[0], graph(d[0])).add(d[1])
    stopwatch.stop()
    print(stopwatch.report())
    
        
def part1():
    return graphDict["you"].traverse1() #you to out

def part2():
    startNode = graphDict["svr"]
    fft = graphDict["fft"]
    dac = graphDict["dac"]
    
    rev = graphDict["svr"].reverseEdges({}) #get a list of the nodes in reverse. for example, if svr: aaa bbb, then rev will have {'aaa': ['svr'], 'bbb': ['svr']} as aaa and bbb are reached from svr.
    
    fftSearch = fft.reverseSearch(rev) #this does DFS down this new tree to get a list of every node that can possibly reach FFT
    dacSearch = dac.reverseSearch(rev) #this does DFS down this new tree to get a list of every node that can possibly reach DAC
    
    return graphDict["svr"].traverse2(fftSearch, dacSearch) #svr to out, passing through fft and dac

def run(part, example, exNum, ptNum):
    stopwatch = Stopwatch()
    stopwatch.start()
    num = part()
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == (exNum if example else ptNum))
    
    
graphDict = {}
example = False
with open("example1.txt" if example else "input.txt") as f:
    generateGraph(f) #not timing because fuck it
    run(part1, example, 5, 668)

with open("example2.txt" if example else "input.txt") as f:
    if(example):
        graphDict = {} #reset because there are two examples with different data
        generateGraph(f) #set up again
    run(part2, example, 2, 294310962265680)
