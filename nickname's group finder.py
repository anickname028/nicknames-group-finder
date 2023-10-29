import requests
import time
print("script has been started, sending request")

r = requests.get('https://youtube.com')
a = r.text
b = a.find("sadasdasdfasdasdasdsad adfafsafdsfsgdfsfsdf")
found = str("Error")
print(b)
# this is the part where it checks
if b : found = True
else : found = False



print(found)
time.sleep(5)