import json

with open("data.json", "r") as data_file:
    # read data
    data_js = json.load(data_file)
    website = "ebay"
    email = data_js[website]["email"]
    print(data_js[website]["email"])