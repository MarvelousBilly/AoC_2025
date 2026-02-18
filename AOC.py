from stopwatch import Stopwatch
import os

def run(part, f, partNumber, example, exampleAnswer, inputAnswer):   
    if os.getenv("AOC_BULK") == "1":
        example = False
        
    sw = Stopwatch()
    
    sw.start()
    num = part(f)
    sw.stop()
    
    ex = " (Example)" if example else ""
    print(f"Part #{partNumber}{ex}: {num}", end = " ")
    print(f"[{sw.elapsed / 60:.2f}m]" if sw.elapsed > 60 else f"[{sw.elapsed:.2f}s]" if sw.elapsed > 0.1 else f"[{sw.elapsed * 1000:.2f}ms]", end = " ")
    
    if(type(inputAnswer) is list): #lower and upper bounds (not inclusive)
        assert(num == exampleAnswer if example else inputAnswer[1] > num > inputAnswer[0])
        if(not example):
            print("- Within range, check output")
        else:
            print("- PASS")
    else:
        assert(num == (exampleAnswer if example else inputAnswer))
        print("- PASS")

    f.seek(0)