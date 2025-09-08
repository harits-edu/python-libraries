import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

tmp = response.json()

for result in tmp["results"]:
    print(result["trackName"])