from stopwatch import Stopwatch
from math import prod as p
from itertools import islice as i
from re import split as s

def part1(f):
    #Funny teehee oneliner because i was bored
    return sum(p(map(int, l[0:2])) >= 9 * sum(map(int, l[3:])) for l in (s("\D", c.strip()) for c in i(f,30,None)))

def part2(f):
    return "Advent of Code 2025 Complete!"

def run(part, f, partNumber, example, exNum, ptNum):
    sw = Stopwatch()
    sw.start()
    num = part(f)
    sw.stop()
    print(f"Part #{partNumber}: {num}", end = " ")
    print(f"[{sw.elapsed:.2f}s]" if sw.elapsed > 0.1 else f"[{sw.elapsed * 1000:.2f}ms]")
    assert(num == (exNum if example else ptNum))
    f.seek(0)

example = False
with open("example.txt" if example else "input.txt") as f:
    run(part1, f, 1, example, 2, 546) #lmao this literally doesn't work for the example the damn troll
    run(part2, f, 2, example, 2, "Advent of Code 2025 Complete!")
