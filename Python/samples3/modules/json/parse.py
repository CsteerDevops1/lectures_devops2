import json
from pprint import pprint

with open("data.json") as f:
    data = json.load(f)

pprint(data)

print(data["maps"][0]["id"])
print(data["masks"]["id"])
print(data["om_points"])

data["masks"]["id"] = "vvalore"
with open("data2.json", "w") as f:
    json.dump(data, f, sort_keys=True, indent=4)
