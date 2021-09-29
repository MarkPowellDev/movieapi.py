import requests
import json
import pprint
"""
I often need to manipulate JSON data for builds and deployments. This simple script Fetches API DATA, creates and then saves the JSON file in the directory. 
Example for demo purposes: https://www.tvmaze.com/api
Read & Write JSON in PY: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python
"""

url = "https://api.tvmaze.com/singlesearch/shows"
params = {"q": "Star Trek"} 
response = requests.get(url, params)

if response.status_code == 200:
    data = json.loads(response.text)
    pprint.pprint(data) # <-----  Human Readable
    with open('data.json', 'w') as outfile: # <--
        json.dump(data, outfile) #Creates a json file 
else:
    print(f"Error: {response.status_code}")
