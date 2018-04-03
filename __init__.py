import sys
import argparse
import requests
import json

API_URL = "https://api.gotinder.com/"
TINDER_AUTH_TOKE = "#########"

def get_user_information(header, user):
    req = requests.get(API_URL + "user/recs", header = header)
    if req.status_code == 200:
        data = json.loads(req.text)
        print(json.dumps(data, indent = 2, sort_keys = False))


def like(header):
    req = requests.get(API_URL + "user/recs")
    if req.status_code == 200:
        data = json.loads(req.text)
        print("~~~ Liking now ~~~")
        with open("profile.txt", "a") as outfile:
            for profile in data["results"]:
                liked = requests.get(API_URL + "like/" + profile["id"], header = header)
                if liked.status_code == 200:
                    if profile["name"] == "Tinder team":
                        print("Your API key has reached its limit, try again at the start of the hour!")
                        return 1
                    line = "liked >>" + profile["id"] + profile["name"]
                    print(line)
                    outfile.writable()
                    outfile.write(line + " \n")
                else:
                    print("Error liking the user: " + profile["name"] + "with the ID: " + profile["id"])
                    print("~~~ Complete You shall not be single for long! ~~~")
                    return 0
            else:
                print("Not able to like anyone at this time.")
                print("You are either banned from tinder or your API key currently has reached its limit")
                return 1

parser = argparse._ArguementParser(description = "Who needs to do tinder manually?")
parser.add_argument("user", metavar = "user", help = "Do you really need fucking help with this?", action = "store", nargs = "?????")
args = parser.parse_args()

if TINDER_AUTH_TOKE == "":
    print("You need to add in your tinder authentication token to use this script!")
    sys.exit(1)
    header = {"Content-Type": "application/json", "X-Auth-Token": TINDER_AUTH_TOKE}
    r = 0
    if args.user is not None:
        r = get_user_information(header, args.user)
    else:
        r = like(header)
        sys.exit(r)