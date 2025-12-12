from stopwatch import Stopwatch

def run(part, f, partNumber, example, exNum, ptNum):
    sw = Stopwatch()
    sw.start()
    num = part(f)
    sw.stop()
    print(f"Part #{partNumber}: {num}", end = " ")
    print(f"[{sw.elapsed:.2f}s]" if sw.elapsed > 0.1 else f"[{sw.elapsed * 1000:.2f}ms]")
    if(type(ptNum) is list): #lower and upper bounds (not inclusive)
        assert(num == exNum if example else ptNum[1] > num > ptNum[0])
        if(not example): print("\t Check this output?")
    else:
        assert(num == (exNum if example else ptNum))
    print()
    f.seek(0)