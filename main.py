from instagrapi import Client
import random as rand

moviename = "Barbie"
myname = "Luke"

with open("creds.txt", "r") as f:
    user, pasw = f.read().splitlines()
    f.close()

with open("actors.txt", "r") as f:
    cast = dict() 
    for x in f.read().splitlines():
        name, handle = x.split(', ')
        if handle == 'none':
            continue
        cast[name] = handle
    f.close()

# straight up loggin in everytime is sus for instagram, so instead store a session from start_session.py and the load it here 
client = Client()
client.load_settings("session.json")
client.login(user, pasw) # this doesn't actually login from scratch, just uses the session. dw about it basically

# see if session is valid, if not we have to login again
try: 
    client.get_timeline_feed()
except:
    print("Session Invalid. need to log in again (run start_session.py)")
    exit()

for name, handle in cast.items():
    with open("letters/" + str(rand.randint(1, 6)) + ".txt", "r") as f:
        letter = f.read().replace("[Actor's Name]", name.split(" ")[0])
        letter = letter.replace("[Movie Title]", moviename)
        letter = letter.replace("[Your Name]", myname)

client.direct_send("hello", [int(client.user_id_from_username("bigfloppa.irony"))])
