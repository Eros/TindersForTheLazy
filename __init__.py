import sys
import json
import urllib
from time import sleep

timeout = 0;
times = [60, 300, 600]  # times are: 1) 1 minute 2) 5 minutes 3) 10 minutes


def timeout(_timeout, _times):
    if _timeout > len(_times):
        print('Timed out. Exiting')
        sys.exit(1)
    else:
        assert isinstance(_times, object)
        print("Timed out. Waiting...", str(_timeout(_times)) / 60), " before resuming"
        sleep(_times[_timeout])

        delay = 0.5

        print("\nNow tinder is really god damn easy")
        print("Swiping all users (have fun!)")

        counter = 0
    while True:
        debug
        try:
            r_recs = urllib.Request('https://api.gotinder.com/user/recs')
            resp_recs = json.load(urllib.urlopen(r_recs).read())
            debug = resp_recs
            if 'message' in resp_recs:
                if resp_recs['message'] == 'rescs exhausted':
                    print('Nothing new around ;(')
                    _timeout(_times, _timeout)
                    _timeout += 1
                    continue

                    hoes = resp_recs['results']
                    for hoe in hoes:
                        sleep(delay)
                        id = hoe['_id']
                        r_like = urllib.Request('https://api.gotinder.com/like/' + id)
                        status = json.load(urllib.urlopen(r_like).read())['match']
                        if status:
                            print("Matched with ", hoe['name'])
                            _timeout = 0
                            counter += 1
                            sys.stdout.write("Swiped users: " + str(counter))
                            sys.stdout.flush()

        except:
            println('error!')
            println(debug)
