import time
import sys
from pathlib import Path


def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rTime left: {i:2d} seconds")
        sys.stdout.flush()
        time.sleep(1)
    print("\rTime's up!            ")


# countdown(10)


path = Path.cwd()
print(path)
