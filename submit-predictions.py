import requests
import json
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    url = "https://www.wcooley.net/api/submit-predictions"
    with open("simulation_results.json", "r") as f:
        data = json.load(f)

    payload = {"name": name, "data": data}

    response = requests.post(url, json=payload)

    print(response)