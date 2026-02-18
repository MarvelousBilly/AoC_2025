import subprocess
import pathlib
import re
import sys
from stopwatch import Stopwatch
import os

ROOT = pathlib.Path(__file__).parent

def main():
    day_dirs = sorted(
        d for d in ROOT.iterdir()
        if d.is_dir() and re.match(r"Day \d+", d.name)
    )
    
    for day_dir in day_dirs:
        day_number = re.search(r"\d+", day_dir.name).group()
        script = day_dir / f"day{int(day_number)}.py"

        if script.exists():
            print(f"\n=== Running {script} ===")
            subprocess.run(
                [sys.executable, script.name],
                cwd=day_dir,
                env={**os.environ, "AOC_BULK": "1"}
            )
        else:
            print(f"Skipping {day_dir} (no matching script found)")

if __name__ == "__main__":
    sw = Stopwatch()
    
    sw.start()
    main()
    sw.stop()
    print("\n=== ALL COMPLETE ===")
    print(f"Total Duration:", end = " ")
    print(f"[{sw.elapsed / 60:.2f}m]" if sw.elapsed > 60 else f"[{sw.elapsed:.2f}s]" if sw.elapsed > 0.1 else f"[{sw.elapsed * 1000:.2f}ms]")
