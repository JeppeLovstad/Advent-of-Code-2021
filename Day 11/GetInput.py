from pip._vendor import requests
import sys
import re


try:
    with open("TOKEN", "r") as file:
        TOKEN = file.readline()
except:
    print("no token, shutting down")
    exit()

path = sys.path[0]+"\input.txt"
m = re.search(r'\d+$', sys.path[0])
day = int(m.group()) if m else 0
URL = f"https://adventofcode.com/2021/day/{day}/input"
token = {"session": TOKEN}
USER_AGENT = {"User-Agent": "advent-of-code-data v{}".format(1)}

response = requests.get(url=URL, cookies=token, headers=USER_AGENT)
data = response.text

with open(path, "w") as f:
    f.write(data)
