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
    "?dataset_id=gd_luzfs1dn2oa0teb81"
    "&notify=true"
    "&include_errors=true"
    "&limit_per_input=134"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        {
            "url":"https://www.google.com/maps/place/Dong+xuan+market/@21.0381484,105.8474638,17z/data=!3m1!4b1!4m6!3m5!1s0x3135ab005a92c3ff:0x6fa5382220f93152!8m2!3d21.0381434!4d105.8500387!16s%2Fg%2F11y84f4rcg?entry=ttu&g_ep=EgoyMDI2MDcyMS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
    ],  
    "limit_per_input": 134,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)