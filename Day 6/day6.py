import re
from stopwatch import Stopwatch

def part1(f):
    rows = []
    for line in f:
        newRow = [l for l in line.strip().split(" ")]
        rows.append([])
        for r in newRow:
            if(r != ""):
                rows[len(rows)-1].append(r) #ugly as sin babyyy

    count = 0
    func = "+"
    rowCounts = 0
    for element in range(0,len(rows[0])):
        func = rows[len(rows)-1][element]
        rowCounts = 0 if func == "+" else 1
        for row in range(len(rows)-2, -1, -1):
            if(func == "+"):
                rowCounts += int(rows[row][element]) #what the fuck even is this
            else: # *
                rowCounts *= int(rows[row][element])
        count += rowCounts
    return count

def part2(f):
    lines = [line for line in f]
    func = "+"
    count = 0
    totals = []
    for i in range(0, len(lines[0]) - 1): #for each character in a line (so we can grab every line at the same place)
        
        if(lines[len(lines)-1][i] == "*"): #if the last row matches a math function, set it to that and handle the default value for * and + differently.
            func = "*"
            total = 1
        elif(lines[len(lines)-1][i] == "+"):
            func = "+"
            total = 0
        #but dont change it if theres no function.
            
        num = "" #resultant number for that column
        for LC in range(0, len(lines) - 1): #for each digit in the row, ignoring the function row
            num += lines[LC][i]
    
        if(num.strip() != ""): #if this number isn't blank (so ignore the blank columns)
            if(func == "+"): 
                total += int(num)
            else: # *
                total *= int(num) #change total based on function
    
        elif(lines[0][i].strip() == "" and total > 1): #if the number IS blank (can change to or end of line but it wants to break and idc enough)
            count += total #add to the running total
            total = 1
            
    count += total #once more because the loop breaks on the last one lmao
    return count # wow!


with open("input.txt") as f:
    stopwatch = Stopwatch()

    stopwatch.start()
    num = part1(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == 5316572080628)
    
    f.seek(0)
    stopwatch.reset()
    
    stopwatch.start()
    num = part2(f)
    stopwatch.stop()
    print(num)
    print(stopwatch.report())
    assert(num == 11299263623062)