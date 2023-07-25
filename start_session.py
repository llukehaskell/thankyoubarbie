from instagrapi import Client


with open("creds.txt", "r") as f:
    user, pasw = f.read().splitlines()
    f.close()

with open("session.json", "w") as f:
    f.close()

client = Client()
client.login(user, pasw)
client.dump_settings("session.json")
