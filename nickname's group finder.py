import requests
import time

r = requests.get('https://www.roblox.com/groups/14770396/')
a = r.text
b = a.find("----")
found = str("Error")
# this is the part where it checks
if b : 
    found = [True]
else : found = False


print(found)
time.sleep(600)