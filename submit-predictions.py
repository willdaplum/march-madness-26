import requests
import json

if __name__ == "__main__":
    url = "https://www.wcooley.net/api/submit-predictions"
    with open("simulation_results.json", "r") as f:
        data = json.load(f)

    payload = {"name": "test", "data": data}

    response = requests.post(url, json=payload)

    print(response)