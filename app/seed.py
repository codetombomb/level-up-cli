import requests
import json

resp = requests.get("http://numbersapi.com/random/year?json")
data = json.loads(resp.text)

breakpoint()