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
    "&limit_per_input=86"
)

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

data = json.dumps({
    "input": [
        {
            "url":"https://www.google.com/maps/place/Miradouro+de+Santa+Catarina/@38.709485,-9.1503008,17z/data=!3m1!4b1!4m6!3m5!1s0xd1935fe69aa1429:0x93ac29cf91489a98!8m2!3d38.709485!4d-9.1477259!16s%2Fg%2F11mnh3bbf7?entry=ttu&g_ep=EgoyMDI2MDcyMS4wIKXMDSoASAFQAw%3D%3D",
            "days_limit":365,
            "sort_by":"Most relevant"
        },
    ],  
    "limit_per_input": 86,
})

response = requests.post(
    url, 
    headers=headers,
    data=data
)

print(response.json())
print(response.status_code)
print(response.text)