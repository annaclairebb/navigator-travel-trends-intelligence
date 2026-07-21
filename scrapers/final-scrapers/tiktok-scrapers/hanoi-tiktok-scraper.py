from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_TOKEN = os.getenv("BRIGHTDATA_API_TOKEN")

if API_TOKEN is None:
    raise ValueError("BRIGHTDATA_API_TOKEN not found")

url = (
    "https://api.brightdata.com/datasets/v3/scrape"
    "?dataset_id=gd_lu702nij2f790tmv9h"
    "&type=discover_new"
    "&discover_by=keyword"
    "&notify=true"
    "&include_errors=true"
    "&limit_per_input=125"
    )

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({ 
    "input": [
        {
            "search_keyword":"travel hanoi",
            "num_of_posts":125,
            "country":""
        },
    
        {
            "search_keyword":"things to do in hanoi",
            "num_of_posts":125,
            "country":""
        },
        {
            "search_keyword":"day in hanoi",
            "num_of_posts":125,
            "country":""
        },
        {
            "search_keyword":"days in hanoi",
            "num_of_posts":125,
            "country":""
        },
        {
            "search_keyword":"#hanoi #travel",
            "num_of_posts":125,
            "country":""
        },
        {
            "search_keyword":"#visithanoi",
            "num_of_posts":125,
            "country":""
        },
        {
            "search_keyword":"#hanoitravel",
            "num_of_posts":125,
            "country":""
        },
        {
            "search_keyword":"#hanoiguide",
            "num_of_posts":125,
            "country":""
        }],
    "limit_per_input": 125,
})



response = requests.post(
    url, 
    headers=headers, 
    data=data
)

print(response.json())
print(response.status_code)

print(response.text)