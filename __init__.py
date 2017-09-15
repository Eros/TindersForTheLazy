import sys
import json
from time import sleep

timeout = 0;
times = [60, 300, 600] #times are: 1) 1 minute 2) 5 minutes 3) 10 minutes

def timeout(timeout, times):
    if timeout > len(times):
        print('Timed out. Exiting')
        sys.exit(1)
    else:
        print("Timed out. Waiting...", str(timeout(times)) / 60), " before resuming"
        sleep(times[timeout])

        delay = 0.5

        print "\nNow tinder is really god damn easy"
        