import requests
import time

r = requests.get('https://www.roblox.com/groups/14770396/')
a = r.text
print(a)
time.sleep(600)