from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_TOKEN = os.getenv("BRIGHTDATA_API_TOKEN")

if API_TOKEN is None:
    raise ValueError("BRIGHTDATA_API_TOKEN not found")

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

keywords = [
    "travel lisbon",
    "#lisbon"
    "#lisbon #travel",
    "things to do in lisbon",
    "day in lisbon",
    "days in lisbon",
    "#visitlisbon"
]

payload = {
    "input": [
        {
            "search_keyword": keyword,
            "country": "GB",
            "num_of_posts": 1,
        }
        for keyword in keywords
    ],
    "limit_per_input": 1,
}

response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)


# payload = {
#     "input": [
#         {
#             "search_keyword": "#travel #lisbon",
#             "country": "GB",
#             "num_of_posts": 1,
#         },
#         {
#             "search_keyword": "travel lisbon",
#             "country": "GB",
#             "num_of_posts": 1,
#         },
#     ],
#     "limit_per_input": 1,
# }