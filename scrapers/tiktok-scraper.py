import os
import requests

API_TOKEN = os.environ["a54db300-b924-4c15-a48f-954f1af33950"]

url = (
    "https://api.brightdata.com/datasets/v3/scrape"
    "?dataset_id=gd_lu702nij2f790tmv9h"
    "&notify=false"
    "&include_errors=true"
    "&type=discover_new"
    "&discover_by=keyword"
    "&limit_per_input=2"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

payload = {
    "input": [
        {
            "search_keyword": "#travel #lisbon",
            "country": "GB",
            "num_of_posts": 1,
        },
        {
            "search_keyword": "travel lisbon",
            "country": "GB",
            "num_of_posts": 1,
        },
    ],
    "limit_per_input": 1,
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)